from django.shortcuts import render
from main import models
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

def index(request):
	#r = urllib.urlopen('https://sports.bwin.com/en/sports#sportId=4').read()
	#soup = BeautifulSoup(r, 'html.parser')
	driver = webdriver.PhantomJS()
	#driver.get("https://sports.bwin.com/en/sports#sportId=4")
	driver.get("https://sports.bwin.com/en/sports#leagueIds=46&sportId=4")
	#elems = WebDriverWait(driver, 10).until(find)
	
#	with self.wait_for_page_load(timeout=10):


	teams = driver.find_elements_by_class_name("mb-option-button__option-name--odds-4")
	elems = driver.find_elements_by_class_name("mb-option-button__option-odds")
	# except StaleElementReferenceException: driver.implicitly_wait(10)
	
	odds = []
	ts = []
	for el in elems: 
		odds.append(el.text)
	for team in teams:
		ts.append(team.text)
	context = {
		#'soup': soup.find_all('form'),
		'site_title': 'Odds aggregator',
		'odds': odds,
		'teams': ts,
		}
	return render(request, "main/index.html", context,)
