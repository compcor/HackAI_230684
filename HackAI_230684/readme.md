**Project name : Real time monitoring of temperature of a city**

**Description :**

This project let's the user choose a city, which one wants to monitor. Then the user will set the minimum and maximum temperature, and if temperature of the user selected city goes beyond this range, a visual alert will be generated, with red text color for warning or alert and green text color if temperature remains within range. The agent will run with a period of 10 seconds so that there is enough time for temperature to change as well for optimal result to be used in scientific research or personal usage.

**Instructions to run the program :**

Note - Internet connectivity is required

Step 1 - Clone the repository or Download zip file in a folder

Step 2 - Change the api

Step 3 - Run the main.py file

**Detailed Configuration :**

Step 1 - Free Sign up for OpenWeather and you will recieve api key in your email. link - https://home.openweathermap.org/users/sign_up  

Step 2 - After getting api, replace the api_key and base_url with your key and url in the main.py file inside src folder 
         Note - for base_url, copy the url from point mentioned in the email as 'Example of API call:' only till '....weather?'

Step 3 - Remove or comment the code block which used .env file (commented in the main.py)

Step 4 - In terminal, inside src folder run the following commands (Python should be installed)

            poetry init -n
            poetry shell (You should be inside virtual enviornment)
            poetry install
            pip install uagents
            python3 main.py (api key and base url should be replaced with yours to be executed in your computer)

Step 5 - Enter the city and temperature (give less difference value) so that all three cases ie below, above and within range temperature can be observed

            example input can be like this -
            City : London
            if current temperature is around 16.39° then
            Minimum temperature : 16.38°
            Maximum temperature : 16.40°
            
**Result :** Red color alert if temperature goes beyond the specified range and green color alert if temperature remains within range.            
    


