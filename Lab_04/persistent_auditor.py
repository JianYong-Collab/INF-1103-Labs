
#Get Valid Input
def get_valid_input(input_type):
    while True:
        if input_type == "product":
            user_input = input("Enter Product Name: ")
        elif input_type == "quantity":
            user_input = input("Enter Quantity: ")

        if user_input == "quit":
            return "quit"

        if input_type == "product":
            if(any(char.isdigit() for char in user_input)):
                print("Please enter valid input")
                continue
            return user_input.replace(" ","")
        elif input_type == "quantity":
            try:
                user_input = int(user_input)
            except ValueError:
                print("Please enter valid input")
                continue

            if user_input < 0:
                print("Please enter valid input")
                continue

            return user_input

def process_delivery(current_total, new_value):
     return current_total + new_value

def calculate_tax(amount):
     return 0.10 * amount

def generate_report(total_units, failed_attempts):
     print("\n--- Final Report ---")
     print("Total Deliveries Processed:",total_units)
     print("Number of Failed/Rejected Entries:",failed_attempts)

def load_inventory():
    try:
        with open("inventory.txt","r") as file:
            lines = file.read().splitlines()

            if not lines:
                return [],0
            
            *transaction_history, total_inventory = lines
            print("Current Orders:\n")
            for transaction in transaction_history:
                print(transaction)
            return transaction_history, total_inventory
    except FileNotFoundError:
        with open("inventory.txt","w") as file:
            transaction_history = []
            total_inventory = 0
            return transaction_history, total_inventory
def save_inventory(transaction_history, total_inventory):
    with open("inventory.txt","w") as file:
        file.write(transaction_history+total_inventory)
    print("Order successfully saved to orders.txt")
    pass

#Check for Existing Data
transaction_history, total_inventory = load_inventory()
total_inventory = int(total_inventory)
#Store data in transactions
transactions_sorted = []
for transaction in transaction_history:
    transactions_sorted.append(transaction.split(', '))

user_input = ""
no_of_deliveries = 0

while(True):
    product_input = get_valid_input("product")
    if(product_input == "quit"):
        save_inventory("\n".join(transaction_history),
                       "\n"+str(total_inventory))
        break
    quantity_input = get_valid_input("quantity")
    if(quantity_input == "quit"):
        save_inventory("\n".join(transaction_history),
                                 "\n"+str(total_inventory))
        break

    print("New Order Added:")
    total_inventory += quantity_input
    if(len(transactions_sorted) <= 0):
        order_no = 1000
    else:
        order_no = int(transactions_sorted[-1][0]) + 1
    new_order = str(order_no)+", "+product_input+", "+str(quantity_input)
    print(new_order)

    transaction_history.append(new_order)
    transactions_sorted.append(new_order.split(', '))
    print(transactions_sorted)

    
      
