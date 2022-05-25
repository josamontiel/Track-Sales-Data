stock = # Enter total stock amount
jeans_sold = # Enter amount of items sold
target = # Sales target

target_hit = jeans_sold == target
print("Hit jeans sale target: ")
print(target_hit)

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock:")
print(in_stock)
