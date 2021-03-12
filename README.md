# robo-advisor
Navigate to the robo-advisor repository from your local GitHub Desktop client in the command line [ex: Git Bash, Command Prompt, etc.]. The below code is an example, so make sure it reflects your depository's unique address.
`cd ~/Desktop/GitHub/robo-advisor`

##Setting up the advisor environment
The first time you use the robo advisor (and only the first time), you need to create a new environment and name it something like "robo-env".

`conda create -n robo-env python=3.8`

This code will also install Python 3.8 into this new environment. To navigate to this environment or return to it in the future, use the below code.

`conda activate robo-env`

When activating the environment for the first time, you have to install the required packages listed in the requirements.txt file in the repository. (You only need to do this the first time you setup this environment.)

`pip install -r requirements.txt`

## Customizing your API key or something

Create a new file called ".env"

`> .env`

The required package for this game python-dotenv allows the user to enter a secret username that is displayed in the game but not visible when looking through the root depository. To change your username, open the new .env file in your text editor (example below),

atom .env

and enter your chosen username.

ALPHAVANTAGE_API_KEY


ENV USERNAME BEFORE RUNNING THE THING









# rock-paper-scissors-exercise
Navigate to the rock-paper-scissors-exercise repository from your local Git Hub
Desktop client in the command line [ex: Git Bash, Command Prompt, etc.]. The below code
is an example, so make sure it reflects your depository's unique address.

`cd ~/Documents/GitHub/rock-paper-scissors-exercise`

## Setting up the game environment
The first time you play this game (and only the first time), you need to create
a new environment, and name it something like "my-game-env".

`conda create -n my-game-env python=3.8`

This code will also install Python 3.8 into this new environment.
To navigate to this environment or return to it in the future, use the below code.

`conda activate my-game-env`


When activating the environment for the first time, you have to install the
required packages listed in the requirements.txt file in the repository. (You only
need to do this the first time you setup this environment.)

`pip install -r requirements.txt`


## Playing Rock, Paper, Scissors
To play the game, run the below code, and follow the in-game instructions. Have fun!

`python game.py`


## Customizing your username
Create a new file called ".env"

`> .env`


The required package for this game python-dotenv allows the user to
enter a secret username that is displayed in the game but not visible when
looking through the root depository.
To change your username, open the new .env file in your text editor (example below),

`atom .env`

and enter your chosen username.

`USER_NAME = "Remy Ratatouille"`


# Files included
- README.md
- requirements.txt
- game.py
- gitignore
