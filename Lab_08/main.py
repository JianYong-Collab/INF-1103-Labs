from inventory_manager import Inventory
from file_manager import load_file
from menu import run
from utils import convert_js_to_products
from constants import INVENTORY_FILE
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product import Product
from supplier import Supplier
from order import Order

# start of code
# Load Data_Manager
# Load Menu Class
# Initialise Class Instances
inventory = Inventory()
print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")

raw_data = load_file(INVENTORY_FILE)

if raw_data:
    print("inventory.json found.")
    print("Inventory loaded successfully")
    data = convert_js_to_products(raw_data)
    inventory.set_inventory(data)
    
run(inventory, INVENTORY_FILE)
