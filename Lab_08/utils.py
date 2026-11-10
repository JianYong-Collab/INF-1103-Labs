from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier
#Note This cannot check for negative numbers
def is_number(string_to_check):
    try:
        float(string_to_check)
        return True
    except (ValueError, TypeError):
        return False

# Handle all cases of valid input
# Strings && Integers only
def get_valid_input(input_prompt,input_type):
    user_input = ""
    while True:
        user_input = input(f"{input_prompt}")
        #handle all string input types and integer inputs
        if(input_type == "string" and user_input.isdigit() == True):
            continue

        if(input_type == "number" and is_number(user_input) == False):
            continue

        return user_input

def convert_js_to_products(parsed_data: list):
    PRODUCT_MAPPING = {
        PhysicalProduct.__name__ : PhysicalProduct,
        DigitalProduct.__name__ :  DigitalProduct
    }
    try:
        products = []
        for item in parsed_data:
            product_type = item["product_type"]
            if product_type not in PRODUCT_MAPPING:
                continue

            supplier = Supplier(
                supplier_id = item.get("supplier_id"),
                name = item.get("supplier_name"),
                contact_email= item.get("supplier_email")
            )

            kwargs = {
                k : v for k, v in item.items()
                if k not in ["product_type", "supplier_id", "supplier_name", "supplier_email"]
            }
            kwargs["supplier"] = supplier

            product_instance = PRODUCT_MAPPING[product_type](**kwargs)
            products.append(product_instance)

        return products
            
    except TypeError, KeyError:
        return []