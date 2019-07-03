import random

import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

## Input Capture
valid_entries = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

while True:
    chicken_total = input("Enter the number of chicken meals desired: ")
    if chicken_total in valid_entries:     #prevents generation of large number of recipes
        pass
    else:
        print("Invalid entry please enter a number between 0 and 9 inclusive") #ensures entry is a numeric value 
        continue
    
    beef_total = input("Enter the number of beef meals desired: ")
    if beef_total in valid_entries:     #prevents generation of large number of recipes
        pass
    else:
        print("Invalid entry please enter a number between 0 and 9 inclusive") #ensures entry is a numeric value 
        continue

    fish_total = input("Enter the number of fish meals desired: ")
    if fish_total in valid_entries:     #prevents generation of large number of recipes
        pass
    else:
        print("Invalid entry please enter a number between 0 and 9 inclusive") #ensures entry is a numeric value 
        continue
    
    pork_total = input("Enter the number of pork meals desired: ")
    if pork_total in valid_entries:     #prevents generation of large number of recipes
        pass
    else:
        print("Invalid entry please enter a number between 0 and 9 inclusive") #ensures entry is a numeric value 
        continue

    other_total = input("Enter the number of other meals desired: ")
    if other_total in valid_entries:     #prevents generation of large number of recipes
        break
    else:
        print("Invalid entry please enter a number between 0 and 9 inclusive") #ensures entry is a numeric value 
        continue

## Recipe Data  #must contain meat/produce/dairy/spices/other lists within ingrediants to iterate through with for loop below even if empty. Sample template available in README

chicken = [
        {"name": "Beer Can Chicken",
        "website": "https://www.foodnetwork.com/recipes/patrick-and-gina-neely/pats-beer-can-grilled-chicken-recipe-1945080",
        "ingredients": {"meat": ["4-lb whole chicken"], "produce": [], "dairy": [], "spices": [], "other": ["1 12 ounce beer"]}},

        {"name": "Baked Chicken Parm",
        "website": "https://www.skinnytaste.com/baked-chicken-parmesan/",
        "ingredients": {"meat": ["4 8oz chciken breasts"], "produce": [], "dairy": ["1/4 cup grated parmesan", "2 tablespoons butter", "3/4 cup mozzarella"], "spices": [], "other": ["1 cup marinara", "3/4 cup breadcrumbs"]}},

        {"name": "Grilled Chicken Paillard",
        "website": "https://www.rachaelrayshow.com/recipes/21362_katie_lee_grilled_chicken_paillard_with_arugula_and_shaved_pecorino",
        "ingredients": {"meat": ["4 boneless chicken breast halves"], "produce": ["grated zest and juice of 1/2 lemon", "8 cups arugula"], "dairy": ["shaved pecorino romano cheese"], "spices": ["1/4 tsp garilic powder", "1/2 tsp grainy mustard"], "other": []}}
]

beef = [
        {"name": "Slow Cooker Korean Beef",
        "website": "https://www.ihearteating.com/slow-cooker-korean-beef/",
        "ingredients": {"meat": ["4-lb boneless beef chuck roast"], "produce": ["2 T ginger"], "dairy": [], "spices": ["5 cloves garlic", "1/2 tsp onion powder"], "other": ["1 cup beef broth", "1/2 cup soy sauce", "1/3 cup brown sugar", "2 T sesame Oil", "2 T rice vinegar", "2 T gochujang"]}},
        
        {"name": "Cheeseburger Casserole",
        "website": "https://lowcarbyum.com/bacon-cheeseburger-casserole/",
        "ingredients": {"meat": ["2-lbs ground beef", "1-lb bacon"], "produce": [], "dairy": ["8 eggs", "1 cup heavy cream", "12 ounces grated cheddar"], "spices": ["2 cloves garlic", "1/2 tsp onion powder"], "other": ["1 can tomato paste"]}},

        {"name": "Grilled Steak",
        "website": "no website",
        "ingredients": {"meat": ["steak cut of choice"], "produce": [], "dairy": [], "spices": [], "other": []}},

        {"name": "Slow Cooker Broccoli Beef",
        "website": "https://www.lecremedelacrumb.com/slow-cooker-broccoli-beef/",
        "ingredients": {"meat": ["1.5-lbs flank steak"], "produce": ["4 cups broccoli"], "dairy": [], "spices": ["1 T garlic", "1/4 tsp red chili flakes"], "other": ["1 cup beef broth", "2/3 cup soy sauce", "1/3 cup brown sugar", "1 T sesame oil", "2 T corn starch"]}}
]

fish = [
        {"name": "Baked Lemon Haddock",
        "website": "https://www.tasteofhome.com/recipes/baked-lemon-haddock/",
        "ingredients": {"meat": ["2-lb haddock"], "produce": ["2 T Lemon Zest"],"dairy": ["1/4 cup butter"], "spices": ["2 T parsley", "1/2 tsp garlic powder"], "other": ["1 cup bread crumbs"]}}
]

pork = [
        {"name": "Slow Cooker Sausage and Peppers",
        "website": "https://vanillaandbean.com/lemon-garlic-orzo-with-roasted-vegetables/",
        "ingredients": {"meat": ["8 italian sausage links"], "produce": ["1 large geen bell pepper", "1 large yellow onion"], "dairy": [], "spices": ["1 tsp fennel seeds", "1/2 tsp oregano", "1/2 tsp basil", "1/2 tsp garlic powder", "1/4 tsp red pepper"], "other": ["28 oz can crushed tomatos", "1/4 cup marsala wine or chicken broth"]}}

]

