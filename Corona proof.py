# We will start by asking the user for the number of guests which will be invited
guests = int(input("How many guests would you like to invite for your birthday party?"))
# We define the variable "guestnumber" with a value of 0 so we can use this later on in the code
guestnumber = 0
# If the number of guests which will be invited is lower than 7, we will ask for the names of the guests
if guests < 7:
    for i in range(guests):
        guestnumber += 1
        print("What is the name of guest number", guestnumber, 'you would like to invite?')
        name = str(input())
        print(name, "has been invited!")
# if the number of guests which will be invited is higher than 7 we will inform the user that this not corona proof
else:
    print('Inviting more than 6 guests is not corona proof, please reconsider the amount of guests')
