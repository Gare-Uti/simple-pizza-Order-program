#An exercise on writing a pizza ordering program
#defining the variables

available_pizzas = ['pepperoni', 'vegetarian', '4cheese']
available_toppings = ['mushroom', 'pineapple', 'green pepper']
pizza_prices = {'pepperoni': 8.65, 'vegetarian': 4.25, '4cheese': 3.17}
topping_prices = {'mushroom': 1.0, 'pineapple': 2.50, 'green pepper': 1.15}
sub_total = []
final_order = {}

#making the order

print("Hello, welcome to 'ANONYMOUS-PIZZA' online ordering system")
order_pizza = True
while order_pizza:
    print("Please select a pizza from the menu: ")
    print()
    for pizzas in available_pizzas:
        print(pizzas)
        print()
    while True:
        chosen_pizza = input('Which pizza would you love to order? ')
        if chosen_pizza in available_pizzas:
            print(f"You have ordered a {chosen_pizza}.")
            sub_total.append(pizza_prices[chosen_pizza])
            break
        if chosen_pizza not in available_pizzas:
            print(f"Sorry, we currently do not have {chosen_pizza}.")

#Requesting for extra toppings.

order_toppings = True
print('This is the list of available extra toppings: ')
for toppings in available_toppings:
    print(toppings)
    print()
while order_toppings:
    extra_topping = input('Would you like an extra topping? yes or no?')
    if extra_topping == "yes":
        chosen_topping = input("Which one would you like to add? ")
        if chosen_topping in available_toppings:
            final_order.setdefault(chosen_pizza, [])
            print(f"You have added{chosen_topping}.")
            sub_total.append(topping_prices[chosen_topping])
        else:
            print(f"Sorry, we don't have{chosen_topping}.")

    elif extra_topping == "no":
        break

#finalizing the order
print(f"You have ordered for a {chosen_pizza}")
print(f"Your total order price is: ${sum(sub_total)}CAD")
print(f"Thank you for choosing ANONYMOUS PIZZA!")
