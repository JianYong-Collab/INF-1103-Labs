import os
import json
script_dir = os.path.dirname(os.path.abspath(__file__))

"""
@brief - Load Json file and return List / Create new json file
"""
def load_file(fileName) -> list[dict]:
    file_path = os.path.join(script_dir, fileName)
    if not os.path.exists(file_path):
        with open(file_path,"w") as file:
            return []
    try:
        with open(file_path,"r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        with open(file_path,"w") as file:
            return []
            
def save_inventory(inventory, fileName) -> None:
    #open the file and overwrite
    file_path = os.path.join(script_dir, fileName)
    with open(file_path,"w") as file:
            json.dump(inventory,file, indent=4)