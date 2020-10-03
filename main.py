import requests
from bs4 import BeautifulSoup
import geocoder

#Get Location
usrLoc = input("Where are you right now? ")
g = geocoder.google('Mountain View, CA')

lat = g.lat
lon = g.lng


print (g.latlng)

print (str(lon) + "\n\n\n")




#weather data NO APIs!!!!
page = requests.get("http://forecast.weather.gov/MapClick.php?lat=33.138230&lon=-96.882751")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
#print(tonight.prettify())

#breaking down HTML into chunks of valuable information
timePeriod = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
lowTemp = tonight.find(class_="temp").get_text()
print(timePeriod)
print(short_desc)
print(lowTemp)

print ("\n\n")

#More detailed info can be found in the img title
img = tonight.find("img")
desc = img['title']
print(desc)