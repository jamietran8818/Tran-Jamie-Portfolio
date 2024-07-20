#DSC 510
#Week 10
#Final Programming Assignment
#Jamie Tran
#7/26/2023

def city_lookup():
    import requests

    city_url = "https://api.openweathermap.org/data/2.5/weather?q="
    key_api = 'c8541d95699838c63c2443eca4e5dae9'

    try:
        print('------------------------------------------------')
        print('WARNINGS: No abbreviations allowed. Be sure to have a comma separating the city and state.')
        city = input('Type in your city and state in the following format (city, state): ')
        final_city = city.casefold()
        check_cityurl = city_url + str(final_city) + '&appid=' + key_api
        city_weather = requests.get(check_cityurl)
        check_readable = city_weather.json()
        print('------------------------------------------------')
        print('Checking weather for ' + check_readable['name'] + '.')
        print('------------------------------------------------')
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
        finished_cityurl = city_url + str(final_city) + '&appid=' + key_api + '&units=' + final_measurement
        city_weather = requests.get(finished_cityurl)
        readable = city_weather.json()
        print('------------------------------------------------')
        print("Today's Forecast for:  ", readable['name'])
        print('Temperatures displayed in: ' + case_measurement)
        print('{:24}{:24}'.format('Category:', 'Answer:'))
        print('------------------------------------------------')
        print('{:15}{:15}'.format('Feels like:', readable['main']['feels_like']))
        print('{:15}{:15}'.format('Current temp:', readable['main']['temp']))
        print('{:15}{:15}'.format('High temp:', readable['main']['temp_max']))
        print('{:15}{:15}'.format('Low temp:', readable['main']['temp_min']))
        print('{:15}{:15}'.format('Pressure:', readable['main']['pressure']))
        print('{:15}{:15}'.format('Humidity:', readable['main']['humidity']))
        print('{:15}{:15}'.format('Clouds:', readable['weather'][0]['description']))
    except KeyError:
        print('City not found.')
        print('You need to type your city and state in the following format (city, state).')
        print('REMEMBER: No abbreviations allowed. Make sure to have a comma separating the city and state.')
        print('------------------------------------------------')
        print('Program exited.')
        exit()


def zip_lookup():
    import requests

    zip_url = "https://api.openweathermap.org/data/2.5/weather?zip="
    key_api = 'c8541d95699838c63c2443eca4e5dae9'

    try:
        postal = int(input('Type in your zip code: '))
    except ValueError:
        print('You need to enter a numerical value.')
        print('Program exited.')
        exit()

    try:
        check_zipurl = zip_url + str(postal) + '&appid=' + key_api
        zip_weather = requests.get(check_zipurl)
        check_readable_zip = zip_weather.json()
        print('------------------------------------------------')
        print('Checking weather for ' + check_readable_zip['name'] + '.')
        print('------------------------------------------------')
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
        finished_zipurl = zip_url + str(postal) + '&appid=' + key_api + '&units=' + final_measurement
        zip_weather = requests.get(finished_zipurl)
        readable = zip_weather.json()
    except KeyError:
        print('City not found.')
        print('Program exited.')
        exit()

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


def main():
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


if __name__ == '__main__':
    main()


#Change#:1
#Changes Made: Created file and added two try and except functions for zip and city
#Date of Change: 7/26/2023
#Author: Jamie Tran
#Date to be submitted: 8/13/2023

#Change#:2
#Changes Made: Added if statements to the while statements for Celsius, Fahrenheit
#Date of Change: 7/26/2023
#Author: Jamie Tran
#Date to be submitted: 8/13/2023

#Change#:3
#Changes Made: Built out zip_lookup and city_lookup functions
#Date of Change: 8/7/2023
#Author: Jamie Tran
#Date to be submitted: 8/13/2023

#Change#:4
#Changes Made: Added additional url for Fahreinheit or Celsius
#Date of Change: 7/26/2023
#Author: Jamie Tran
#Date to be submitted: 8/13/2023
