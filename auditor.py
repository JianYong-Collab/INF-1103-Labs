# Initialize Inventory to 0
inventory = 0
user_input = ""
failed_entries = 0

while(True):
    user_input = input("Enter the new stock changes: ")
    if(user_input == "quit"):
        break
    if(not user_input.isdigit()):
        failed_entries += 1
        continue
    elif (int(user_input) < 0):
        failed_entries += 1
        continue
    else:
        inventory += int(user_input)
        print("Inventory stock is now:",inventory)
    if(inventory > 500):
        print("Overstock Alert!!!")
        break
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)