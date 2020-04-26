
import json
import requests

#find user's longitude and latitude
res_ip = requests.get('http://ipinfo.io/')

loc_data = res_ip.json()
location = loc_data['loc'].split(",")

api_key= "067e773acbe43ac693677db3d85dc144"
lat = location[0]
long = location[1]

#url 
url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat,long,api_key)


c_or_f = (input("Would you like your temperature in celcius or farenheit?").strip()).lower()
 
#complete_url = base_url + "appid=" + api_key + "&q=" + city
#response object
response = requests.get(url) 

#json format data converted into python format (dictionary)
data_conv = response.json() 

#check to find city name, if 404, city not found
if  c_or_f == "c" or  c_or_f== "celcius" or c_or_f== "f" or  c_or_f =="farenheit":
   

   if data_conv["cod"] != "404": 
       print("Current Weather: ")
        #save weather data
       weather_data = data_conv["main"] 
  
       # current temperature
    
       current_temperature = weather_data["temp"] #in kelvin
       if c_or_f == "c" or c_or_f=="celcius":
           current_temperature = round(current_temperature-273.15,2)
       elif c_or_f=="f" or c_or_f=="farenheit":
           current_temperature = round(current_temperature*(9/5)-459.67,2)

       #temperature in celcius 
 
       # current pressure
       current_pressure = weather_data["pressure"] 
  
       # current humidity
       current_humidiy = weather_data["humidity"]

       #prints current weather if city found, if not, prints message

       print(" Temperature  = " +
                    str(current_temperature) + " "+ c_or_f +
          "\n atmospheric pressure  = " +
                    str(current_pressure) + " hPa" + 
          "\n humidity = " +
                    str(current_humidiy) + "%"
         ) 
  
   else: 
        print(" City Not Found ")
else:
    print("Invalid entry")

