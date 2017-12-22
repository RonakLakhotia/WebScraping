from selenium import webdriver
from bs4 import BeautifulSoup
import self
import os
import errno
import requests
import time

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

    	print("Height - " + Height)

    	Weight = ""
    	w_span = soup.find('div', string = 'WT')

    	for span in w_span.findNextSiblings():
    		Weight = Weight + span.text

    	print("Weight - " + Weight)

    	DateOfBirth = ""
    	b_span = soup.find('div', string = 'BORN')

    	for span in b_span.findNextSiblings():
    		DateOfBirth = DateOfBirth + span.text

    	print("Date of Birth - " + DateOfBirth)	
    	print()
    	
    driver.quit()
    	
def mkdir_path(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def getPlayersImage(playerList):

	driver = webdriver.PhantomJS(executable_path = '/Users/ronaklakhotia/Desktop/phantomjs')

	for player in playerList[1:2]:

		playerUrl = 'https://stats.nba.com' + player.link
		driver.get(playerUrl)

		time.sleep(2)
		
		soup = BeautifulSoup(driver.page_source, 'lxml')

		div = soup.find('div', class_ = 'player-summary__image-block')
		img = div.find('img')
		print(img['src'])

		imageFile = open('/Users/ronaklakhotia/Desktop/WebScraping/NBA/Images/{0}.jpg'.format(player.name), 'wb')
		imageFile.write(requests.get(img['src']).content)
		imageFile.close()


	driver.quit()
		
players = getPlayerList()
directoryNameToStoreImages = 'Images'
directoryPathOfFolder = '/Users/ronaklakhotia/Desktop/WebScraping/NBA'
os.chdir(directoryPathOfFolder)
mkdir_path(directoryNameToStoreImages)
getPlayersImage(players)
getPlayerDetails(players)	
getPlayersImage(players)
	