other = [
        {"name": "Lemon Garlic Orzo with Roasted Vegtables",
        "website": "https://foodfolksandfun.net/sausage-peppers-slow-cooker-recipe/",
        "ingredients": {"meat": [], "produce": ["1 cup mushrooms", "1 cup peppers", "1-lb asparagus", "12 oz cherry tomatos", "1/2 cup shallots", "1 lemon"], "dairy": ["1/2 cup feta"], "spices": ["2 tsp garlic"], "other": ["1 cup orzo", "1.5 cup vegtable broth"]}},

         {"name": "Low Carb Carbonara",
        "website": "https://sweetcsdesigns.com/paleo-low-carb-carbonara/",
        "ingredients": {"meat": ["4 slices bacon"], "produce": ["3 zucchinis"], "dairy": ["1 T heavy cream", "2 eggs", "1/3 cup shredded parmesan"], "spices": ["3 cloves garlic"], "other": []}},

         {"name": "Zucchini Rice with Cranberries, Bacon, Goat Cheese, and Walnuts",
        "website": "https://inspiralized.com/zucchini-rice-with-cranberries-bacon-goat-cheese-and-walnuts-with-maple-dijon-dressing/",
        "ingredients": {"meat": ["4 slices bacon"], "produce": ["1 zucchini", "1/4 cup dried cranberries"],"dairy": ["1 oz goat cheese"], "spices": [], "other": ["1/3 cup walnuts", "1/5 T apple cider vinegar", "3/4 tsp dijon", "1.5 T maple syrup"]}}
]

## Compiling Shopping List

chicken_meal_list = random.sample(chicken, k=int(chicken_total)) 
beef_meal_list = random.sample(beef, k=int(beef_total)) 
fish_meal_list = random.sample(fish, k=int(fish_total)) 
pork_meal_list = random.sample(pork, k=int(pork_total)) 
other_meal_list = random.sample(other, k=int(other_total)) 

shopping_list = []
chicken_meal_info = ""
beef_meal_info = ""
fish_meal_info = ""
pork_meal_info = ""
other_meal_info = ""

print("\n" + "\n")

for meal in chicken_meal_list:
        single_chicken_meal_name = meal["name"]
        single_chicken_meal_website = meal["website"]
        chicken_meal_info = chicken_meal_info + single_chicken_meal_name + "\n" + single_chicken_meal_website + "\n" + "\n"
        ingredients = (meal["ingredients"])
        shopping_list.append(ingredients)

for meal in beef_meal_list:
        single_beef_meal_name = meal["name"]
        single_beef_meal_website = meal["website"]
        beef_meal_info = beef_meal_info + single_beef_meal_name + "\n" + single_beef_meal_website + "\n" + "\n"
        ingredients = (meal["ingredients"])
        shopping_list.append(ingredients)

for meal in fish_meal_list:
        single_fish_meal_name = meal["name"]
        single_fish_meal_website = meal["website"]
        fish_meal_info = fish_meal_info + single_fish_meal_name + "\n" + single_fish_meal_website + "\n" + "\n"
        ingredients = (meal["ingredients"])
        shopping_list.append(ingredients)

for meal in pork_meal_list:
        single_pork_meal_name = meal["name"]
        single_pork_meal_website = meal["website"]
        pork_meal_info = pork_meal_info + single_pork_meal_name + "\n" + single_pork_meal_website + "\n" + "\n"
        ingredients = (meal["ingredients"])
        shopping_list.append(ingredients)

for meal in other_meal_list:
        single_other_meal_name = meal["name"]
        single_other_meal_website = meal["website"]
        other_meal_info = other_meal_info + single_other_meal_name + "\n" + single_other_meal_website + "\n" + "\n"
        ingredients = (meal["ingredients"])
        shopping_list.append(ingredients)               

all_meat = []
all_produce = []
all_dairy = []
all_spices = []
all_other = [] 


for item in shopping_list:
    meat_by_meal = (item["meat"])
    all_meat = all_meat + meat_by_meal
    other_by_meal = (item["other"])
    all_other = all_other + other_by_meal
    dairy_by_meal = (item["dairy"])
    all_dairy = all_dairy + dairy_by_meal 
    produce_by_meal = (item["produce"])
    all_produce = all_produce + produce_by_meal   
    spices_by_meal = (item["spices"])
    all_spices = all_spices + spices_by_meal

compiled_list = all_produce + all_meat + all_dairy + all_spices + all_other

final_list = chicken_meal_info + " \n" + beef_meal_info + " \n" + fish_meal_info + "\n" + pork_meal_info + "\n" + other_meal_info + "\n" + "\n"

for thing in compiled_list:
    final_list = final_list + thing + "\n"

print(final_list)

## EMAILING List

message = Mail(
    from_email=(os.environ.get("MY_EMAIL_ADDRESS")),
    to_emails=(os.environ.get("KATIE_EMAIL_ADDRESS")),
    subject='Shopping List',
    plain_text_content=final_list )

try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)

except Exception as e:
    print("Oops! Looks like the email didn't go through.")


