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

from decimal import Decimal

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

def t(team):
	if "Arsenal" in team:
		return "Arsenal"
	if "Bournemouth" in team:
		return "Bournemouth"
	if "Burnley" in team:
		return "Burnley"
	if "Chelsea" in team:
		return "Chelsea"
	if "Crystal Palace" in team:
		return "Crystal Palace"
	if "Everton" in team:
		return "Everton"
	if "Hull City" in team:
		return "Hull City"
	if "Leicester" in team:
		return "Leicester City"
	if "Liverpool" in team:
		return "Liverpool"
	if "Manchester City" in team:
		return "Manchester City"
	if "Middlesbrough" in team:
		return "Middlesbrough"
	if "Southampton" in team:
		return "Southampton"
	if "Sunderland" in team:
		return "Sunderland"
	if "Stoke" in team:
		return "Stoke City"
	if "Sunderland" in team:
		return "Sunderland"
	if "Swansea" in team:
		return "Swansea City"
	if "Tottenham" in team:
		return "Tottenham"
	if "Watford" in team:
		return "Watford"
	if "West Bromwich" in team:
		return "West Bromwich Albion"
	if "West Ham" in team:
		return "West Ham United"		
	return team
		
def match_event():
	return True
def index1111(request):

	driver = webdriver.PhantomJS()
	driver.get("https://sports.betway.com/#/soccer/england/premier-league") #  BetWay
	elem_teams = driver.find_elements_by_class_name("event_name")
	elem_odds = driver.find_elements_by_class_name("outcome_button")
	odds = []
	teams = []
	events = []


	for team in elem_teams:
		team1, team2 = team.text.split("-")
		teams.append(team1)
		teams.append(team2)
	
	for el in elem_odds:
		odds.append(el.text)

	
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
	#odds = ['1.65', '3.80' '5.50', '3.10', '3.25', '2.37', '1.22', '6.00', '15.00', '2.00', '3.50', '3.80', '1.55', '4.33', '5.75', '1.95', '3.40', '4.00'] 

	for i in range(len(elem_teams)/3):
		event = Event()
		event.team1 = teams[i*3]
		event.team2 = teams[i*3+2]
		event.win1 = odds[i*3]
		event.draw = odds[i*3+1]
		event.win2 = odds[i*3+2]
		events2.append(event)
	
	#driver.get("https://www.parimatch.com/en/sport/futbol/anglija-premer-liga")
	
	####!!!!!!!!!! ----- Marathonbet	
	#driver.get("https://www.marathonbet.com/en/betting/Football/England/Premier+League/?menu=21520")
	#event3 = driver.find_elements_by_class_name('name')
	#############

	
	driver.get("https://www.fonbet.com/bets/?locale=en#11918")
	event3 = driver.find_elements_by_class_name('eventNumber')
	teams = []
	

	
	for team in event3:
		teams.append(team.text)

	context = {
		'site_title': 'Odds aggregator',
		'odds': odds,
		'teams': teams,
		'events': events,
		'events2': events2,
		# 'event3': len(event3),
		# 'dates': dates,
		# 'test': test,
		}
	return render(request, "main/index.html", context,)


class Ev():
	def __init__(self, team1, team2):
		self.team1 = team1
		self.team2 = team2
		self.odds = []

	def add_odds(self, od):
		self.odds.append(od)

class Od():
	def __init__(self, win1, win2, draw):
		self.win1 = win1
		self.win2 = win2
		self.draw = draw
        #self.book = book
        
	

def index(request):
	# driver = webdriver.PhantomJS()
	# driver.get("https://sports.betway.com/#/soccer/england/premier-league") #  BetWay
	# elem_teams = driver.find_elements_by_class_name("event_name")
	# elem_odds = driver.find_elements_by_class_name("outcome_button")
	# odds = []
 	teams = []
	events = []
	odds = ['1.65', '3.80', '5.50', '3.10', '3.25', '2.37', '1.22', '6.00', '15.00', '2.00', '3.50', '3.80', '1.55', '4.33', '5.75', '1.95', '3.40', '4.00'] 
	elem_teams = ['Bournemouth - Sunderland', 'Burnley - Crystal Palace', 'Manchester City - Middlesbrough', 'West Ham - Stoke', 'Chelsea - Everton', 'Arsenal - Tottenham']
	# for el in elem_odds: 
	# 	odds.append(el.text)
	for team in elem_teams:
		# team1, team2 = team.text.split("-")
		data = team.split(" - ")
		if len(data) == 2:
			team1, team2 = team.split(" - ", 2)
		
		teams.append(t(team1))
		teams.append(t(team2))

	for i in range(6):
		event = Ev(teams[i*2],teams[i*2+1])
		od = Od(Decimal(odds[i*3]), Decimal(odds[i*3+2]), Decimal(odds[i*3+1]))
		event.add_odds(od)
		events.append(event)

	#driver.get("https://sports.bwin.com/en/sports#leagueIds=46&sportId=4") #  BWin
	#elem_teams = driver.find_elements_by_class_name("mb-option-button__option-name")
	#elem_odds = driver.find_elements_by_class_name("mb-option-button__option-odds")
	
	#odds = []
	teams = []
	events2 = []
	test = []
	elem_teams = ['West Ham United', 'Stoke City', 'Bournemouth', 'Sunderland', 'Manchester City', 'Middlesbrough FC', 'Burnley', 'Crystal Palace', 'Chelsea FC', 'Everton', 'Arsenal FC', 'Tottenham Hotspur']
	odds = ['1.55', '3.90', '5.50', '3.20', '3.15', '2.30', '1.32', '6.05', '14.00', '2.10', '3.40', '3.70', '1.55', '4.23', '5.80', '1.90', '3.50', '4.00'] 
	# for el in elem_odds: 
	# 	odds.append(el.text)
	for team in elem_teams:
		# teams.append(team.text)
		teams.append(team)
	# for i in range(len(elem_teams)/3):
	for i in range(6):
		event = Event()
		#event.team1 = teams[i*3]
		#event.team2 = teams[i*3+2]
		event.team1 = t(teams[i*2])
		event.team2 = t(teams[i*2+1])
		event.win1 = Decimal(odds[i*3])
		event.draw = Decimal(odds[i*3+1])
		event.win2 = Decimal(odds[i*3+2])
		events2.append(event)
	for i in range(6):
		if events[i] == events2[i]:
			test.append("yes")
		else:
			test.append("no")



	context = {
		'site_title': 'Odds aggregator',
		'odds': odds,
		'teams': teams,
		'events': events,
		'events2': events2,
		
		# 'dates': dates,
		'test': test,
		}
	return render(request, "main/index.html", context,)








