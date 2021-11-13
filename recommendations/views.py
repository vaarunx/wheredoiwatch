from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from imdb import IMDb


from .forms import SearchForm

# Create your views here.

"""
import requests

url = "https://streaming-availability.p.rapidapi.com/get/basic"

querystring = {"country":"us","tmdb_id":"movie/120","output_language":"en"}

headers = {
    'x-rapidapi-host': "streaming-availability.p.rapidapi.com",
    'x-rapidapi-key': "fd72cb71a9msh1fa6a2791e31886p1c79aejsne23a14ea8bd6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

"""


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['name']
            country = form.cleaned_data['country']
            print(name)
            print(country)
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'recommendations/search.html', {'form': form})