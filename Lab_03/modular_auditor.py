# Initialize Inventory to 0
inventory = 0
user_input = ""
failed_entries = 0
no_of_deliveries = 0
#Get Valid Input
def get_valid_input():
    while True:
     user_input = input("Enter the new stock changes: ")
     if(user_input == "quit"):
          return "quit"

     try:
        user_input = int(user_input)
     except ValueError:
        return "Invalid"

     if(user_input < 0):
         return "Invalid"

     return user_input

def process_delivery(current_total, new_value):
     return current_total + new_value

def calculate_tax(amount):
     return 0.10 * amount

def generate_report(total_units, failed_attempts):
     print("\n--- Final Report ---")
     print("Total Deliveries Processed:",total_units)
     print("Number of Failed/Rejected Entries:",failed_attempts)



while(True):
    user_input = get_valid_input()
    if(user_input == "quit"):
        generate_report(no_of_deliveries,failed_entries)
        break
    if(user_input == "Invalid"):
        failed_entries += 1
        print("Please Enter Valid Input!!!")
        continue

    #Calculate Tax
    tax = calculate_tax(user_input)
    inventory = min(process_delivery(inventory, user_input-tax),500)
    print("Inventory Stock is now:", inventory)
    no_of_deliveries += 1
    if(inventory == 500):
        print("Inventory Overstocked!!!")
        generate_report(no_of_deliveries,failed_entries)
        break