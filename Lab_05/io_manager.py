import inventory_manager
import data_manager
INVENTORY_FILE = "inventory.json"

#Note This cannot check for negative numbers
def is_number(string_to_check):
    try:
        return float(string_to_check)
    except (ValueError, TypeError):
        return 0


def display_menu():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================\n")

    data_manager.load_file(INVENTORY_FILE)
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
        if(user_input.isdigit() == False or len(user_input) > 1 ):
            print("Please enter valid input")
        # process input
        process_input(user_input)
        if(user_input == "6"):
            break

    print("Thank you for using Inventory Management System.")
    print("Program terminated")

def process_input(option):
    match(option):
        case("1"):
           inventory_manager.display_all()
        case("2"):
            print("\nAdd new product")
            productID_input = get_valid_input("Product ID: ","string")
            productName_input = get_valid_input("Name: ","string")
            productPrice_input = float(get_valid_input("Price: ","integer"))
            productStock_input = int(get_valid_input("Stock Quantity: ","integer"))
            add_status = inventory_manager.add_product(productID_input,
                                            productName_input,
                                            productPrice_input,
                                            productStock_input)
            if(add_status == False):
                print("Cannot add two different products with same product Ids!!")
            else: 
                print("Product added successfully!")
        case("3"):
            print("\nUpdate Stock")
            productID_input = get_valid_input("Product ID: ","string")
            print("\n")
            product = inventory_manager.search_product("ID",productID_input)
            if(product == None):
                print("Product is not found!!")
            else:
                print("Product Found:")
                print("------------------------------------------------")
                print(f"ID: {product['ID']}")
                print(f"Price: {product['Price']}")
                print(f"Stock: {product['Stock']}")
                print("------------------------------------------------")
                print("\n")
                new_stock_input = get_valid_input("New Stock Quantity: ", "integer")
                inventory_manager.update_stock(product['ID'], new_stock_input)
                print("\n")
                print("Stock Updated Successfully!")
            
        case("4"):
            print("\nSearch Product")
            productID_input = get_valid_input("Enter Product ID: ","string")
            print("\n")
            product = inventory_manager.search_product("ID",productID_input)
            if(product == None):
                print("Product is not found!!")
            else:
                print("Product Found:")
                print("------------------------------------------------")
                print(f"ID: {product['ID']}")
                print(f"Price: {product['Price']}")
                print(f"Stock: {product['Stock']}")
                print("------------------------------------------------")
                print("\n")

        case("5"):
            #Save Inventory
            print("\nSaving Inventory......")
            data_manager.save_inventory(inventory_manager.get_inventory(), INVENTORY_FILE)
            print("Inventory saved successfully to inventory.json")
        case("6"):
            #Save Inventory
            print("\nSaving Inventory before exit.....")
            data_manager.save_inventory(inventory_manager.get_inventory(), INVENTORY_FILE)
            print("Inventory saved successfully.")


# Handle all cases of valid input
# Strings && Integers only
def get_valid_input(input_prompt,input_type):
    user_input = ""
    while True:
        user_input = input(f"{input_prompt}")
        #handle all string input types and integer inputs
        if(input_type == "string" and user_input.isdigit() == True):
            continue

        if(input_type == "integer" and is_number(user_input) == False):
            continue

        return user_input
