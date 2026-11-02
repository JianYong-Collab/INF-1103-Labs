from inventory_manager import Inventory
from file_manager import FileManager
from menu import Menu
from constants import INVENTORY_FILE


# start of code
# Load Data_Manager
# Load Menu Class
# Initialise Class Instances
file_manager = FileManager()
inventory = Inventory()
menu = Menu(inventory, file_manager, INVENTORY_FILE)
print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")

data = file_manager.load_file(INVENTORY_FILE)
if data:
    print("inventory.json found.")
    print("Inventory loaded successfully")
    inventory.set_inventory(data)
menu.run()
