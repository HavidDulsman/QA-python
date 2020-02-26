#!/user/bin/env python3.8

capacity = int(0)
while capacity <= 100:
    amount = int(input("How many tickets do you want? "))
    if amount > 10:
        print("thats too many! pick again")
    else:
        capacity = capacity + amount
        print("there are " + str(100 - capacity))
print("the capacity is now full!")