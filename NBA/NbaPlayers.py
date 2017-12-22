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
		newPlayer = Player()
		newPlayer.name = aTag.text
		newPlayer.link = aTag['href']
		playerList.append(newPlayer)

	driver.quit()
	return playerList


def getPlayerDetails(playerList):

	driver = webdriver.PhantomJS(executable_path = '/Users/ronaklakhotia/Desktop/phantomjs')

	for player in playerList[1:3]:

		playerUrl = 'https://stats.nba.com' + player.link
		driver.get(playerUrl)
		soup = BeautifulSoup(driver.page_source, 'lxml')

		Height = ""
		h_span = soup.find('div', string = 'HT')

		for span in h_span.findNextSiblings():
    		Height = Height + span.text

    	print(Height)


players = getPlayerList()
getPlayerDetails(players)	

	