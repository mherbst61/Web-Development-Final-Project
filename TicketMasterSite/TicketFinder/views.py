from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

from TicketFinder.forms import ticketSearchForm


# Create your views here.
def Search(request):

    form = ticketSearchForm(request.GET or None)
    if(request.method == "GET"):
        if(form.is_valid()):
            apiKey = "Bd9NVuUJf6tdtp7GETrrQvkuMtOVm4fk"
            city = form.cleaned_data['city']
            genre = form.cleaned_data['genre']
            response = requests.get("https://app.ticketmaster.com/discovery/v2/events.json?&sort=date,asc&countryCode=US&city=" + city + "&classificationName=" + genre + "&apikey=" + apiKey)
            print(response.json())

    context = {'form': form}
    return render(request,'ticketmasterhtml.html', context)