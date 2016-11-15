# -*- coding: utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
from django.shortcuts import render
#from main import models
#from models import Event
#from bs4 import BeautifulSoup
from selenium import webdriver
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.common.exceptions import StaleElementReferenceException

import urllib

from decimal import Decimal
TWO_PLACES = Decimal("0.01")

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
    if "Arsenal" in team or "Арсенал" in team:
        return "Arsenal"
    if "Bournemouth" in team or "Борнм" in team:
        return "Bournemouth"
    if "Burnley" in team or "рнли" in team:
        return "Burnley"
    if "Chelsea" in team or "Челси" in team:
        return "Chelsea"
    if "Crystal Palace" in team or "Кристал" in team:
        return "Crystal Palace"
    if "Everton" in team or "Эвертон" in team:
        return "Everton"
    if "Hull City" in team or "Халл" in team:
        return "Hull City"
    if "Leicester" in team or "Лестер" in team:
        return "Leicester City"
    if "Liverpool" in team or "Ливерпуль" in team:
        return "Liverpool"
    if "Manchester City" in team or "Man City" in team or "Манчестер Сити" in team: 
        return "Manchester City"
    if "Manchester United" in team or "Manchester Utd" in team or "Манчестер Ю" in team:
        return "Manchester United"
    if "Middlesbrough" in team or "длсбро" in team:
        return "Middlesbrough"
    if "Southampton" in team or "Саутг" in team:
        return "Southampton"
    if "Stoke" in team or "Сток" in team:
        return "Stoke City"
    if "Sunderland" in team or "Сандерл" in team:
        return "Sunderland"
    if "Swansea" in team or "Суонси" in team:
        return "Swansea City"
    if "Tottenham" in team or "Тоттен" in team:
        return "Tottenham"
    if "Watford" in team or "Уотфорд" in team:
        return "Watford"
    if "West Brom" in team or "Вест Бром" in team:
        return "West Bromwich Albion"
    if "West Ham" in team or "Вест Хэм" in team:
        return "West Ham United"        
    return team


class Ev():
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.odds = []
        self.time = None
        self.max_odds = []

    def add_odds(self, od):
        self.odds.append(od)

    def set_time(self, time):
        self.time = time

    def set_max(self):
        self.max_odds.append(max(bet.win1 for bet in self.odds))
        self.max_odds.append(max(bet.draw for bet in self.odds))
        self.max_odds.append(max(bet.win2 for bet in self.odds))
        self.max_odds.append(max(bet.o1x for bet in self.odds))
        self.max_odds.append(max(bet.o12 for bet in self.odds))
        self.max_odds.append(max(bet.ox2 for bet in self.odds))

    def __eq__(self, other):                            # comparing class instances
        if not isinstance(other, type(self)):
            return False
        return ((self.team1, self.team2) == (other.team1, other.team2))

class Od():
    def __init__(self, win1, win2, draw, bookmaker):
        if "Marathonbet" in bookmaker:
            self.win1 = self.transform_to_decimal(win1)
            self.draw = self.transform_to_decimal(draw)
            self.win2 = self.transform_to_decimal(win2)
        else:
            self.win1 = Decimal(win1).quantize(TWO_PLACES)
            self.win2 = Decimal(win2).quantize(TWO_PLACES)
            self.draw = Decimal(draw).quantize(TWO_PLACES)
        self.o1x = None
        self.o12 = None
        self.ox2 = None
        self.bookmaker = bookmaker

    def set_other_odds(self, o1x, o12, ox2):
        if "Marathonbet" in self.bookmaker:
            self.o1x = self.transform_to_decimal(o1x)
            self.o12 = self.transform_to_decimal(o12)
            self.ox2 = self.transform_to_decimal(ox2)
        else:
            self.o1x = Decimal(o1x).quantize(TWO_PLACES)
            self.o12 = Decimal(o12).quantize(TWO_PLACES)
            self.ox2 = Decimal(ox2).quantize(TWO_PLACES)

    def transform_to_decimal(self, var):
        data = var.split("/")
        if len(data) == 2:
            one, two = var.split("/", 2)
            return (Decimal(one)/Decimal(two) + 1).quantize(TWO_PLACES)
        
