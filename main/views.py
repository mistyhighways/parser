from django.shortcuts import render
from main import models
from models import Event
#from bs4 import BeautifulSoup
from selenium import webdriver
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import staleness_of

from selenium.common.exceptions import StaleElementReferenceException

import urllib

# @contextmanager
# def wait_for_page_load(self, timeout=30):
#     old_page = self.driver.find_element_by_tag_name('html')
#     yield
#     WebDriverWait(self.driver, timeout).until(staleness_of(old_page))

def find(driver):
    element = driver.find_elements_by_class_name("mb-option-button__option-odds")
    if element:
        return element
    else:
        return False

#def addEvent():
def index(request):
	#r = urllib.urlopen('https://sports.bwin.com/en/sports#sportId=4').read()
	#soup = BeautifulSoup(r, 'html.parser')
	driver = webdriver.PhantomJS()
	#driver.get("https://sports.bwin.com/en/sports#sportId=4")
	driver.get("https://sports.bwin.com/en/sports#leagueIds=46&sportId=4")
	#elems = WebDriverWait(driver, 10).until(find)
	
#	with self.wait_for_page_load(timeout=10):

	
	teams = driver.find_elements_by_class_name("mb-option-button__option-name")
	elems = driver.find_elements_by_class_name("mb-option-button__option-odds")
	# except StaleElementReferenceException: driver.implicitly_wait(10)
	
	odds = []
	ts = []
	events = []

	for el in elems: 
		odds.append(el.text)
	for team in teams:
		ts.append(team.text)

	for i in range(len(teams)/3):
		ev = Event()
		ev.team1 = ts[i*3]
		ev.team2 = ts[i*3+2]
		ev.win1 = odds[i*3]
		ev.draw = odds[i*3+1]
		ev.win2 = odds[i*3+2]
		events.append(ev)
	context = {
		#'soup': soup.find_all('form'),
		'site_title': 'Odds aggregator',
		'odds': odds,
		'teams': ts,
		'events': events,
		}
	return render(request, "main/index.html", context,)
