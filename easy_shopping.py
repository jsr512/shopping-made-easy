

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

## Recipe List

chicken = [
        {"name": "Beer Can Chicken",
        "website": "https://www.foodnetwork.com/recipes/patrick-and-gina-neely/pats-beer-can-grilled-chicken-recipe-1945080",
        "ingredients": {"4-lb whole chicken": "meat", "1 12 ounce beer": "other"}}
]

beef = [
        {"name": "Slow Cooker Korean Beef",
        "website": "https://www.ihearteating.com/slow-cooker-korean-beef/",
        "ingredients": {"4-lb boneless beef chuck roast": "meat", "1 cup beef broth": "canned goods", "1/2 cup soy sauce": "sauces", "1/3 cup brown sugar": "baking", "5 cloves garlic": "spices", "2 T sesame Oil": "baking", "2 T rice vinegar":"baking", "2 T ginger": "spices", "2 T gochujang": "asian", "1/2 tsp onion powder": "spices"}},
        
        {"name": "Cheeseburger Casserole",
        "website": "https://lowcarbyum.com/bacon-cheeseburger-casserole/",
        "ingredients": {"2-lbs ground beef": "meat", "1-lb bacon": "meat", "8 eggs": "dairy", "2 cloves garlic": "spices", "1/2 tsp onion powder": "spices", "1 can tomato paste": "canned goods", "1 cup heavy cream": "dairy", "12 ounces grated cheddar": "dairy"}}
]


fish = [
        {"name": "Baked Lemon Haddock",
        "website": "https://www.tasteofhome.com/recipes/baked-lemon-haddock/",
        "ingredients": {"2-lb haddock": "meat", "1 cum bread crumbs": "baking", "1/4 cup butter": "dairy", "2 T parsley": "spices", "2 T Lemon Zest": "produce", "1/2 tsp garlic powder": "spices"}}
]

