import pandas as pd

# Initialize inventory as a pandas DataFrame
inventory_data = {
    'Item': ['Rice', 'Lentils', 'Spices', 'Cooking Oil', 'Sugar'],
    'Quantity': [50, 40, 30, 20, 60],  # Initial stock
    'Price': [50, 80, 120, 200, 45]  # Price per unit
}
inventory = pd.DataFrame(inventory_data)

# Function to update inventory after a sale
def update_inventory(item_name, quantity_sold):
    global inventory
    if item_name in inventory['Item'].values:
        idx = inventory[inventory['Item'] == item_name].index[0]
        if inventory.at[idx, 'Quantity'] >= quantity_sold:
            inventory.at[idx, 'Quantity'] -= quantity_sold
            print(f"Updated inventory: {item_name} reduced by {quantity_sold}. Remaining: {inventory.at[idx, 'Quantity']}")
        else:
            print(f"Not enough stock for {item_name}. Available: {inventory.at[idx, 'Quantity']}")
    else:
        print(f"{item_name} not found in inventory.")

# Function to generate a bill for a customer
def generate_bill(items, quantities):
    total = 0
    bill_details = []
    
    for item, qty in zip(items, quantities):
        if item in inventory['Item'].values:
            idx = inventory[inventory['Item'] == item].index[0]
            if inventory.at[idx, 'Quantity'] >= qty:
                cost = inventory.at[idx, 'Price'] * qty
                total += cost
                bill_details.append(f"{item}: {qty} x ₹{inventory.at[idx, 'Price']} = ₹{cost}")
                update_inventory(item, qty)
            else:
                bill_details.append(f"{item}: Not enough stock.")
        else:
            bill_details.append(f"{item}: Item not available.")
    
    print("\n--- Customer Bill ---")
    for detail in bill_details:
        print(detail)
    print(f"Total Amount: ₹{total}")
    print("----------------------")

# Function to check for low stock alerts
def low_stock_alert(threshold=20):
    low_stock_items = inventory[inventory['Quantity'] < threshold]
    if not low_stock_items.empty:
        print("\n*** Low Stock Alert ***")
        print(low_stock_items[['Item', 'Quantity']])
    else:
        print("\nAll items are sufficiently stocked.")

# Example usage
print("Initial Inventory:\n", inventory)
generate_bill(['Rice', 'Lentils'], [5, 10])  # Example sale
low_stock_alert()  # Check for low stock