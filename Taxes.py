# We start by asking the user for the gross salary and store the input as the variable "salary"
salary = float(input("Please state your gross salary"))
# When the salary is greater than 50000, we calculate the net income by multiplying with 0.5
if salary > float(50000):
    net = salary * float(0.5)
# When the salary is smaller than 50000, but greater than 25000, we calculate the net income by multiplying with 0.75
elif salary > float(25000):
    net = salary * float(0.75)
# When the salary is smaller than 25000, but greater than 10000, we calculate the net income by multiplying with 0.9
elif salary > float(10000):
    net = salary * float(0.9)
# When the salary is smaller than 10000, the gross salary is the same as the net income
else:
    net = salary
# Lastly we return the gross salary and the net income
print("Your gross salary is", salary, "Your net income is", net)
