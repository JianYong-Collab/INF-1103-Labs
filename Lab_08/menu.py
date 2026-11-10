from inventory_manager import Inventory
from digital_product import DigitalProduct
from physical_product import PhysicalProduct
from file_manager import save_inventory
from utils import get_valid_input
from supplier import Supplier

supplier = Supplier("SUPPLIER1","OS_CORPORATIONS", "OS_CORP@GMAIL.COM")
def display_all_opt(inventory: Inventory):
   inventory.display_all()

def add_new_product_opt(inventory: Inventory):
    productType_input = get_valid_input("Product Type: ", "string").lower()
    #Exit if user typed an invalid type
    if(productType_input != "physical" and productType_input != "digital"):
        print("Product Type does not exist!!")
        return

    productID_input = get_valid_input("Product ID: ","string").upper()
    productName_input = get_valid_input("Name: ","string")
    productPrice_input = float(get_valid_input("Price: ","number"))
    productStock_input = int(get_valid_input("Stock Quantity: ","number"))
    if(productType_input == "physical"):
        productWeight_input = float(get_valid_input("Weight: ","number"))
        add_status = inventory.add_product(PhysicalProduct(productID_input, productName_input, productPrice_input, productStock_input, supplier, productWeight_input))

    elif(productType_input == "digital"):
        productDownload_size_input = float(get_valid_input("Download Size: ","number"))
        add_status = inventory.add_product(DigitalProduct(productID_input, productName_input, productPrice_input, productStock_input, supplier, productDownload_size_input))

    if(add_status == False):
        print("Cannot add two different products with same product Ids!!")
    else: 
        print("Product added successfully!")
    
def update_stock_opt(inventory: Inventory):
    print("\nUpdate Stock")
    productID_input = get_valid_input("Product ID: ","string").upper()
    print("\n")
    product = inventory.search_product(productID_input)
    if(product == None):
        print("Product is not found!!")
    else:
        print("Product Found:")
        print("------------------------------------------------")
        print(f"ID: {product.id}")
        print(f"Name: {product.name}")
        print(f"Price: {product.price}")
        print(f"Stock: {product.stock}")
        product.get_fulfilment_info()
        if(isinstance(product, PhysicalProduct)):
            product.calculate_shipping_cost()

        print("------------------------------------------------")
        print("\n")
        new_stock_input = get_valid_input("New Stock Quantity: ", "integer")
        inventory.update_inventory_stock(productID_input, new_stock_input)
        print("\n")
        print("Stock Updated Successfully!")

def search_prod_opt(inventory: Inventory):
    print("\nSearch Product")
    productID_input = get_valid_input("Enter Product ID: ","string").upper()
    print("\n")
    product = inventory.search_product(productID_input)
    if(product == None):
        print("Product is not found!!")
    else:
        print("Product Found:")
        print("------------------------------------------------")
        print(f"ID: {product.id}")
        print(f"Name: {product.name}")
        print(f"Price: {product.price}")
        print(f"Stock: {product.stock}")
        product.get_fulfilment_info()
        if(isinstance(product, PhysicalProduct)):
            product.calculate_shipping_cost()
        print("------------------------------------------------")
        print("")

def save_inventory_opt(inventory: Inventory, file_name: str):
        #Save Inventory
        print("\nSaving Inventory......")
        inventory_dict = [product.to_dict() for product in inventory.inventory]
        save_inventory(inventory_dict, file_name)
        print("Inventory saved successfully to inventory.json")

def exit_opt():
    print("Thank you for using Inventory Management System.")
    print("Program terminated")

def process_input(option: str, inventory: Inventory, file_name: str):
    match(option):
        case("1"):
            display_all_opt(inventory)
        case("2"):
            add_new_product_opt(inventory)
        case("3"):
            update_stock_opt(inventory)
        case("4"):
            search_prod_opt(inventory)
        case("5"):
            save_inventory_opt(inventory, file_name)
        case("6"):
            save_inventory_opt(inventory, file_name)
            exit_opt()

def run(inventory: Inventory, file_name: str):
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
        process_input(user_input, inventory, file_name)
        if(user_input == "6"):
            break   

