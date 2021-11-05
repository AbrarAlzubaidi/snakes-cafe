
"""
this program show the user a menu of snake cafe 
and make the user able to order from the menu
after finishing the order show the summary ^^ to make sure that he/she ordered those

"""


def introMsg():
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print("** To quit at any time, type \"quit\" **")
    print("**************************************\n")


def orderMesg():
    print("***********************************")
    print("** What would you like to order? **")
    print("***********************************")


Menu = [
    {
        "dish":"Wings",
        "count":0
    },
    {
        "dish":"Cookies",
        "count":0
    },
    {
        "dish":"Spring Rolls",
        "count":0
    },
    {
        "dish":"Salmon",
        "count":0
    },
    {
        "dish":"Meat Tornado",
        "count":0
    },
    {
        "dish":"A Literal Garden",
        "count":0
    },
    {
        "dish":"Ice Cream",
        "count":0
    },
     {
        "dish":"Cake",
        "count":0
    },
    {
        "dish":"Pie",
        "count":0
    },
    {
        "dish":"Coffee",
        "count":0
    },
    {
        "dish":"Tea",
        "count":0
    },
    {
        "dish":"Unicorn Tears",
        "count":0
    },
    
]


def Appetizers():
    print("Appetizers\n----------\n Wings\n Cookies\n Spring Rolls\n  ")


def Entrees():
    print("Entrees\n-------\n Salmon\n Steak\n Meat Tornado\n A Literal Garden\n ")


def Desserts():
    print("Desserts\n--------\n Ice Cream\n Cake\n Pie\n  ")


def Drinks():
    print("Drinks\n------\n Coffee\n Tea\n Unicorn Tears\n  ")


def clientOrder():   
    while True:
        print("> ")
        order = input()
        for item in Menu:
            if order == item["dish"]:
                count=item["count"]
                print(item["dish"] )
                print(item["count"])
                count+=1
                item["count"]= count
                print(f"** {count} order of {order} have been added to your meal **")
                break
        if order == "quit":
            break
        

def summary():
    for item in Menu:
        if item["count"] != 0:
            count = item["count"]
            dish = item["dish"]
            print(f"** {count} order of {dish} have been added to your meal **")
        
    
if __name__ == "__main__":
    introMsg()
    Appetizers()
    Entrees()
    Desserts()
    Drinks()
    orderMesg()
    clientOrder()
    summary()