def index2222(request):
	# driver = webdriver.PhantomJS()
	# driver.get("https://sports.betway.com/#/soccer/england/premier-league") #  BetWay
	# elem_teams = driver.find_elements_by_class_name("event_name")
	# elem_odds = driver.find_elements_by_class_name("outcome_button")
	# odds = []
 	teams = []
	events = []
	odds = ['1.65', '3.80', '5.50', '3.10', '3.25', '2.37', '1.22', '6.00', '15.00', '2.00', '3.50', '3.80', '1.55', '4.33', '5.75', '1.95', '3.40', '4.00'] 
	elem_teams = ['Bournemouth - Sunderland', 'Burnley - Crystal Palace', 'Manchester City - Middlesbrough', 'West Ham - Stoke', 'Chelsea - Everton', 'Arsenal - Tottenham']
	# for el in elem_odds: 
	# 	odds.append(el.text)
	for team in elem_teams:
		# team1, team2 = team.text.split("-")
		data = team.split(" - ")
		if len(data) == 2:
			team1, team2 = team.split(" - ", 2)
		
		teams.append(t(team1))
		teams.append(t(team2))

	for i in range(6):
		event = Event()
		event.team1 = teams[i*2]
		event.team2 = teams[i*2+1]
		event.win1 = Decimal(odds[i*3])
		event.draw = Decimal(odds[i*3+1])
		event.win2 = Decimal(odds[i*3+2])
		events.append(event)

	#driver.get("https://sports.bwin.com/en/sports#leagueIds=46&sportId=4") #  BWin
	#elem_teams = driver.find_elements_by_class_name("mb-option-button__option-name")
	#elem_odds = driver.find_elements_by_class_name("mb-option-button__option-odds")
	
	#odds = []
	teams = []
	events2 = []
	test = []
	elem_teams = ['West Ham United', 'Stoke City', 'Bournemouth', 'Sunderland', 'Manchester City', 'Middlesbrough FC', 'Burnley', 'Crystal Palace', 'Chelsea FC', 'Everton', 'Arsenal FC', 'Tottenham Hotspur']
	odds = ['1.55', '3.90', '5.50', '3.20', '3.15', '2.30', '1.32', '6.05', '14.00', '2.10', '3.40', '3.70', '1.55', '4.23', '5.80', '1.90', '3.50', '4.00'] 
	# for el in elem_odds: 
	# 	odds.append(el.text)
	for team in elem_teams:
		# teams.append(team.text)
		teams.append(team)
	# for i in range(len(elem_teams)/3):
	for i in range(6):
		event = Event()
		#event.team1 = teams[i*3]
		#event.team2 = teams[i*3+2]
		event.team1 = t(teams[i*2])
		event.team2 = t(teams[i*2+1])
		event.win1 = Decimal(odds[i*3])
		event.draw = Decimal(odds[i*3+1])
		event.win2 = Decimal(odds[i*3+2])
		events2.append(event)
	for i in range(6):
		if events[i] == events2[i]:
			test.append("yes")
		else:
			test.append("no")



	context = {
		'site_title': 'Odds aggregator',
		'odds': odds,
		'teams': teams,
		'events': events,
		'events2': events2,
		
		# 'dates': dates,
		'test': test,
		}
	return render(request, "main/index.html", context,)

































def index00(request):
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
	#odds = ['1.65', '3.80' '5.50', '3.10', '3.25', '2.37', '1.22', '6.00', '15.00', '2.00', '3.50', '3.80', '1.55', '4.33', '5.75', '1.95', '3.40', '4.00'] 

	for i in range(len(elem_teams)/3):
		event = Event()
		event.team1 = teams[i*3]
		event.team2 = teams[i*3+2]
		event.win1 = odds[i*3]
		event.draw = odds[i*3+1]
		event.win2 = odds[i*3+2]
		events2.append(event)
	event3 = events[0]
	for event in events:
		if event == events2[3]:
			event3 = event



	context = {
		'site_title': 'Odds aggregator',
		'odds': odds,
		'teams': teams,
		'events': events,
		'events2': events2,
		'event3': event3,
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
