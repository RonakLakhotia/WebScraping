from selenium import webdriver
from bs4 import BeautifulSoup

class Player():

	#attributes for each player
	  name = ""
	  link = ""
	  Height = ""
	  Weight = ""
	  DateOfBirth = ""


def getPlayerList():

	driver = webdriver.PhantomJS(executable_path = '/Users/ronaklakhotia/Desktop/phantomjs')
	url = 'https://stats.nba.com/players/list/?ls=iref:nba:gnav'

	#download HTML page
	driver.get(url)

	#create soup
	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_ = 'columns / small-12 / section-view-overlay')


getPlayerList()	

	