def index(request):
    #driver = webdriver.PhantomJS()
    # driver.get("https://sports.betway.com/#/soccer/england/premier-league")             #  BetWay
    # elem_teams = driver.find_elements_by_class_name("event_name")
    # elem_odds = driver.find_elements_by_class_name("outcome_button")
    odds = []
    teams = []
    events = []

    # for team in elem_teams:
    #     data = team.text.split(" - ")
    #     if len(data) == 2:
    #         team1, team2 = team.text.split(" - ", 2)

    #     teams.append(t(team1))
    #     teams.append(t(team2))
    teams = ['Manchester United', 'Arsenal', 'Crystal Palace', 'Manchester City', 'Everton', 'Swansea City', 'Southampton', 'Liverpool', 'Chelsea', 'Tottenham', 'Crystal Palace', 'Manchester United', 'Everton', 'Leicester', 'Southampton', 'Stoke City', 'Burnley', 'Arsenal', 'Everton', 'Manchester City', 'West Ham', 'Swansea City', 'Southampton', 'Burnley']
    odds = ['1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34']
    # for el in elem_odds:
    #     odds.append(el.text)

    for i in range(10):
        event = Ev(teams[i*2],teams[i*2+1])
        od = Od(odds[i*3], odds[i*3+2], odds[i*3+1], "BetWay")
        event.add_odds(od)
        events.append(event)

    #driver.get("https://sports.bwin.com/en/sports#leagueIds=46&sportId=4")                  #  BWin
    # elem_teams = driver.find_elements_by_class_name("mb-option-button__option-name")
    # elem_odds = driver.find_elements_by_class_name("mb-option-button__option-odds") 
    # odds = []
    # teams = []
    # events2 = []

    # for team in elem_teams:
    #     teams.append(t(team.text))
    # for el in elem_odds: 
    #     odds.append(el.text)

    teams = ['Manchester United', 'Arsenal', 'Crystal Palace', 'Manchester City', 'Everton', 'Swansea City', 'Southampton', 'Liverpool', 'Chelsea', 'Tottenham', 'Crystal Palace', 'Manchester United', 'Everton', 'Leicester', 'Southampton', 'Stoke City', 'Burnley', 'Arsenal', 'Everton', 'Manchester City', 'West Ham', 'Swansea City', 'Southampton', 'Burnley']
    odds = ['1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34']

    for i in range(10):
        event = Ev(teams[i*2], teams[i*2+1])

        od = Od('3.56', '5.31', '1.15', "BWin")
        for ev in events:
            if ev == event:
                ev.add_odds(od)
        # else:
        #   event.add_odds(od)
        #   events.append(event)
        event.add_odds(od)


    
    # driver.get("https://www.marathonbet.com/en/betting/Football/England/Premier+League/?menu=21520") # Marathonbet
    # elem_teams = driver.find_elements_by_class_name('member-name')
    # elem_odds = driver.find_elements_by_class_name("price") 
    # elem_times = driver.find_elements_by_class_name("date") 
    # odds = []
    # teams = []
    times = ['19 Nov 12:30', '19 Nov 15:00', '19 Nov 15:00', '20 Nov 12:30', '20 Nov 12:30', '20 Nov 12:30', '20 Nov 15:00', '20 Nov 16:00', '21 Nov 12:30', '21 Nov 12:30', '22 Nov 14:30']
    teams = ['Manchester United', 'Arsenal', 'Crystal Palace', 'Manchester City', 'Everton', 'Swansea City', 'Southampton', 'Liverpool', 'Chelsea', 'Tottenham', 'Crystal Palace', 'Manchester United', 'Everton', 'Leicester', 'Southampton', 'Stoke City', 'Burnley', 'Arsenal', 'Everton', 'Manchester City', 'West Ham', 'Swansea City', 'Southampton', 'Burnley']
    odds = ['1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34']
    

    # for team in elem_teams:
    #     teams.append(t(team.text))
    # for el in elem_odds: 
    #     odds.append(el.text)
    # for time in elem_times: 
    #     times.append(time.text)

    for i in range(10):
        event = Ev(teams[i*2], teams[i*2+1])
        od = Od('48/13', '4/23', '29/13', "Marathonbet")
        od.set_other_odds('14/18', '7/41', '39/15')
        for ev in events:
            if ev == event:
                ev.add_odds(od)
                ev.set_time(times[i])
    # i = 0
    # for ev in events:
    #     od = Od('48/13', '4/23', '29/13', "Marathonbet")
    #     od.set_other_odds('14/18', '7/41', '39/15')
    #     ev.add_odds(od)
    #     ev.set_time('Nov 19')
        

        #event.add_odds(od)
        
    #driver.get("https://www.parimatch.com/en/sport/futbol/anglija-premer-liga")
        
    # driver.get("https://www.fonbet.com/bets/?locale=en#11918")
    # event3 = driver.find_elements_by_class_name('eventNumber')
    # teams = []
    
    # driver.get("http://olimp.com/betting/index.php?page=line&action=2&sel[]=11664") # Olimp
    # elem_teams = driver.find_elements_by_class_name("m")
    # elem_odds = driver.find_elements_by_class_name("bet_sel") 
    
    # odds = []
    # teams = []
    
    # events4 = []

    teams = ['Manchester United', 'Arsenal', 'Crystal Palace', 'Manchester City', 'Everton', 'Swansea City', 'Southampton', 'Liverpool', 'Chelsea', 'Tottenham', 'Crystal Palace', 'Manchester United', 'Everton', 'Leicester', 'Southampton', 'Stoke City', 'Burnley', 'Arsenal', 'Everton', 'Manchester City', 'West Ham', 'Swansea City', 'Southampton', 'Burnley']
    odds = ['1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34', '1.02', '2.12', '3.32', '1.51', '2.53', '3.56', '1.05', '2.34']

    # for team in elem_teams:
    #     data = team.text.split(" - ")
    #     if len(data) == 2:
    #         team1, team2 = team.text.split(" - ", 2)

    #     teams.append(t(team1))
    #     teams.append(t(team2))  
    # for el in elem_odds: 
    #     odds.append(el.text)


    for i in range(10):
        event = Ev(teams[i*2], teams[i*2+1])
        od = Od(odds[i*3], odds[i*3+2], odds[i*3+1], "Olimp")
        od.set_other_odds('1.25', '2.17', '5.42')
        for ev in events:
            if ev == event:
                ev.add_odds(od)
                ev.set_max()
                ev.set_time(times[i])
            request.session[ev.team1 + '-' + ev.team2] = ev

        #event.add_odds(od)
        
        # events4.append(event)


    context = {
        'site_title': 'Odds aggregator',
        # 'odds': odds,
        # 'teams': teams,
        'events': events,
        # 'times': times,
        # 'event3': len(event3),
        # 'dates': dates,
        # 'test': test,
        }
    return render(request, "main/index.html", context,)













