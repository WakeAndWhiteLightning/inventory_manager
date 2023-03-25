from tabulate import tabulate
#========The beginning of the class==========
#Define the class for shoes with methods to return the cost, quantity and string of the object. 
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        return f'{self.product}, {self.code}, {self.quantity}, {self.cost}, {self.country}'
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========r
'''
The list will be used to store a list of objects of shoes.
'''
#Create the list to hold all the shoe objects
shoe_list = []
#==========Functions outside the class==============
#Fucntion to read the shoe data from the file into shoe_list
def read_shoes_data():
    #Open the inventory file for reading
    with open('inventory.txt', 'r') as file:
        
        #Create a list from inventory for each line and add the first line to the shoe_list
        inventory = file.readlines()
        shoe_list.append(inventory[0].strip('\n'))
        
        #For every other line create a Shoe object from the line info and add it to the shoe_list
        for shoe in inventory[1:]:
            shoe = shoe.split(',')
            pair = Shoe(shoe[0], shoe[1], shoe[2], shoe[3], shoe[4].strip('\n'))
            shoe_list.append(pair)
            
    print('Shoe objects created from file')
        
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''

#Function to add a new shoe object to the list
def capture_shoes():
    print('''
    ______________________________________________________________________

    To add your shoes please enter the information below''')
    
    #Get class properties from user
    country = input('Enter the country: ')
    code = input('Enter the code: ')
    product = input('Enter the product name: ')
    cost = input('Enter the price (numerical symbols only): ')
    quantity = input('Enter the quantity:') 
    print('''_____________________________________________________________________''')

    #Create the object from inputs and add to the list
    cap_shoes = Shoe(country, code, product, cost, quantity)
    shoe_list.append(cap_shoes)

    print(''' 
    *****
    Your shoes have been added to the list
    *****''')


    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

#Fucntion to display a table of all the shoes 
def view_all():
    table_data = []

    #For every object - except the first - in shoe_lsit, turn it into a lsit and add to tbale_data. 
    for shoe in shoe_list[1:]:
        shoe_info = f'{shoe.product}, {shoe.code}, {shoe.quantity}, {shoe.cost}, {shoe.country}'
        shoe_info_list = shoe_info.split(', ')
        table_data.append(shoe_info_list)
    
    #Create and display the table
    print(tabulate(table_data, headers = ['Country', 'Code', 'Product', 'Quantity', 'Price']))
    print('sucess')

'''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

#Function to find the shoe with the lowest stock and ask if you would like to restock it
def re_stock():
    while True:
        
        #Find the shoe with the lowest stock
        lowest_stock = shoe_list[1]
        for shoe in shoe_list[2:]:
            if int(lowest_stock.quantity) > int(shoe.quantity):
                lowest_stock = shoe
        
        #Ask the user if they would like to restock
        restock = input(f'''
______________________________________________________________________________________________________________
        
The shoes with the lowest stock are the {lowest_stock.product} with only {lowest_stock.quantity} in stock. 
          
Would you like to restock this product? y/n: ''')
        
        #Ask for the quantity to restock or break depending on input
        if restock.lower() == 'y':
            add_quantity = int(input('How many pairs would you like to add: '))
            lowest_stock.quantity = str(int(lowest_stock.quantity) + add_quantity)
        if restock.lower() == 'n':
            break
        else:
            continue

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

#Function to find a show by code
def search_shoe():

    #Loop through all shoes to check if the code entered matches any objects
    search_code = input('What would you like to search for: ')
    for shoe in shoe_list[1:]:
        if shoe.code == search_code: 
            print(f'''
            __________________________
            Shoe Found: 

            {f'{shoe.product}, {shoe.code}, {shoe.quantity}, {shoe.cost}, {shoe.country}'}
            __________________________''')
            return
    print('Shoe not found')
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    
    #Create a list for the table date and add the header titles with the additional 'Value' header
    table_data = []
    header_list = shoe_list[0].split(',')
    header_list.append('Value')
    table_data.append(header_list)

    #For every shoe object - except the first one - in the list create a list of the objects properties, including a 'Value' property, and append it to the table_data list
    for shoe in shoe_list[1:]:
        shoe_info = f'{shoe.product}, {shoe.code}, {shoe.quantity}, {shoe.cost}, {shoe.country}'
        shoe_info_list = shoe_info.split(', ')
        value = int(shoe_info_list[2]) * int(shoe_info_list[3])
        shoe_info_list.append(value)
        table_data.append(shoe_info_list)
    print(tabulate(table_data, headers = 'firstrow' ))
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

#Function to find shoe with highest quantity and display it for sale 
def highest_qty():

    #Loop through each object to find lowest quantity property
    highest_stock = shoe_list[1]
    for shoe in shoe_list[2:]:
        if int(highest_stock.quantity) < int(shoe.quantity):
            highest_stock = shoe
    
    #Display shoe as for sale
    print(f'''
      ***  ON SALE NOW  ***  
    
    {f'{highest_stock.product}, {highest_stock.code}, {highest_stock.quantity}, {highest_stock.cost}, {highest_stock.country}'}
      
      ***      ***      ***''')
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''

#Create menu so the user can execute each of the functions
while True: 
    choice = input('''
     Make a selection
    r  - read shoe data from file
    a  - add new shoe data
    va - view all shoe data 
    re - restock the pair of shoes with the lowest quantity
    s  - search for a pair of shoes
    v  - show total stock value for each pair of shoes
    h  - print which shoe has the higest stock quantity and is on sale
    e  - exit
     ''')

    if choice == 'r':
        read_shoes_data()
    
    elif choice == 'a':
        capture_shoes()
    
    elif choice == 'va':
        view_all()
    
    elif choice == 're':
        re_stock()
    
    elif choice == 's':
        search_shoe()
    
    elif choice == 'v':
        value_per_item()
    
    elif choice == 'h':
        highest_qty()

    elif choice == 'e': 
        break

    else:
        print('Selection not recognised please try again')

