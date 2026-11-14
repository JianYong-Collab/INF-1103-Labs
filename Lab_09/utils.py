from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

# Handle all cases of valid input
# Strings && Integers only
def get_valid_input(input_prompt,input_type):
    user_input = ""
    while True:
        user_input = input(f"{input_prompt}")
        #handle all string input types and integer inputs
        if(input_type == "string" and user_input.isdigit() == True):
            continue

        if(input_type == "number"):
            try:
                value = float(user_input)
                if value <= 0:
                    print("Please enter a number greater than zero.")
                    continue
                return value
            except ValueError:
                print("Please enter a valid number, e.g. 12.50")
                continue

        return user_input #only if its a str
