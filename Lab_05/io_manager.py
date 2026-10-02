import inventory_manager

def has_numbers(string_to_check):
    return any(char.isdigit() for char in string_to_check)


def display_menu():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    ## inventory found
    ## inventory loaded
    user_input = ""

    while (True):
        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        user_input = input("Enter Option: ")
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
            print("Add new product")
            productID_input = get_valid_input("Product ID: ","string")
            productName_input = get_valid_input("Name: ","string")
            productPrice_input = int(get_valid_input("Price: ","integer"))
            productStock_input = int(get_valid_input("Stock Quantity: ","integer"))
            inventory_manager.add_product(productID_input,
                                            productName_input,
                                            productPrice_input,
                                            productStock_input)
            print("Product added successfully!")
            pass
        case("3"):
            print("Update Stock")
            productID_input = get_valid_input("Product ID: ","string")
            product = inventory_manager.search_product("ID","P001")
            if(product == None):
                print("Product is not found!!")
            else:
                print("Product Found:")
                print("------------------------------------------------")
                print(f"ID: {product["ID"]}")
                print(f"Price: {product["Price"]}")
                print(f"Stock: {product["Stock"]}")
                print("------------------------------------------------")
            
        case("4"):
            pass
        #Search Product
        case("5"):
            #Save Inventory
            pass
        case("6"):
            #Save Inventory
            pass

# Handle all cases of valid input
# Strings && Integers only
def get_valid_input(input_prompt,input_type):
    user_input = ""
    while True:
        user_input = input(f"{input_prompt}")
        #handle all string input types and integer inputs
        if(input_type == "string" and user_input.isdigit() == True):
            continue

        if(input_type == "integer" and user_input.isdigit() == False):
            continue

        return user_input
