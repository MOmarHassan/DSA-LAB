spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

#1------------------------------------------------------------------------------------------------------------

list1=[]
def get_names(x):
    for i in x:
        list1.append(i["name"])
    print(list1)

#get_names(spicy_foods)

#2------------------------------------------------------------------------------------------------------------

list2=[]
def get_spiciest_foods(x):
    for i in x:
        if i["heat_level"] > 5:
            list2.append(i)
    return list2
    

#print(get_spiciest_foods(spicy_foods))

#4------------------------------------------------------------------------------------------------------------

list3=[]
def print_spicy_food(x):
    for i in x:
        print(i["name"],"|","Heat Level",i["heat_level"]*"H")
    
#print_spicy_food(spicy_foods)

#6------------------------------------------------------------------------------------------------------------

def get_spicy_food_by_cuisine(x,j):
    for i in x:
        if i["cuisine"]==j:
            print(i)
        else:
            pass

#get_spicy_food_by_cuisine(spicy_foods,"American")
#get_spicy_food_by_cuisine(spicy_foods,"Thai")

#8------------------------------------------------------------------------------------------------------------

def print_spiciest_food(x):
    
    print_spicy_food(get_spiciest_foods(x))

#print_spiciest_food(spicy_foods)

#10-----------------------------------------------------------------------------------------------------------        

def get_average_heat_level(x):
    list4=[]
    for i in x:
        list4.append(i["heat_level"])
    average_heat_value=sum(list4)/len(list4)
    return average_heat_value , 'is the average heat value'

#print(get_average_heat_level(spicy_foods))

#11-----------------------------------------------------------------------------------------------------------

def create_spicy_food(x,y):
    spicy_foods.append(y)
    return spicy_foods



new_spicy_food={'name': 'Griot',
'cuisine': 'Haitian',
'heat_level': 10,}

print(create_spicy_food(spicy_foods, new_spicy_food))
    
#-----------------------------------------------------------------------------------------------------------