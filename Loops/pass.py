for i in range(1,11):
    if i==5:
        pass #literaaly does nothing. but it's a placeholder for future needed logic
    print(i)

# Sometimes, when using conditional statements we may not want to perform any action 
# for a condition but still need the block to exist. 
# The pass statement ensures the code remains valid without adding logic.


x = 10
if x > 5:
    pass  # Placeholder for future logic
else:
    print("x is 5 or less")

# Explanation:

# When x > 5, the pass statement runs, so nothing happens.
# If x <= 5, else block executes and prints the message.

