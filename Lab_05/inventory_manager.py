import copy
inventory_container = []
def add_product(productID, productName, productPrice, productStock):
    #Avoid duplicate ID
    for product in inventory_container:
        for value in product.values():
            if(value == productID):
                return False
    inventory_container.append(
        {
        "ID"    :productID,
        "Name"  :productName,
        "Price" :productPrice,
        "Stock" :productStock
        }
    )
    return True   

def update_stock(productID, newValue):
    for product in inventory_container:
        for value in product.values():
            if(value == productID):
                product["Stock"] = newValue
                return

def search_product(productKey, productID):
    for product in inventory_container:
        for (key, value) in product.items():
            if(key == productKey and value == productID):
                return product
    return None
    

def display_all():
    if(len(inventory_container) == 0):
        print("No Stock")
        return

    print("\nCurrent Inventory")
    print("------------------------------------------------")
    for product in inventory_container:
        product_display = ""
        for index, key in enumerate(product.keys()):
            if(index == len(product.keys())-1):
                product_display += f"{key}: {product[key]}"
            else:
                if(key == "Price"):
                    product_display += f"{key}: ${product[key]} | "
                else:
                    product_display += f"{key}: {product[key]} | "
        print(product_display)

    print("------------------------------------------------")

def get_inventory():
    return inventory_container

def load_inventory(file_data):
    global inventory_container
    inventory_container = copy.deepcopy(file_data)