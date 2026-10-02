inventory_container = []
def add_product(productID, productName, productPrice, productStock):
    inventory_container.append(
        {
        "ID"    :productID,
        "Name"  :productName,
        "Price" :productPrice,
        "Stock" :productStock
        }
    )   

def update_stock(productID):
    inventory_container[productID]
    pass

def search_product(productKey, productID):
    for product in inventory_container:
        for (key, value) in product.items():
            if(key == productKey and value == productID):
                print("Found Product")
                print(product)
                return product
    return None
    

def display_all():
    print("Current Inventory")
    print("------------------------------------------------")
    for product in inventory_container:
        product_display = ""
        for index, key in enumerate(product.keys()):
            if(index == len(product.keys())-1):
                product_display += f"{key}: {product[key]}"
            else:
                product_display += f"{key}: {product[key]} | "
        print(product_display)

    print("------------------------------------------------")


def load_inventory():
    pass
