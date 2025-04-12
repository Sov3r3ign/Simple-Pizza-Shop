# The owner of the pizza shop has asked you to write a
# script that allows a customer to calculate the cost of a pizza. He has asked you to make the
#following options available to the customer:
#• Pizza base (Customer must choose 1): Thick (R 10) or Thin (R 5)
#• Pizza size (Customer must choose 1): Small (R 30), Medium (R 40) or Large (R 50)
#• Basic sauce (Customer must choose 1): Tomato (R 5) or Barbecue (R 10)
#• Toppings (Customer may choose any or none): Cheese (R 5), Mushrooms (R 3),
#  Avocado (R 7), Pineapple (R 5), Bacon (R 7), Chicken (R 7) or Fish (R 6).
#If a specific item is selected display the item and its price on the screen. At the bottom (the
#last line) of the display present the customer with the total of the purchase.
from contextlib import nullcontext

print("Hello Customer! How may we help you today.")

base = "Thick, Thin"
size = "Small, Medium,Large"
sauce = "Tomato,Barbecue"
toppings = "None , Cheese, Mushrooms, Avocado, Pineapple, Bacon, Chicken, Fish (R 6)"

base_choice = input(f"How would you like to structure your pizza the base: {base}\n - ")

if base_choice == "Thick":
    print("Thick (R 10)")
    base_price = 10
else:
    print("Thick (R 5)")
    base_price = 5
print()

size_choice = input(f"What about the size of the pizza: {size}\n -  ")
if size_choice == "Small":
    print("Small (R 30)")
    size_price = 30
else:
    if size_choice == "Medium":
     print("Medium (R 40)")
     size_price = 40
    else:
      print("Large (R50)")
      size_price = 50
print()

sauce_choice = input(f"Which sauce would you like on your pizza: {sauce}\n - ")
if sauce_choice == "Tomato":
    print("Tomato (R 5)")
    sauce_price = 5
else:
    print("Barbecue (R 10)")
    sauce_price = 10
print()

toppings_choice = input(f"Which toppings would you like on top of that Customer: {toppings}\n - ")
if toppings_choice == "Cheese":
    print("Cheese (R 5)")
    topping_price = 5
elif toppings_choice == "Mushrooms":
    print("Mushrooms (R 3)")
    topping_price = 3
elif toppings_choice == "Avocado":
    print("Avocado (R 7)")
    topping_price = 7
elif toppings_choice == "Pineapple":
    print("Pineapple (R 5)")
    topping_price = 5
elif toppings_choice == "Bacon":
    print("Bacon (R 7)")
    topping_price = 7
elif toppings_choice == "Chicken":
    print("Chicken (R 7)")
    topping_price = 7
elif toppings_choice == "Fish":
    print("Fish (R 6)")
    topping_price = 5
elif toppings_choice == "None":
    print("No choice made")
    topping_price = 0
else:
    print("We do have that topping here.")
    topping_price = nullcontext


totalPurchase = base_price +size_price + sauce_price + topping_price
print(f"The total purchase price is {totalPurchase}")