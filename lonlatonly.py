import requests
import config
import smopy
import matplotlib.pyplot as plt


urlbase='http://api.openweathermap.org/data/2.5/weather?appid='+config.api

def get_weather(c):
    lati= c['lat']
    longi= c['lon']
    url=urlbase+'&lat='+lati+'&lon='+longi+'&units=metric'
    print(url)
    recup= requests.get(url).json()
    return(recup)

def get_map(coords):
    map = smopy.Map( (coords['lat_min'],coords['lon_min'],coords['lat_max'],coords['lon_max']) , z=8)
    ax = map.show_mpl(figsize=(8,8))
    plt.show()
    return True

def get_locations():
    geocode=[]
    lonlat=open('lonlatonly.txt', 'r')
    for line in lonlat:
        lat,lon=line.split(',') #slip pour séparer les vigule
        coord= {'lon': lon.strip(),'lat':lat} #strip pour supprimer les espaces
        geocode.append(coord)

    return geocode

def get_area(locations):
    # get area boundaries.
    # initialising min/max with first record #0
    lat_min=lat_max=float(locations[0]['lat'])
    lon_min=lon_max=float(locations[0]['lon'])
    # let's check each record :
    for location in locations :
        lat_min=min(lat_min,float(location['lat']))
        lat_max=max(lat_max,float(location['lat']))
        lon_min=min(lon_min,float(location['lon']))
        lon_max=max(lon_max,float(location['lon']))
    # adding some border  (10%):
    o_lat = ((lat_max - lat_min)/100)*10
    o_lon = ((lon_max - lon_min)/100)*10
    lat_min=lat_min-o_lat
    lat_max=lat_max+o_lat
    lon_min=lon_min-o_lat
    lon_max=lon_max+o_lat

    # finally , return directly a list
    return {'lat_min':lat_min, 'lat_max':lat_max, 'lon_min':lon_min,'lon_max':lon_max}



def main():
    #1 - get locations from file :
    locations = get_locations('lonlat.txt')


    #2 - add weather for each point :
    for location in locations :
        location = get_weather(location)


    #3 display locaQtions (print) :
    nbligne=0
    for location in locations :
        nbligne=nbligne+1
        sep = "LIGNE %d"  % nbligne
        print_dict(location,sep)


    #4 - get area boundary  :
    area = get_area(locations)
    print_dict(area,"AREA")

    #4 - get the map (according to boundaries)
    map = get_map(area)

    # NOW, we have all the data we need, no more API Request !




if __name__ == "__main__":
    main()


