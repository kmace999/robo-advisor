# robo-advisor
Navigate to the robo-advisor repository from your local GitHub Desktop client in the command line [ex: Git Bash, Command Prompt, etc.] after cloning it from [this remote GitHub repo](https://github.com/kmace999/robo-advisor). The below code is an example, so make sure it reflects your depository's unique address.

`cd ~/Desktop/GitHub/robo-advisor`

## Setting up the advisor environment
The first time you use the robo advisor (and only the first time), you need to create a new environment and name it something like "robo-env".

`conda create -n stocks-env python=3.8`

This code will also install Python 3.8 into this new environment. To navigate to this environment or return to it in the future, use the below code.

`conda activate stocks-env`

When activating the environment for the first time, you have to install the required packages listed in the requirements.txt file in the repository. (You only need to do this the first time you setup this environment.)

`pip install -r requirements.txt`

## Customizing your secure API key

Create a new file called ".env"

`> .env`

The required package for this advisor python-dotenv allows the user to enter their API key that will allow the advisor to issue requests to the AlphaVantage API. User security is a priority, and this sensitive key will only be used to access the user requested information, and it will not be displayed in the advisor outputs. To change enter an API key, open the new .env file in your text editor (example below),

atom .env

and enter your chosen username.

`ALPHAVANTAGE_API_KEY = "abc123"`

## Running the robo advisor program
To run the robo advisor program, run the below code, and follow the in-program instructions.

`python robo_advisor.py`

### Tips for running the robo advisor program
- Make sure the symbol for the chosen stock/cryptocurrency is accurate and exists
- Use the exact prompted responses to in-program questions (e.g. "Do you wish to receive advice on another stock or cryptocurrency? ['yes'/'no']:" = yes OR no NOT another symbol)
- Data used in the recommendation algorithm can be accessed in the app/data/prices.csv file after the program is run for one symbol

## Happy investing!

# Files included
- README.md
- requirements.txt
- app (robo_advisor.py, data (.gitignore))
- gitignore
