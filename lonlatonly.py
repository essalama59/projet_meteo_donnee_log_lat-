import requests
import smtplib
import urllib
import geopy
import json

api='47032cb2779badc8a8a41370b64beff1'
urlbase='http://api.openweathermap.org/data/2.5/weather?appid='+api

def get_weather(c):
    lati= c['latitude']
    longi= c['longitude']
    url=urlbase+'&lat='+lati+'&lon='+longi+'&units=metric'
    print(url)
    recup= requests.get(url).json()
    return(recup)

def get_location():
    geocode=[]
    lonlat=open('/Users/achrafessalama/Desktop/AGTECH/lonlatonly.txt', 'r')
    for line in lonlat:
        lat,lon=line.split(',') #slip pour séparer les vigule
        coord= {'longitude': lon.strip(),'latitude':lat} #strip pour supprimer les espaces
        geocode.append(coord)



    return geocode

coord=get_location()
w=get_weather(coord[0])
print(w)



