print("-------MENU-------")
items={"popcorn": 5.00,
       "samosa": 10.00,
       "coke": 10.00,
       "pepsi":10.00,
       "redbull":20.00}
for item,price in items.items():
    print(f"{item:10}:{price}")
print("------------------\n")
orders=[]
t_price=0
while(True):
    order=input("enter your order (press q to quit): ").lower()
    if order == 'q':
        break
    elif items.get(order) is not None: 
        qty=int(input("enter the quantity: "))
        orders.append([order,qty])
    else:
        print("Sorry, it's not on our menu ^_^")
print("your orders: ",orders)
for o in orders:
    price=o[1]*items[o[0]]
    print(f"{o[0]} ${price}")
    t_price+=price
print(f"total price: ${t_price}")




 