def index_good(request):
    driver = webdriver.PhantomJS()
    driver.get("https://sports.betway.com/#/soccer/england/premier-league")             #  BetWay
    elem_teams = driver.find_elements_by_class_name("event_name")
    elem_odds = driver.find_elements_by_class_name("outcome_button")
    odds = []
    teams = []
    events = []

    for team in elem_teams:
        data = team.text.split(" - ")
        if len(data) == 2:
            team1, team2 = team.text.split(" - ", 2)

        teams.append(t(team1))
        teams.append(t(team2))  
    for el in elem_odds:
        odds.append(el.text)

    for i in range(10):
        event = Ev(teams[i*2],teams[i*2+1])
        od = Od(odds[i*3], odds[i*3+2], odds[i*3+1], "BetWay")
        event.add_odds(od)
        events.append(event)

    driver.get("https://sports.bwin.com/en/sports#leagueIds=46&sportId=4")                  #  BWin
    elem_teams = driver.find_elements_by_class_name("mb-option-button__option-name")
    elem_odds = driver.find_elements_by_class_name("mb-option-button__option-odds") 
    odds = []
    teams = []
    events2 = []

    for team in elem_teams:
        teams.append(t(team.text))
    for el in elem_odds: 
        odds.append(el.text)

    for i in range(len(elem_teams)/3):
        event = Ev(teams[i*3], teams[i*3+2])

        od = Od(odds[i*3], odds[i*3+2], odds[i*3+1], "BWin")
        for ev in events:
            if ev == event:
                ev.add_odds(od)
        # else:
        #   event.add_odds(od)
        #   events.append(event)
        event.add_odds(od)
        events2.append(event)

    
    driver.get("https://www.marathonbet.com/en/betting/Football/England/Premier+League/?menu=21520") # Marathonbet
    elem_teams = driver.find_elements_by_class_name('member-name')
    elem_odds = driver.find_elements_by_class_name("price") 
    elem_times = driver.find_elements_by_class_name("date") 
    odds = []
    teams = []
    times = []
    events3 = []

    for team in elem_teams:
        teams.append(t(team.text))
    for el in elem_odds: 
        odds.append(el.text)
    for time in elem_times: 
        times.append(time.text)

    for i in range(len(elem_teams)/2):
        event = Ev(teams[i*2], teams[i*2+1])
        od = Od(odds[i*10], odds[i*10+2], odds[i*10+1], "Marathonbet")
        od.set_other_odds(odds[i*10+3], odds[i*10+4], odds[i*10+5])
        for ev in events:
            if ev == event:
                ev.add_odds(od)
                ev.set_time(times[i])

        event.add_odds(od)
        events3.append(event)
    #driver.get("https://www.parimatch.com/en/sport/futbol/anglija-premer-liga")
        
    # driver.get("https://www.fonbet.com/bets/?locale=en#11918")
    # event3 = driver.find_elements_by_class_name('eventNumber')
    # teams = []
    
    driver.get("http://olimp.com/betting/index.php?page=line&action=2&sel[]=11664") # Olimp
    elem_teams = driver.find_elements_by_class_name("m")
    elem_odds = driver.find_elements_by_class_name("bet_sel") 
    
    odds = []
    teams = []
    
    events4 = []

    for team in elem_teams:
        data = team.text.split(" - ")
        if len(data) == 2:
            team1, team2 = team.text.split(" - ", 2)

        teams.append(t(team1))
        teams.append(t(team2))  
    for el in elem_odds: 
        odds.append(el.text)


    for i in range(12):
        event = Ev(teams[i*2], teams[i*2+1])
        od = Od(odds[i*10], odds[i*10+2], odds[i*10+1], "Olimp")
        od.set_other_odds(odds[i*10+3], odds[i*10+4], odds[i*10+5])
        for ev in events:
            if ev == event:
                ev.add_odds(od)
                ev.set_max()
                ev.set_time(times[i])
            request.session[ev.team1 + '-' + ev.team2] = ev

        event.add_odds(od)
        
        events4.append(event)


    context = {
        'site_title': 'Odds aggregator',
        'odds': odds,
        'teams': teams,
        'events': events,
        'events2': events2,
        'events3': events3,
        'events4': events4,
        'times': times,
        # 'event3': len(event3),
        # 'dates': dates,
        # 'test': test,
        }
    return render(request, "main/index.html", context,)



def check(request, team1, team2):
    event = request.session[team1 + '-' + team2]#ev.team1 + '-' + ev.team2]
    context = {
        'site_title': 'Odds aggregator',
        'event': event,
        }
    return render(request, "main/check.html", context,)







def index2(request):
    #r = urllib.urlopen('https://sports.bwin.com/en/sports#sportId=4').read()
    #soup = BeautifulSoup(r, 'html.parser')
    driver = webdriver.PhantomJS()
    #driver.get("https://sports.bwin.com/en/sports#sportId=4")
    driver.get("https://sports.bwin.com/en/sports#leagueIds=46&sportId=4") # Premier Liga BWin
    #driver.get("https://sports.bwin.com/en/sports#leagueIds=16108&sportId=4")  # La Liga
    
    #elems = WebDriverWait(driver, 10).until(find)
    
#   with self.wait_for_page_load(timeout=10):

    
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
