restaurant_reservation={'Alice':15, 'Bob':17,"Carol": 19}
conflictiing_reservation = {'Alice': 15, 'Bob':17}
customer_name = input("Enter the customer's name: ")
while  True:
    time =int(input("Enter the time of reservation between (0 and 23): "))
    if time >=0 and time <=23:
        break
    else:
        print("Invalid time, please enter a value between 0 and 23")
restaurant_reservation[customer_name] = time
print(restaurant_reservation)
print(conflictiing_reservation)