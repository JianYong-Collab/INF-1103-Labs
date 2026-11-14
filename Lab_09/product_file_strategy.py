from abc import ABC, abstractmethod
import json
import csv
from inventory_manager import Inventory
from supplier import Supplier
from product_factory import ProductFactory
class ProductFileStrategy(ABC):
    @abstractmethod
    def load_products(self, file_path: str, inventory: Inventory, supplier: Supplier):
        pass
    
    @abstractmethod
    def save_file(self, file_path: str, inventory: Inventory):
        pass

class CSVProductFileStrategy(ProductFileStrategy):
    extension = ".csv"
    def load_products(self, file_path: str, inventory: Inventory, supplier: Supplier):
        if not file_path.endswith((".json", ".csv")):
            file_path += self.extension
        try:
            file = open(file_path, newline="")
            print(f"{file_path} found.")
        except FileNotFoundError:
            print(f"Products file not found: {file_path}")
        else:
            with file:
                    reader = csv.reader(file)
                    header = next(reader, None)
                    if not header:
                        print("CSV file is empty.")
                    loaded = 0

                    for row in reader:
                       
                            if len(row) < 5:
                                continue

                            p_type, p_id, p_name, price, stock, = row[:5]
                            try:
                                price = float(price)
                                if price < 0:
                                    continue

                                stock = int(stock)
                                if stock < 0: 
                                    continue
                                
                                product = ProductFactory.create(p_type, p_id, p_name, price, stock, supplier=supplier)
                                inventory.add_product(product)
                                loaded += 1
                            except (ValueError, TypeError):
                                print("Error")
        finally:
            print("Load attempt finished.")

    def save_file(self, file_path: str, inventory: Inventory):
            if not file_path.endswith((".json", ".csv")):
                file_path += self.extension
            try:
                with open(file_path, "w", newline="") as file:
                    writer = csv.writer(file)
                    
                    # Write the header row to match your CSV loader layout
                    writer.writerow(["product_type", "product_id", "name", "price", "stock"])
                    
                    # Write each product's row data
                    for product in inventory.inventory:
                        writer.writerow([
                            product.product_type,
                            product.id,
                            product.name,
                            product.price,
                            product.stock
                        ])
                        
                print(f"Successfully saved inventory to {file_path}")
            except IOError as e:
                print(f"Failed to save CSV file {file_path}: {e}")
            except AttributeError as e:
                print(f"Error accessing product attributes: {e}")

class JSONProductFileStrategy(ProductFileStrategy):
    extension = ".json"
    def load_products(self, file_path: str, inventory: Inventory, supplier: Supplier):
        if not file_path.endswith((".json", ".csv")):
            file_path += self.extension
        try:
            file = open(file_path)
            print(f"{file_path} found.")
        except FileNotFoundError:
            print(f"Products file not found: {file_path}")
        else:
            with file:
                try:
                    parsed_data = json.load(file)
                    loaded = 0
                    try:
                        for item in parsed_data:
                            kwargs = {
                                k : v for k, v in item.items()
                            }
                            kwargs["supplier"] = supplier
                            
                            product_instance = ProductFactory.create(**kwargs)
                            inventory.add_product(product_instance)
                            loaded += 1          
                        print(f"{loaded} products loaded.")
                    except (ValueError, TypeError):
                        print("Type / Value Error")
                except (json.JSONDecodeError):
                    print("Invalid JSON format")
        finally:
            print("Load attempt Finished")

    def save_file(self, file_path: str,  inventory: Inventory):
        if not file_path.endswith((".json", ".csv")):
            file_path += self.extension
        try:
            inventory_dict = [product.to_dict() for product in inventory.inventory]
            with open(file_path,"w") as file:
                    json.dump(inventory_dict, file, indent=4)
            print(f"Successfully saved inventory to {file_path}")
        except IOError as e:
            print(f"Failed to save file {file_path}: {e}")
        except AttributeError as e:
            print(f"Error serializing products (ensure to_dict() is implemented): {e}")