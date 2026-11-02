import os
import json
from dataclasses import dataclass
from digital_product import DigitalProduct
from physical_product import PhysicalProduct

class FileManager:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    def __init__(self):
        pass
    """
    @brief - Load Json file and return List / Create new json file
    """
    def load_file(self,fileName):
        file_path = os.path.join(self.script_dir, fileName)
        if not os.path.exists(file_path):
            with open(file_path,"w") as file:
                return []
        try:
            with open(file_path,"r") as file:
                parsed_data = json.load(file)
                PRODUCT_MAPPING = {
                        PhysicalProduct.__name__ : PhysicalProduct,
                        DigitalProduct.__name__ :  DigitalProduct
                }
                try:
                    return [
                        PRODUCT_MAPPING[item["product_type"]](
                        **{k: v for k,v in item.items() if k != "product_type"}
                        )
                        for item in parsed_data
                        ]
                        
                except TypeError:
                    return []
        except json.JSONDecodeError:
            with open(file_path,"w") as file:
                return []
                
    def save_inventory(self, inventory, fileName):
        #open the file and overwrite
        file_path = os.path.join(self.script_dir, fileName)
        with open(file_path,"w") as file:
                json.dump(inventory,file, indent=4)