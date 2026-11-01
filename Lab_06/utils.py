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

        if(input_type == "integer" and is_number(user_input) == False):
            continue

        return user_input