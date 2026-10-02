import os
import json
import inventory_manager

"""
@brief - Load Json file and return dictionary / Create new json file
"""
def load_file(fileName):

    try:
        with open(f"{fileName}","r") as file:
            if(file == ""):
                 return
            file.seek(0)
            inventory_manager.load_inventory(json.load(file))
            print("inventory.json found.")
            print("Inventory loaded successfully")
    except FileNotFoundError:
        with open(f"{fileName}","w") as file:
            inventory_manager.load_inventory([])

def save_inventory(inventory, fileName):
    #open the file and overwrite

    with open(f"{fileName}","w") as file:
            json.dump(inventory,file)