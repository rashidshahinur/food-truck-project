# Creating our menu with correct format
def print_menu(menu):
	for name, price in menu.items(): # for each key value pair in the menu dict, print it out.
		print(name, ': $', format(price, '.2f'), sep='')


def get_order(menu): # We need to pass the menu to add the item to order
	orders = []
	order = input("What would you like to order? (Q to quit)")
	while (order.upper() != 'Q'):
		# find the order
		found = menu.get(order)
		# Check if the order is in the menu, if true then insert it into the orders list
		if found:
			orders.append(order)
			# Let the customer know that we're out of pork
			if order == 'Pork':
				print("Sorry we're out of this item")
				orders.remove('Pork')
		else:
			print("Menu item doesn't exist")
		
		order = input("Anything else? (Q to quit)")
	
	return orders

# This function use both menu and order as parameters, otherwise will get a name-undefined error.
def calculate_total(menu,order):
	# Calculate and print the final total price of the order
	subtotal = 0
	i = 0
	print("Here is your order summary: ")
	
	# Go through each item in the order list and get the associated price from the menu dict
	while i < len(order):
		price = menu.get(order[i])
		print(order[i], "\t", "\t$", price, sep='')
		subtotal = subtotal + price
		i += 1
	
	# Print the final subtotal and total
	print("Subtotal: \t", "$", subtotal, sep='')
	tax = 0.0475
	total = subtotal + tax * subtotal
	print("Total after tax: $",format(total,'.2f'), sep='')

# Set up the app interface
def main():
	print('***=====================***' + '\nWelcome to Banh Mi Sai Gon!' + '\n***=====================***')
	menu = {'Chicken': 5.0, 'Steak': 6.0, 'Pork': 5.5, 'Tofu': 4.0, 'Combinations': 7.0}
	print_menu(menu)
	print()
	order = get_order(menu)
	print()
	print("You ordered: ", order)
	print()
	calculate_total(menu,order)
	print('Thank you! See you again!')
main()