# Initialize Inventory to 0
inventory = 0
user_input = ""
failed_entries = 0

while(True):
    user_input = input("Enter the new stock changes: ")
    if(user_input == "quit"):
        break
    try:
        user_input = int(user_input)
    except ValueError:
        failed_entries += 1
        print("Please enter proper input")
        continue
    #Check if Negative Number
    if ( user_input < 0):
        failed_entries += 1
        print("Negative number are not accepted")
        continue
    else:
        inventory += user_input
        if(inventory >= 500):
                inventory = 500
                print("Overstock Alert!!!")
                print("Inventory stock is now:",inventory)
                break
        print("Inventory stock is now:",inventory)
    
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)