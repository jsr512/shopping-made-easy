import random

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

## Input Capture
valid_entries = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

while True:
    chicken_total = input("Enter the number of chicken meals desired: ")
    if chicken_total in valid_entries:     #prevents generation of large number of recipes
        pass
    else:
        print("Invalid entry please enter a number between 0 and 9 inclusive") #ensures entry is a numeric value 
        next
    
    beef_total = input("Enter the number of beef meals desired: ")
    if beef_total in valid_entries:     #prevents generation of large number of recipes
        pass
    else:
        print("Invalid entry please enter a number between 0 and 9 inclusive") #ensures entry is a numeric value 
        next

    fish_total = input("Enter the number of fish meals desired: ")
    if fish_total in valid_entries:     #prevents generation of large number of recipes
        pass
    else:
        print("Invalid entry please enter a number between 0 and 9 inclusive") #ensures entry is a numeric value 
        next
    
    pork_total = input("Enter the number of pork meals desired: ")
    if pork_total in valid_entries:     #prevents generation of large number of recipes
        pass
    else:
        print("Invalid entry please enter a number between 0 and 9 inclusive") #ensures entry is a numeric value 
        next

    other_total = input("Enter the number of other meals desired: ")
    if other_total in valid_entries:     #prevents generation of large number of recipes
        break
    else:
        print("Invalid entry please enter a number between 0 and 9 inclusive") #ensures entry is a numeric value 
        next

print(chicken_total)
print(beef_total)
print(fish_total)
print(pork_total)
print(other_total)

## Recipe Data

chicken = [
        {"name": "Beer Can Chicken",
        "website": "https://www.foodnetwork.com/recipes/patrick-and-gina-neely/pats-beer-can-grilled-chicken-recipe-1945080",
        "ingredients": {"meat": ["4-lb whole chicken"], "other": ["1 12 ounce beer"]}}
]

beef = [
        {"name": "Slow Cooker Korean Beef",
        "website": "https://www.ihearteating.com/slow-cooker-korean-beef/",
        "ingredients": {"meat": ["4-lb boneless beef chuck roast"], "other": ["1 cup beef broth", "1/2 cup soy sauce", "1/3 cup brown sugar", "2 T sesame Oil", "2 T rice vinegar", "2 T gochujang"], "spices": ["5 cloves garlic", "1/2 tsp onion powder"], "produce": ["2 T ginger"]}},
        
        {"name": "Cheeseburger Casserole",
        "website": "https://lowcarbyum.com/bacon-cheeseburger-casserole/",
        "ingredients": {"meat": ["2-lbs ground beef", "1-lb bacon"], "dairy": ["8 eggs", "1 cup heavy cream", "12 ounces grated cheddar"], "spices": ["2 cloves garlic", "1/2 tsp onion powder"], "other": ["1 can tomato paste"]}}
]

fish = [
        {"name": "Baked Lemon Haddock",
        "website": "https://www.tasteofhome.com/recipes/baked-lemon-haddock/",
        "ingredients": {"meat": ["2-lb haddock"], "other": ["1 cup bread crumbs"], "dairy": ["1/4 cup butter"], "spices": ["2 T parsley", "1/2 tsp garlic powder"], "produce": ["2 T Lemon Zest"]}}
]

## Compiling Shopping List

chicken_meal_list = random.sample(chicken, k=int(chicken_total)) 
beef_meal_list = random.sample(beef, k=int(beef_total)) 
fish_meal_list = random.sample(fish, k=int(fish_total)) 
#pork_meal_list = random.sample(pork, k=int(pork_total)) 
#other_meal_list = random.sample(other, k=int(other_total)) #need to input samples in order to uncomment 

shopping_list = []

for meal in chicken_meal_list:
        print(meal["name"])
        print(meal["website"])
        ingredients = (meal["ingredients"])
        shopping_list.append(ingredients)

for meal in beef_meal_list:
        print(meal["name"])
        print(meal["website"])
        ingredients = (meal["ingredients"])
        shopping_list.append(ingredients)

for meal in fish_meal_list:
        print(meal["name"])
        print(meal["website"])
        ingredients = (meal["ingredients"])
        shopping_list.append(ingredients)

#for meal in pork_meal_list:
#        print(meal["name"])
#        print(meal["website"])
#        ingredients = (meal["ingredients"])
#        shopping_list.append(ingredients)

#for meal in other_meal_list:
#        print(meal["name"])    
#        print(meal["website"])
#        ingredients = (meal["ingredients"])
#        shopping_list.append(ingredients)               ### TODO build out iterations

print(shopping_list)

all_meat = []
all_produce = []
all_dairy = []
all_spices = []
all_other = [] 

for stuff in shopping_list:
    meat_by_meal = (stuff["meat"])
    all_meat = all_meat + (meat_by_meal)    #compiles list of all meat ingredients into one list



print(all_meat)


### EMAILING List
#
#message = Mail(
#    from_email=(os.environ.get("MY_EMAIL_ADDRESS")),
#    to_emails=(os.environ.get("KATIE_EMAIL_ADDRESS")),
#    subject='Shopping List',
#    html_content='test' )  #TODO
#
#try:
#    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#    response = sg.send(message)
#    print(response.status_code)
#    print(response.body)
#    print(response.headers)
#
#except Exception as e:
#    print("Oops! Looks like the email didn't go through.")
#

