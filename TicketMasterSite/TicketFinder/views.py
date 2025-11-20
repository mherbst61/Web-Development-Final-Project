from contextlib import nullcontext
from datetime import datetime

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup

from TicketFinder.forms import ticketSearchForm
from TicketFinder.models import SavedTickets



# Create your views here.
def search(request):
    search_form = ticketSearchForm(request.POST or None)
    message = ""
    eventObject = []
    if request.method == "POST":
        if search_form.is_valid():
            apiKey = "Bd9NVuUJf6tdtp7GETrrQvkuMtOVm4fk"
            city = search_form.cleaned_data['city']
            genre = search_form.cleaned_data['genre']
            state = search_form.cleaned_data['state']
            print(city, genre)
            try:
                data = {}
                try:
                    response = requests.get(
                    "https://app.ticketmaster.com/discovery/v2/events.json?&sort=date,asc&countryCode=US&stateCode="+state+"&city=" + city + "&classificationName=" + genre + "&apikey=" + apiKey)
                    data = response.json()
                    if "_embedded" not in data:
                        message = "Events Not found Try different parameters"
                except :
                    message = "Error in the query attempt"
                #print(data)
                event_imageUrl = ""
                message= str(len(data["_embedded"]["events"])) + " Events Found"
                for event in data["_embedded"]["events"]:
                    for image in event["images"]:
                        if (image["width"] == 2048 and image["height"] == 1152):
                            event_imageUrl = image["url"]
                    event_name = event["name"]
                    ticket_id = event["id"]
                    theater_name = event["_embedded"]["venues"][0]["name"]
                    theater_address1 = event["_embedded"]["venues"][0]["address"]["line1"]
                    theater_city = event["_embedded"]["venues"][0]["city"]["name"]
                    theater_state = event["_embedded"]["venues"][0]["state"]["name"]
                    theater_zip = event["_embedded"]["venues"][0]["postalCode"]
                    theater_address2 = theater_city + ", " + theater_state + ", " + theater_zip
                    event_url = event["url"]
                    event_dateTimeString = event["dates"]["start"]["dateTime"]
                    if (event_dateTimeString or event_dateTimeString == ""):
                        try:
                            event_dateTime = datetime.fromisoformat(event_dateTimeString)
                            event_ConvertedDate = event_dateTime.strftime("%a %b %d, %Y")
                            event_ConvertedTime = event_dateTime.strftime("%I:%M %p")
                        except Exception as d:
                            print(d)
                    else:
                        event_ConvertedDate =""
                        event_ConvertedTime=""

                #print(event_name)
                #print(event_dateTime)
                #print("Converted Date and time: " + event_ConvertedDate + " " + event_ConvertedTime)
                    ticket = {
                        "event_name": event_name,
                        "event_url": event_url,
                        "theater_name": theater_name,
                        "theater_address1": theater_address1,
                        "theater_address2": theater_address2,
                        "event_imageUrl": event_imageUrl,
                        "event_ConvertedDate": event_ConvertedDate,
                        "event_ConvertedTime": event_ConvertedTime,
                        "ticket_id":ticket_id,
                    }
                    eventObject.append(ticket)

            except Exception as e:
                print("Exception: ", e)
       # if(save_TicketForm.is_valid()):

    context = {
        'search_form': search_form,
        'tickets': eventObject,
        'message': message
    }
    return render(request, 'ticketmasterhtml.html', context)

def SavedTicket(request):
    if request.method == "POST":
        print("save called")
        event_name= request.POST["event_name"]
        print(event_name)
        event_url= request.POST["event_url"]
        print(event_url)
        theater_name= request.POST["theater_name"]
        print(theater_name)
        theater_address1 = request.POST["theater_address1"]
        print(theater_address1)
        theater_address2 = request.POST["theater_address2"]
        print(theater_address2)
        event_imageUrl= request.POST["event_imageUrl"]
        print(event_imageUrl)
        event_ConvertedDate= request.POST["event_ConvertedDate"]
        print(event_ConvertedDate)
        event_ConvertedTime= request.POST["event_ConvertedTime"]
        print(event_ConvertedTime)
        ticket_id= request.POST["ticket_id"]
        print(ticket_id)
        SavedTickets.objects.create(event_name=event_name, event_url=event_url, theater_name=theater_name,theater_address1=theater_address1,theater_address2=theater_address2,event_imageUrl=event_imageUrl,event_ConvertedDate=event_ConvertedDate,event_ConvertedTime=event_ConvertedTime,ticket_id=ticket_id)
        return JsonResponse({"message":"Ticket Saved"})
    return JsonResponse({"message":"Error Ticket Not saved"})


def loadTickets(request):
    ticket = SavedTickets.objects.all()
    context = {'tickets': ticket}
    return render(request, 'load_saved tickets.html', context)

def deleteTicket(request, ticket_id):
    print("from delete ticket",request)
    if SavedTickets.objects.filter(ticket_id=ticket_id).exists():
        ticket = SavedTickets.objects.get(ticket_id=ticket_id)
        ticket.delete()
        return JsonResponse({'deleted':True,'message':'Ticket Deleted'})
    else:
        return JsonResponse({'deleted':False,'message':'Ticket Not saved'})
