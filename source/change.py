import sys

# 1. Get inputs from user 
cost_of_item = float(input("What is the total cost: "))
money_from_user = float(input("Give the exact amount or more for this cost: "))


# 2. Check if they make sense 
if cost_of_item < 0 or money_from_user < 0:
    sys.exit("The cost or the given amount of money is negative")

# 3. Calculate the total change and print
change = money_from_user - cost_of_item 
if change < 0:
    sys.exit("The amount you gave is too lillte")



# 4. Find the correct bills/coins to give for change TODO

# 4.1 Figure out correct bills
bills = [100, 50, 20, 10, 5]
# TODO 

# 4.2 Figure out correct coins
coins = [2, 1, 0.25, 0.10, 0.05, 0.01]
# TODO