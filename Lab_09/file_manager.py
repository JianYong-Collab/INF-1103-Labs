import os
import json
from inventory_manager import Inventory
from supplier import Supplier
from product_file_strategy import ProductFileStrategy
script_dir = os.path.dirname(os.path.abspath(__file__))

"""
@brief - Load Json file and return List / Create new json file
"""
def load_file(fileName, product_loader: ProductFileStrategy, inventory: Inventory, supplier: Supplier) -> None:
    file_path = os.path.join(script_dir, fileName)
    product_loader.load_products(file_path, inventory, supplier)
            
def save_inventory(inventory, fileName: str, product_saver : ProductFileStrategy) -> None:
    #open the file and overwrite
    file_path = os.path.join(script_dir, fileName)
    product_saver.save_file(file_path, inventory)