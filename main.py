import os
clear = lambda: os.system('clear')

import art
from art import *

import time
from time import sleep

import requests
from bs4 import BeautifulSoup

import geopy
from geopy.geocoders import Nominatim

###################################################

Art = text2art("ES Weather")
print(Art, "\n")

def getWeatherNow():
  #Get Location
  usrLoc = input("Enter location to check: ")
  geolocator = Nominatim(user_agent="ES_Weather-Machine")
  location = geolocator.geocode(usrLoc)
  lat = location.latitude
  lon = location.longitude

  print ("lat: ", lat, "\nlon: ", lon, "\n", "\nAccessing federal weather data...", "\n\n\n")
  time.sleep(2)


  #weather data NO APIs!!!!
  requestURLwithLatLon = ("http://forecast.weather.gov/MapClick.php?lat="+str(lat)+"&lon="+str(lon))
  page = requests.get(requestURLwithLatLon)
  soup = BeautifulSoup(page.content, 'html.parser')
  seven_day = soup.find(id="seven-day-forecast")
  forecast_items = seven_day.find_all(class_="tombstone-container")
  tonight = forecast_items[0]
  #print(tonight.prettify())


  print ("BRIEF WEATHER:")
  #breaking down HTML into chunks of valuable information
  timePeriod = tonight.find(class_="period-name").get_text()
  short_desc = tonight.find(class_="short-desc").get_text()
  lowTemp = tonight.find(class_="temp").get_text()
  print(timePeriod)
  print(short_desc)
  print(lowTemp)

  print ("\n")


  print ("DETAILED WEATHER:")
  #More detailed info can be found in the img title
  img = tonight.find("img")
  desc = img['title']
  print(desc)

  print ("\n\n\n")








#Program begins here
getWeatherNow()



repeat = input("Would you like to access another location? (y/n) ")
if repeat == "y":
  clear()
  time.sleep(2.5)
  getWeatherNow()
elif repeat == "n":
  print("Ok.")
else:
  print("Your input was not understood. Please refresh this page.")