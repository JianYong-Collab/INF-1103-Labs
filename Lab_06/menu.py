from inventory_manager import Inventory
from product import Product
from file_manager import FileManager
from utils import get_valid_input
class Menu:
    # Ref to Inventory and file_manager
    __inventory : Inventory
    __file_manager : FileManager
    __file_name : str

    def __init__(self, inventory : Inventory, file_manager : FileManager , file_name : str):
        self.__inventory = inventory
        self.__file_manager = file_manager
        self.__file_name = file_name

    def __display_all_opt(self):
        self.__inventory.display_all()

    def __add_new_product_opt(self):
        productID_input = get_valid_input("Product ID: ","string").upper()
        productName_input = get_valid_input("Name: ","string")
        productPrice_input = float(get_valid_input("Price: ","integer"))
        productStock_input = int(get_valid_input("Stock Quantity: ","integer"))
        add_status = self.__inventory.add_product(Product(productID_input, productName_input, productPrice_input, productStock_input))
    
        if(add_status == False):
            print("Cannot add two different products with same product Ids!!")
        else: 
            print("Product added successfully!")
        
    def __update_stock_opt(self):
        print("\nUpdate Stock")
        productID_input = get_valid_input("Product ID: ","string")
        print("\n")
        product = self.__inventory.search_product(productID_input)
        if(product == None):
            print("Product is not found!!")
        else:
            print("Product Found:")
            print("------------------------------------------------")
            print(f"ID: {product.get_id()}")
            print(f"Name: {product.get_name()}")
            print(f"Price: {product.get_price()}")
            print(f"Stock: {product.get_stock()}")
            print("------------------------------------------------")
            print("\n")
            new_stock_input = get_valid_input("New Stock Quantity: ", "integer")
            self.__inventory.update_inventory_stock(productID_input, new_stock_input)
            print("\n")
            print("Stock Updated Successfully!")

    def __search_prod_opt(self):
        print("\nSearch Product")
        productID_input = get_valid_input("Enter Product ID: ","string")
        print("\n")
        product = self.__inventory.search_product(productID_input)
        if(product == None):
            print("Product is not found!!")
        else:
            print("Product Found:")
            print("------------------------------------------------")
            print(f"ID: {product.get_id()}")
            print(f"Name: {product.get_name()}")
            print(f"Price: {product.get_price()}")
            print(f"Stock: {product.get_stock()}")
            print("------------------------------------------------")
            print("\n")

    def __save_inventory_opt(self):
            #Save Inventory
            print("\nSaving Inventory......")
            inventory_dict = [product.to_dict() for product in self.__inventory.get_inventory()]
            self.__file_manager.save_inventory(inventory_dict, self.__file_name)
            print("Inventory saved successfully to inventory.json")

    def __exit_opt(self):
        print("Thank you for using Inventory Management System.")
        print("Program terminated")

    def __process_input(self, option):
        match(option):
            case("1"):
                self.__display_all_opt()
            case("2"):
                self.__add_new_product_opt()
            case("3"):
                self.__update_stock_opt()
            case("4"):
                self.__search_prod_opt()
            case("5"):
                self.__save_inventory_opt()
            case("6"):
                self.__save_inventory_opt()
                self.__exit_opt()

    def run(self):
        user_input = ""
        while (True):
            print("\n----------- MENU -----------")
            print("1. Display All Products")
            print("2. Add Product")
            print("3. Update Stock")
            print("4. Search Product")
            print("5. Save Inventory")
            print("6. Exit")
            print("----------------------------")

            user_input = input("\nEnter Option: ")
            if(user_input.isdigit() == False or user_input <= "0" or user_input > "6"):
                print("Please enter valid input")
                continue
            # process input
            self.__process_input(user_input)
            if(user_input == "6"):
                break   

