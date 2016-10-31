from django.shortcuts import render
from main import models
from bs4 import BeautifulSoup
from selenium import webdriver

import urllib

def index(request):
	#r = urllib.urlopen('https://sports.bwin.com/en/sports#sportId=4').read()
	#soup = BeautifulSoup(r, 'html.parser')
	driver = webdriver.PhantomJS()
	driver.get("https://sports.bwin.com/en/sports#sportId=4")
	elems = driver.find_elements_by_class_name("mb-option-button__option-odds")
	context = {
		#'soup': soup.find_all('form'),
		'site_title': 'Odds aggregator',
		'elems': elems[0].text,
		}
	return render(request, "main/index.html", context,)
