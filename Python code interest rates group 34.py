# We start by asking for the name of the user
name = input("Hi! May I know your name?")

# Secondly we ask for the reason of the loan request and make sure that the user gives the right input by stating how the input should be given and warning the user when this is not done in the correct manner
while True:
    try:
        reason = input(
            "Nice to meet you " + name + " for a student loan request type 'student loan' for a home mortgage loan type 'mortgage loan' for a car loan type 'car loan' ")
        if reason == "student loan" or reason == "mortgage loan" or reason == "car loan":
            print("Thank you for selecting", reason)
            break
        else:
            print("Sorry, but please insert one of the specific options given to this question")
    except:
        continue

# We continue by asking the user for the interest rate, the number of years for the loan and the amount of the loan
# In case the input is not given in the correct manner, we inform the user about the correct way of giving input


def inter():
    global interest, years, amount
    while True:
        try:

            interest, years, amount = map(float, input(
                "Please state the annual interest rate, the number of years for the loan and the amount of the loan").split())

        except ValueError:
            print(
                "Please make sure to only insert digits, keep space(s) between every answer and use dots for decimals")

            continue
        else:
            break

    return interest, years, amount


interest, years, amount = map(float, inter())
# The monthly interest is calculated by dividing the annual interest by 12
monint = interest / 12 / 100
# The monthly payment is calculated by the given formula
monpay = (amount * monint) / (1 - (1 / ((1 + monint) ** (years * 12))))
# The total payment is calculated by multiplying the monthly payment by 12 and multiplying the outcome of this calculation by the amount of years for the loan
totpay = monpay * 12 * years
# Finally we inform the user about the monthly and annual payment based on their requirements
print("Based on your requirements, the monthly payment will be", round(monpay, 2), "and the total payment will be",
      round(totpay, 2))
