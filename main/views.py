from django.shortcuts import render
from main import models
from bs4 import BeautifulSoup
import urllib

def index(request):
	r = urllib.urlopen('https://sports.bwin.com/en/sports#sportId=4').read()
	soup = BeautifulSoup(r, 'html.parser')

	context = {
		'soup': soup.find_all('form'),
		'site_title': 'Odds aggregator',
		}
	return render(request, "main/index.html", context,)
