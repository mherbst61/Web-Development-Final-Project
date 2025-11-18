from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from TicketFinder.forms import ticketSearchForm


# Create your views here.
def search(request):

    form = ticketSearchForm(request.POST or None)
    message = ""
    eventObject = []
    if request.method == "POST":
        if form.is_valid():
            apiKey = "Bd9NVuUJf6tdtp7GETrrQvkuMtOVm4fk"
            city = form.cleaned_data['city']
            genre = form.cleaned_data['genre']
            print(city, genre)
            try:
                response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?&sort=date,asc&countryCode=US&city=" + city + "&classificationName=" + genre + "&apikey=" + apiKey)
                data = response.json()
                #print(data)
                for event in data["_embedded"] ["events"]:
                    event_name = event["name"]
                    event_url = event["url"]
                    print(event_name)
                    ticket = {
                        "event_name": event_name,
                        "event_url": event_url,
                    }
                    eventObject.append(ticket)

            except:
                print("No results found")
                message = "No results found"
    context = {
        'form': form,
        'tickets': eventObject,
        'message' : message
    }
    return render(request,'ticketmasterhtml.html', context)