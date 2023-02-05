
#====Define Shoe Class====

# Defining the Shoe class with five attributes
# Also defining three methods to 1) return the cost of a shoe and 2) the quantity of a shoe (both returned as integers) and 3) return the string representation of a shoe.

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
    def get_cost(self):
        return int(self.cost)

    def get_quantity(self):
        return int(self.quantity)

    def __str__(self):
        return (f"{self.country} {self.code} {self.product} {self.cost} {self.quantity}")


#====Defining Functions====

# Function to read the shoe data file (inventory.txt) and create a list of shoe objects, which is then used by all the other functions.
# It asks the user for the name of the file, so I can include try-except error handling.

def read_shoes_data():
    
    print("\nDo you wish to continue with the default data file (\"inventory.txt\"), or do you want to enter the name of a new source data file?")
    file_choice = input("\nType 'continue' to use the default data file, or 'new' to enter the name of a new data file : ")
    file_choice = file_choice.lower()

    while file_choice != "continue" and file_choice !="new":
        file_choice = input("That is an incorrect input.  Please enter 'continue' or 'new' : ")

    if file_choice == "continue":
        with open("inventory.txt", "r", encoding="utf-8") as shoes_data:
            shoes_data_by_line = shoes_data.readlines()[1:]
            for line in shoes_data_by_line:
                data = line.split(",")
                shoe_list.append(Shoe(data[0], data[1], data[2], data[3], data[4]))

    else:
        while True:
            try:
                file_name = input("\nPlease enter the name of your source data file : ")
                # data file is called inventory.txt
                with open(file_name, "r", encoding="utf-8") as shoes_data:
                    shoes_data_by_line = shoes_data.readlines()[1:]
                    for line in shoes_data_by_line:
                        data = line.split(",")
                        shoe_list.append(Shoe(data[0], data[1], data[2], data[3], data[4]))
                break
            except FileNotFoundError:
                print("\nThat file does not exist or is not in this folder.  Please check what you entered and try again.  Don't forget to include .txt at the end of the filename.")
    
# Function to create a new shoe object and append it to shoe_list.

def capture_shoes():

    print("\nIn order to add a new item to inventory, you need to input the following data:")
    country = input("\tCountry : ")
    code = input("\tCode (SKU followed by five digits) : ")
    product = input("\tProduct Name : ")
    cost = input("\tCost (in Rand) : ")
    quantity = input("\tQuantity : ")
    shoe_list.append(Shoe(country, code, product, cost, quantity)) 
    print("\nYour item has been added to the inventory.")

# Function for viewing all the shoes in shoe_list.
# To use tabulate instead of iterating through the __str__ method, this function creates a new list of lists (rather than a list of objects) which tabulate can then display.

def view_all():

    shoe_list_list = []
    for shoe in shoe_list:
        data_new = [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity]
        shoe_list_list.append(data_new)

    print("")
    print(tabulate(shoe_list_list, headers = ["Country", "Code", "Product", "Cost", "Quantity"], tablefmt = "pipe"))

# Function for finding the shoe with the lowest quantity, offering the user the option to restock, and increasing the quantity in stock by that amount.

def re_stock():

    index = (min(range(len(shoe_list)), key=lambda i:shoe_list[i].get_quantity()))

    print(f"\nThe lowest inventory item is {shoe_list[index].product} with {shoe_list[index].get_quantity()} in stock.")
    
    proceed = input("Do you want to re-stock this item? (Y/N) : ")
    proceed = proceed.lower()
    
    while proceed != "y" and proceed != "n":
        proceed = input("That is an incorrect input.  Please enter Y or N : ")
        proceed = proceed.lower()

    if proceed == "y":
        while True:
            try:
                re_stock_quantity = int(input("\nPlease enter the quantity to be restocked : "))
                break
            except ValueError:
                print("\nThat is not a number.")
        new_quantity = shoe_list[index].get_quantity() + re_stock_quantity
        shoe_list[index].quantity = str(new_quantity) + "\n"
        print("\nThe quantity of this item has been updated.")

