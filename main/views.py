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

# def find(driver):
#     element = driver.find_elements_by_class_name("mb-option-button__option-odds")
#     if element:
#         return element
#     else:
#         return False

def match_event():
	return True

def index(request):
	driver = webdriver.PhantomJS()
	driver.get("https://sports.betway.com/#/soccer/england/premier-league") #  BetWay
	elem_teams = driver.find_elements_by_class_name("event_name")
	elem_odds = driver.find_elements_by_class_name("outcome_button")
	odds = []
	teams = []
	events = []


	for el in elem_odds: 
		odds.append(el.text)
	for team in elem_teams:
		team1, team2 = team.text.split("-")
		teams.append(team1)
		teams.append(team2)

	for i in range(14):
		event = Event()
		event.team1 = teams[i*2]
		event.team2 = teams[i*2+1]
		event.win1 = odds[i*3]
		event.draw = odds[i*3+1]
		event.win2 = odds[i*3+2]
		events.append(event)



	driver.get("https://sports.bwin.com/en/sports#leagueIds=46&sportId=4") #  BWin
	elem_teams = driver.find_elements_by_class_name("mb-option-button__option-name")
	elem_odds = driver.find_elements_by_class_name("mb-option-button__option-odds")
	
	odds = []
	teams = []
	events2 = []

	for el in elem_odds: 
		odds.append(el.text)
	for team in elem_teams:
		teams.append(team.text)

	for i in range(len(elem_teams)/3):
		event = Event()
		event.team1 = teams[i*3]
		event.team2 = teams[i*3+2]
		event.win1 = odds[i*3]
		event.draw = odds[i*3+1]
		event.win2 = odds[i*3+2]
		events2.append(event)

	context = {
		'site_title': 'Odds aggregator',
		'odds': odds,
		'teams': teams,
		'events': events,
		'events2': events2,
		# 'dates': dates,
		# 'test': test,
		}
	return render(request, "main/index.html", context,)

def index0(request):
	driver = webdriver.PhantomJS()
	driver.get("https://sports.betway.com/#/soccer/england/premier-league") # Premier Liga BetWay
	elem_teams = driver.find_elements_by_class_name("event_name")
	elem_odds = driver.find_elements_by_class_name("outcome_button")
	#elem_dates = driver.find_elements_by_class_name("date")
	#trs = driver.find_elements_by_tag_name("tr")
	#test = []
	odds = []
	teams = []
	events = []
	#dates = []
	# for tr in trs: 
	# 	test.append(tr.text)	
	# for date in elem_dates: 
	# 	dates.append(date.text)

	for el in elem_odds: 
		odds.append(el.text)
	for team in elem_teams:
		team1, team2 = team.text.split("-")
		teams.append(team1)
		teams.append(team2)

	for i in range(14):
		event = Event()
		event.team1 = teams[i*2]
		event.team2 = teams[i*2+1]
		event.win1 = odds[i*3]
		event.draw = odds[i*3+1]
		event.win2 = odds[i*3+2]
		events.append(event)



	driver.get("https://sports.bwin.com/en/sports#leagueIds=46&sportId=4") # Premier Liga BWin
	elem_teams = driver.find_elements_by_class_name("mb-option-button__option-name")
	elem_odds = driver.find_elements_by_class_name("mb-option-button__option-odds")
	
	odds = []
	teams = []
	events2 = []

	for el in elem_odds: 
		odds.append(el.text)
	for team in elem_teams:
		teams.append(team.text)

	for i in range(len(elem_teams)/3):
		event = Event()
		event.team1 = teams[i*3]
		event.team2 = teams[i*3+2]
		event.win1 = odds[i*3]
		event.draw = odds[i*3+1]
		event.win2 = odds[i*3+2]
		events2.append(event)

	context = {
		'site_title': 'Odds aggregator',
		'odds': odds,
		'teams': teams,
		'events': events,
		'events2': events2,
		# 'dates': dates,
		# 'test': test,
		}
	return render(request, "main/index.html", context,)




def index1(request):
	driver = webdriver.PhantomJS()
	driver.get("https://sports.betway.com/#/soccer/england/premier-league") # Premier Liga
	elem_teams = driver.find_elements_by_class_name("event_name")
	elem_odds = driver.find_elements_by_class_name("outcome_button")
	
	odds = []
	teams = []
	events = []

	for el in elem_odds: 
		odds.append(el.text)
	for team in elem_teams:
		team1, team2 = team.text.split("-")
		teams.append(team1)
		teams.append(team2)

	for i in range(4):
		event = Event()
		event.team1 = teams[i*2]
		event.team2 = teams[i*2+1]
		event.win1 = odds[i*3]
		event.draw = odds[i*3+1]
		event.win2 = odds[i*3+2]
		events.append(event)
	context = {
		'site_title': 'Odds aggregator',
		'odds': odds,
		'teams': teams,
		'events': events,
		}
	return render(request, "main/index.html", context,)

def index2(request):
	#r = urllib.urlopen('https://sports.bwin.com/en/sports#sportId=4').read()
	#soup = BeautifulSoup(r, 'html.parser')
	driver = webdriver.PhantomJS()
	#driver.get("https://sports.bwin.com/en/sports#sportId=4")
	driver.get("https://sports.bwin.com/en/sports#leagueIds=46&sportId=4") # Premier Liga BWin
	#driver.get("https://sports.bwin.com/en/sports#leagueIds=16108&sportId=4")  # La Liga
	
	#elems = WebDriverWait(driver, 10).until(find)
	
#	with self.wait_for_page_load(timeout=10):

	
	elem_teams = driver.find_elements_by_class_name("mb-option-button__option-name")
	elem_odds = driver.find_elements_by_class_name("mb-option-button__option-odds")
	#elem_teams = driver.find_elements_by_class_name("event_name")
	#elem_odds = driver.find_elements_by_class_name("outcome_button")

	# except StaleElementReferenceException: driver.implicitly_wait(10)
	
	odds = []
	teams = []
	events = []

	for el in elem_odds: 
		odds.append(el.text)
	for team in elem_teams:
		teams.append(team.text)

	for i in range(len(elem_teams)/3):
		event = Event()
		event.team1 = teams[i*3]
		event.team2 = teams[i*3+2]
		event.win1 = odds[i*3]
		event.draw = odds[i*3+1]
		event.win2 = odds[i*3+2]
		events.append(event)
	context = {
		#'soup': soup.find_all('form'),
		'site_title': 'Odds aggregator',
		'odds': odds,
		'teams': teams,
		'events': events,
		}
	return render(request, "main/index.html", context,)
