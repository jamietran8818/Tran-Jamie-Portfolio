# PythonWeatherApp
Final project for my intro to Python course is a interactive Weather App using Python that pulls real time data from an API.

## Installation:
-Using the latest version of PyCharm CE you will need to import requests

-Obtain an API key from OpenWeatherMap to access the information

-Use the following link to obtain the url data to incorporate into your code 'https://openweathermap.org/api'

-This specfic program utilizes the 'Current Weather Data' API document


## Loading Data:
-Assign the beginning url and api key to two separate variables 

-Example:
      
      zip_url = "https://api.openweathermap.org/data/2.5/weather?q="
          key_api = 'c8541d95699838c63c2443eca4e5dae9'

## Code:
-Create two functions one for looking up the weather by zip code and the other looking up the weather by city and state

-Both of these functions will be relatively the same aside from the zip and city specific code

-This code is built within a try and except function to exit the program if the zip code or city was not found

-The first try and except function asks the user for input on the zip code they want to check the weather for, if the zip code exists in the api then if will move on to the next try and except function. If the zip code doesn't exist the program will exit.

-Print statements are added to provide context to the user on how to fix the issue

-Example:
          
          try:
              postal = int(input('Type in your zip code: '))
          except ValueError:
              print('You need to enter a numerical value.')
              print('Program exited.')
              exit()

-The next try and except function plugs the user's zip code into the url to complete the the url

-This will look like the following with print statements embedded to give the user context on what is going on

-Example:
            
            check_zipurl = zip_url + str(postal) + '&appid=' + key_api
            zip_weather = requests.get(check_zipurl)
            check_readable_zip = zip_weather.json()
            print('------------------------------------------------')
            print('Checking weather for ' + check_readable_zip['name'] + '.')
            print('------------------------------------------------')

-Next we will insert a input statement asking for the measurement they would like the temperature displayed in

-A series of if statements will then be used to ensure the right measurement is used

-Example: 
            
            measurement = input('Would you like the temperature displayed in Fahrenheit or Celsius? ')
            case_measurement = str(measurement.casefold())
            if case_measurement == 'fahrenheit':
                  final_measurement = 'imperial'
            elif case_measurement == 'f':
                  final_measurement = 'imperial'
            elif case_measurement == 'celsius':
                  final_measurement = 'metric'
            elif case_measurement == 'c':
                  final_measurement = 'metric'
            else:
                  print('You need to choose between fahrenheit and celsius.')
                  print('Program exited.')
                  exit()

-The final url will be strung together and requests will be used to find the information

-We will also end the except function with a KeyError to let the user no if the city could not be found

-Example:
            
            finished_zipurl = zip_url + str(postal) + '&appid=' + key_api + '&units=' + final_measurement
            zip_weather = requests.get(finished_zipurl)
            readable = zip_weather.json()
      except KeyError:
            print('City not found.')
            print('Program exited.')
            exit()

-To wrap up this function a series of print statements will be listed to display the weather data nicely from the json script

-Example:
            
            print('------------------------------------------------')
            print("Today's Forecast for:  ", readable['name'])
            print('{:24}{:24}'.format('Category:', 'Answer:'))
            print('------------------------------------------------')
            print('{:15}{:15}'.format('Feels like:', readable['main']['feels_like']))
            print('{:15}{:15}'.format('Current temp:', readable['main']['temp']))
            print('{:15}{:15}'.format('High temp:', readable['main']['temp_max']))
            print('{:15}{:15}'.format('Low temp:', readable['main']['temp_min']))
            print('{:15}{:15}'.format('Pressure:', readable['main']['pressure']))
            print('{:15}{:15}'.format('Humidity:', readable['main']['humidity']))
            print('{:15}{:15}'.format('Clouds:', readable['weather'][0]['description']))

-After the zip code function is created you will create another functiion for the city lookup

-Lastly the main function where these functions we be used is created just to obtain the information from the user

-This will be made up of print, input, and if statements

-Example:
            
            print('Hello there!')
            print('Welcome to OpenWeatherMap!')
            begin = input("Type 'begin' to get started or 'quit' to exit: ")
            begin_final = str(begin.casefold())

            while begin_final == 'begin':
                  zip_city = input('Would you like to look up the weather with your zip code or city name? ')
                  zip_city_final = str(zip_city.casefold())
                  if zip_city_final == 'zip code':
                        zip_lookup()
                  elif zip_city_final == 'zip':
                        zip_lookup()
                  elif zip_city_final == 'city name':
                        city_lookup()
                  elif zip_city_final == 'city':
                        city_lookup()
                  elif begin_final == 'quit':
                        print('Program exited.')
                        exit()
                  else:
                        print('You need to select zip code or city name.')
                        print('------------------------------------------------')
                        pass
                  begin = input("Type 'begin' to search another location or 'quit' to exit: ")
                  begin_final = str(begin.casefold())

            print('Program exited.')
