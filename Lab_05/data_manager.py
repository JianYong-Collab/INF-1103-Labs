import os
import json
import inventory_manager

"""
@brief - Load Json file and return dictionary / Create new json file
"""
def load_file(fileName):
    os.chdir("Lab_05")
    cwd = os.getcwd()

    try:
        with open(f"{cwd}/{fileName}","r") as file:
            inventory_manager.load_inventory(json.load(file))
    except FileNotFoundError:
        with open(f"{cwd}/{fileName}","w") as file:
            inventory_manager.load_inventory([])

def save_inventory(inventory, fileName):
    #open the file and overwrite
    cwd = os.getcwd()

    with open(f"{cwd}/{fileName}","w") as file:
            json.dump(inventory,file)