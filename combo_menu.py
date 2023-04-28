print("Welcome to the Combo Menu!")

# Menu items and prices
items = {"chicken": 5.99, "tofu": 4.99, "beef": 6.99}
beverages = {"small": 1.99, "medium": 2.99, "large": 3.99}
fries = {"small": 1.99, "medium": 2.99, "large": 3.99}
ketchup_packet_price = 0.25

# Ask user for order
item_choice = input("What would you like for your main item? (chicken/tofu/beef) ")
beverage_choice = input("What size beverage would you like? (small/medium/large) ")
fries_choice = input("What size fries would you like? (small/medium/large) ")
ketchup_packet = input("Would you like a ketchup packet? (y/n) ")

# Calculate order total
item_price = items[item_choice]
beverage_price = beverages[beverage_choice]
fries_price = fries[fries_choice]
ketchup_packet_price_total = ketchup_packet_price if ketchup_packet.lower() == "y" else 0

total_price = item_price + beverage_price + fries_price + ketchup_packet_price_total

# Display order summary and total price
print("Your order summary:")
print("- Main item: {} (${:.2f})".format(item_choice, item_price))
print("- Beverage: {} (${:.2f})".format(beverage_choice, beverage_price))
print("- Fries: {} (${:.2f})".format(fries_choice, fries_price))
if ketchup_packet_price_total > 0:
    print("- Ketchup packet: ${:.2f}".format(ketchup_packet_price_total))
print("Total price: ${:.2f}".format(total_price))

