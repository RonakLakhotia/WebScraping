from selenium import webdriver
from bs4 import BeautifulSoup
import self

class Player():

	#attributes for each player
	  self.name = ""
	  self.link = ""
	  self.Height = ""
	  self.Weight = ""
	  self.DateOfBirth = ""


def getPlayerList():

	driver = webdriver.PhantomJS(executable_path = '/Users/ronaklakhotia/Desktop/phantomjs')
	url = 'https://stats.nba.com/players/list/?ls=iref:nba:gnav'

	#download HTML page
	driver.get(url)

	#create soup
	soup = BeautifulSoup(driver.page_source, 'lxml')
	div = soup.find('div', class_ = 'stats-player-list players-list')

	playerList = []

	for aTag in div.find_all('a'):
		print(aTag.text)

getPlayerList()	

	