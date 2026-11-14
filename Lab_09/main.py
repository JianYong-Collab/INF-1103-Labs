from inventory_manager import Inventory
from file_manager import load_file
from menu import run
from constants import INVENTORY_FILE
from product import Product
from supplier import Supplier
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from product_file_strategy import CSVProductFileStrategy, JSONProductFileStrategy
# start of code
# Load Data_Manager
# Load Menu Class
# Initialise Class Instances
inventory = Inventory()
# order_1 = Order("O111")
# product = DigitalProduct("P111", "POTATO",10,22,None,234)
# order_1.add_order_line(product,25)
# print(order_1.calculate_total())
# order_1.set_discount(BulkDiscount(200,20))
# print(order_1.calculate_total())
# order_1.set_discount(PercentageDiscount(10))
# print(order_1.calculate_total())
supplier = Supplier("SUPPLIER1","OS_CORPORATIONS", "OS_CORP@GMAIL.COM")
print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")
file_strategy = CSVProductFileStrategy()
load_file(INVENTORY_FILE, file_strategy, inventory, supplier)
run(inventory, INVENTORY_FILE, file_strategy)
