# importing libraries
import requests
from uagents import Agent, Context

# code to remove after getting key--------------------------------------
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv('sample.env'))
#-----------------------------------------------------------------------

# api key & base url declaration 
api_key = os.getenv("API_KEY")       # api_key = 'your_api_key' (the key must be inside quotes)
base_url = os.getenv("BASE_URL")     # base_url = 'your_api_url' (the url must be inside quotes)

# taking input from the user, the city user wants to monitor
city = input("Enter the city name: ")

# taking input for minimum and maximum temperature for the city
min_temp = float(input("Enter the minimum temperature (in Celsius): "))
max_temp = float(input("Enter the maximum temperature (in Celsius): "))

# create the API request url with the city and API key
url = base_url + f'q={city}&APPID={api_key}'

# creating an agent
temp_agent = Agent(name = "temp_agent", seed = "city temperature")

# function which will run wih a period of 10 sec
@temp_agent.on_interval(period=10.0)
async def temperature(ctx: Context):
    
    # send an HTTP GET request to the OpenWeatherMap API
    response = requests.get(url)

    # check if the request was successful
    if response.status_code == 200:
        
        # parse the JSON response
        data = response.json()

        # extract and display the temperature in celsius
        temp_kelvin = data['main']['temp']
        # convert to celsius
        temp_celsius = temp_kelvin - 273.15  

        # check if the temperature is outside the specified range
        # red text color for exceeding the range and green text color for within range temperature
        if temp_celsius < min_temp:
            ctx.logger.info(f"Current Temperature in {city}: {temp_celsius:.2f}°C")
            ctx.logger.warning("\33[{color}m".format(color=31) + f"Alert: Temperature is below the minimum of {min_temp}°C.")
        elif temp_celsius > max_temp:
            ctx.logger.info(f"Current Temperature in {city}: {temp_celsius:.2f}°C")
            ctx.logger.warning("\33[{color}m".format(color=31) + f"Alert: Temperature is above the maximum of {max_temp}°C.")
        else:
            ctx.logger.info(f"Current Temperature in {city}: {temp_celsius:.2f}°C")
            ctx.logger.info("\33[{color}m".format(color=32) + f"Temperature is within the range between {min_temp}°C and {max_temp}°C.")
    
    # if request gets failed
    else:
        ctx.logger.warning("Failed to retrieve weather data. Status code:", response.status_code)

# run the agent
if __name__ == "__main__":
    temp_agent.run()