# Function for searching for a shoe based on the code and displaying that object.
# If the code is found, then the item is displayed.
# If the code is not found the user is given the choice of continuing their search, in which case this function calls itself again.  If the user stops the search, the main menu is returned.

def search_shoe():

    shoe_code = input("\nPlease enter the shoe code you wish to search for (in the format SKU followed by five digits) : ")

    found = False

    for shoe in shoe_list:
        if shoe_code == shoe.code:
            found = True
            print("\nYour search has found the following item :")
            print(f"\tProduct: \t{shoe.product}\n\tCountry: \t{shoe.country}\n\tCode: \t\t{shoe.code}\n\tCost: \t\t{shoe.cost}\n\tQuantity: \t{shoe.quantity}")

    if found == False:
        print("\nThat code does not exist.")
        proceed = input("Do you wish to continue your search? (Y/N) : ")
        proceed = proceed.lower()
        while proceed != "y" and proceed != "n":
            proceed = input("That is an incorrect input.  Please enter Y or N : ")
            proceed = proceed.lower()
        if proceed == "y":
            search_shoe()

# Function for displaying the total value of each shoe in stock, and also the total value of all shoes in stock.

def value_per_item():
    
    total_value = 0
    print("")
    for shoe in shoe_list:
        value = (shoe.get_cost()*shoe.get_quantity())
        print(f"The value of {shoe.product} in stock = R{value:,d}.")
        total_value = total_value + value

    print(f"\nThe total value of all shoes in stock is R{total_value:,d}")

# Function for finding the finding the shoe with the highest quantity, and displaying the shoe as on sale.

def highest_qty():

    index = (max(range(len(shoe_list)), key=lambda i:shoe_list[i].get_quantity()))

    print(f"\nThe highest inventory item is {shoe_list[index].product} with {shoe_list[index].get_quantity()} in stock.")
    
    proceed = input("Do you want to put this item on sale? (Y/N) : ")
    proceed = proceed.lower()
    
    while proceed != "y" and proceed != "n":
        proceed = input("That is an incorrect input.  Please enter Y or N : ")
        proceed = proceed.lower()

    if proceed == "y":
        print("\nThe following item is on sale :")
        print(f"\tProduct: \t{shoe_list[index].product}\n\tCountry: \t{shoe_list[index].country}\n\tCode: \t\t{shoe_list[index].code}\n\tCost: \t\t{shoe_list[index].cost}\n\tQuantity: \t{shoe_list[index].quantity}")


#====Program Run====

# This section runs the program.
# It imports the tabulate module, sets up shoe_list as a blank list which is then populated by the read_shoes_data function, and then presents the user with the main menu.
# If read_shoes_data() cannot find the input file to populate shoe_list it will not proceed on to the main menu loop.

print("\nWelcome to the Nike Inventory Management Progam.")

from tabulate import tabulate

shoe_list = []
read_shoes_data()

choice = ""
while choice != "7":

    print("\nPlease choose an option from the menu below :")
    print("1 - create a new inventory item")
    print("2 - view all the items in inventory")    
    print("3 - restock item with the lowest inventory")
    print("4 - search the inventory for a specific item")
    print("5 - calculate the value of all items in stock")
    print("6 - find the item with the highest inventory to put on sale")
    print("7 - exit the program")
    choice = input("Select an option : ")

    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice !="7":
        choice = input("That option does not exist. Select an option : ")
    if choice == "1":
        capture_shoes()
    if choice == "2":
        view_all()
    if choice == "3":
        re_stock()
    if choice == "4":
        search_shoe()
    if choice == "5":
        value_per_item()
    if choice == "6":
        highest_qty()
    if choice == "7":
        print("\nGoodbye.\n")
        exit()
