# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Pablo Montijo,3.8.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
import sys

strFileName = 'products.txt'
lstOfProductObjects = []
product_name = ''
product_price = ''
strStatus = ""



class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Pablo Montijo,3.8.2021,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to the Product class
    # --Fields--

    # -- Constructor --
    def __init__(self, product_name='', product_price=''):
        #-- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    @property
    def product_name(self):
        return self.__product_name

    @product_name.setter  # The NAME MUST MATCH the property's!
    def product_name(self, value):  # (setter or mutator)
        self.__product_name = value

    @property
    def product_price(self):
        return self.__product_price

    @product_price.setter  # The NAME MUST MATCH the property's!
    def product_price(self, value):  # (setter or mutator)
        self.__product_price = value
    def __str__(self):
        return self.product_name + ' ' + self.product_price
# Data -------------------------------------------------------------------- #

# Custom Error Handling --------------------------------------------------- #

class ProductIsNumericError(Exception):    # Custom class to catch Names that include numbers
    def __str__(self):
        return 'A Product Name Cannot be Numeric'

# Custom Error Handling --------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)
        add_data_to_list: (a product object)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Pablo Montijo,3.8.2021,Modified code to complete assignment 8
    """
    pass
    # TODO: Add Code to process data from a file
    # TODO: Add Code to process data to a file

    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (lstOfProductObjects)
        """
        list_of_rows.clear()  # clear current data
        lstOfProductObjects.clear()
        file = open(file_name, "r")
        for line in file:
            product, price = line.split(",")
            lstOfProductObjects.append(Product(product, price))
        file.close()
        return lstOfProductObjects

    @staticmethod
    def add_data_to_list(product, price, lstOfProductObjects):
        # TODO: Add Code Here!
        """  Adds data to a list of product objects

        :param product: (string) with product name:
        :param price: (list) with product price:
        :param lstOfProductObjects: (list) with product objects:
        :return: (lstOfProductObjects)
        """
        lstOfProductObjects.append(Product(product, price))
        return lstOfProductObjects

    @staticmethod
    def remove_data_from_list(product, lstOfProductObjects):
        # TODO: Add Code Here!
        """  Adds data to a list of product objects

        :param product: (string) with product name:
        :param lstOfProductObjects: (list) with product objects:
        :return: (lstOfProductObjects)
        """
        for obj in lstOfProductObjects:
            if obj.product_name == product:
                lstOfProductObjects.remove(obj)
        return lstOfProductObjects

    @staticmethod
    def save_data_to_file(file_name, lstOfProductObjects):
        # TODO: Add Code Here!
        """  Adds data to a list of product objects

        :param file_name: (string) with file name:
        :param lstOfProductObjects: (list) with product objects:
        :return: (lstOfProductObjects)
        """
        file = open(file_name, "w")
        for obj in lstOfProductObjects:
            product = str(obj.product_name).strip()
            price = str(obj.product_price).strip()
            row = product + ',' + price + "\n"
            file.write(row)
        file.close()
        return lstOfProductObjects


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    pass
    # TODO: Add code to show menu to user
    # TODO: Add code to get user's choice
    # TODO: Add code to show the current data from the file to user
    # TODO: Add code to get product data from user
# Presentation (Input/Output)  -------------------------------------------- #
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product
        2) Remove an existing Product
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_products_in_list(lstOfProductObjects):
        """ Shows the current Tasks in the list of dictionaries rows

        :param lstOfProductObjects: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for obj in lstOfProductObjects:
            product = str(obj.product_name).strip()
            price = str(obj.product_price).strip()
            print(product + ',' + price)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_product_and_price():
        pass  # TODO: Add Code Here!
        """ Input a new product

        :return: product, price
        """
        try:
            product = str(input('enter Product Name: ')).strip()

            if product.isnumeric():
                raise ProductIsNumericError()

        except Exception as e:
            print(e, e.__doc__, type(e), sep='\n')
            sys.exit()

        try:
            piece_price = float(input('enter Product Price: '))

        except ValueError as e:
            print(e, e.__doc__, type(e), sep='\n')
            sys.exit()

        price = str(piece_price).strip()
        return product, price

    @staticmethod
    def input_product_to_remove():
        pass  # TODO: Add Code Here!
        """ Input a product to remove

        :return: product_name
        """
        product_name = str(input('enter Product to remove: ')).strip()
        return product_name


# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Step 1 - When the program starts, Load data from ToDoFile.txt.

FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)  # read file data
# lstOfProductObjects returned

# Step 2 - Display a menu of choices to the user

while (True):
    # Step 3 Show current data
    IO.print_current_products_in_list(lstOfProductObjects)  # Show current data in the list/table
    # nothing returned
    IO.print_menu_Tasks()  # Shows menu
    # menu printed
    strChoice = IO.input_menu_choice()  # Get menu option
    # choice returned

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Product
        # TODO: Add Code Here
        product_name, product_price = IO.input_new_product_and_price()
        # product_name, product_price returned
        FileProcessor.add_data_to_list(product_name, product_price, FileProcessor.read_data_from_file(strFileName, lstOfProductObjects))
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # TODO: Add Code Here
        product_name = IO.input_product_to_remove()
        # product_name returned
        FileProcessor.remove_data_from_list(product_name, FileProcessor.read_data_from_file(strFileName, lstOfProductObjects))
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # TODO: Add Code Here!
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # TODO: Add Code Here!
            FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit


