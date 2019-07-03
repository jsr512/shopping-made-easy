# shopping-made-easy

Chooses randomly from a list of favorite recipes and generates organized shopping list that is then sent via email to the user

## Prerequisites

Anaconda 3.7
Python 3.7
Pip

## Installation and Setup

Fork the repo from: https://github.com/jsr512/shopping-made-easy

Create a local repository with the name easy-shopping then navigate to this using the command line:

    ''
    cd ~/Desktop/easy-shopping
    ''

Create and activate a new virtual environment:

    ''
    conda create n- easy-shopping-env python=3.7
    conda activate easy-shopping-env
    ''

Within the virtual environment, install the necessary packages for the program to run:

    ''
    pip install sendgrid==6.0.5
    pip install os
    pip install python-dotenv
    ''

Create a sengrid account through the sendgrid website and link the email that you would like to send emails from by following the instructions provided by sendgrid. Secure the given API Key for usage within this program.

Create .env files in order to securly contain data for both sender and recipient email if you wish for this information to be hidden. Also create a .env file SENDGRID_API_KEY placing within it the API key obtained through account set up.

Add all .env files created to a .gitignore file

## Data Customization (optional)

The program is configured with recipes hardcoded. Should you wish to customize the recipe list please use the following formatting to ensure the program runs successfully. All data entered should be in string format.

    ''
    recipe_catagory = [
            {"name": ""example recipe name",
            "website": "example recipe website",
            "ingredients": {"meat": ["example"], "produce": ["example"], "dairy": ["example"], "spices": ["example"], "other": ["example"]}} 
    ]   
    ''

## Running the Program

Once installation and setup is complete initiate the program using the following command:

    ''
    python easy_shopping.py
    ''

Once initiated, follow the prompts on screen. The program will ask to input the number of desired meal by catagory, in the default case by protein. Once data is enter for one of each [chicken, beef, fish, pork, other] the program will randomly select a recipe from the coded list and provide the user with an output of recipe name, recipe website, follwed by a shopping list organized by each of the following store departments [produce, meat, dairy, spices, other]. Finally an email will be sent to the configured address containing the information output for easy on the go reference.
