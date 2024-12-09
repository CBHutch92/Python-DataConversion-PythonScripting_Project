# Assignment 1
# Casey Hutchinson
# ITEC 3100
# Due by 09/01/2024

def user_name():
    # Part A
    # Asks the user to enter this name and stores it in variable "n" (step 1)
    global n    # I made "n" a global variable so I could call it in multiple functions (I learned about global in a previous class and verified its use on tutorialspoint)
    n = input("Please enter your first and last name: ")   # (step 2)

def tuition_info():
    # Part B
    # Greet user with the name entered for Part A that is stored in the "n" variable (step 1)
    print(f"Welcome to MGA, {n}! We're excited for you to join us.")

    # Creating a while loop that starts by asking the user to input the number of credit hours they're registered for and stores it in the variable "hrs" (step 2)
    while True:
        hrs = int(input("How many credit-hours are you registered for this semester? Please enter a numeric value (no decimals) as the total number of hours here: "))      # (step 3)
    
        # This requires the user to input any number greater than 3 since 3 credit hours is the lowest a single standalone class can be
        if hrs == 0:
            print("Please enter a number above 0.")

        # This section calculates in-state tuition, displays the additional fees that are stored in a tuple, displays the in-state tuition total, and then displays the total cost of tuition + additional fees
        else:
            print("\n")
            print("Thank you for that information.")
            adtl_fees = (45, 45, 20, 10, 180, 46)   # tuple that stores additional fees information
            rate = 174  # in-state tuition rate of $174 per credit hour
            tuition = hrs * rate    # calculates total in-state tuition by multiplying the hrs variable (int input from user) by the rate variable and stores it in the tuition variable (step 4)

            print("We will add your tuition total to the following additional fees:") # displays a list of what each additional fee and the amount of each fee (step 5)
            print("The activity fee is", adtl_fees[0],"dollars")
            print("The athletic fee is", adtl_fees[1],"dollars")
            print("The health fee is", adtl_fees[2],"dollars")
            print("The parking fee is", adtl_fees[3],"dollars")
            print("The rec and wellness fee is", adtl_fees[4],"dollars")
            print("And the technology fee is", adtl_fees[5],"dollars")
            print("\n")
            print(f"If you are registered for {hrs} credit hours, your total in-state tuition cost will be ${tuition}. MGA's in-state tuition rate is ${rate} per credit hour.") # displays the total cost of in-state tuition that is stored in the "tuition" variable (step 6)
            total_tuition = tuition + adtl_fees[0] + adtl_fees[1] + adtl_fees[2] + adtl_fees[3] + adtl_fees[4] + adtl_fees[5] # creates a new variable that adds the value in the "tuition" variable to the values stored in the tuple
            print("\n")
            print(f"The total cost of your in-state tuition + the additional fees is ${total_tuition}.") # displays the total cost of in-state tuition + additional fees that is stored in the total_tuition variable (step 7)
            # all outputs are labeled so that the user knows exactly what is being displayed (step 8)

        break

def subway_order():
    # Part C
    # Greet user with the name entered for Part A that is stored in the "n" variable (step 1)
    print("\n")
    print(f"Hello {n}! We have a couple more questions for you.")

    subway = [(float(input("What is the cost of your favorite Subway sandwich? (Please do not enter a dollar sign value - numeric digits only): ")))] # Asks user to input cost of favorite Subway sandwich and stores it in the list "Subway" (step 2)
    subway.append(float(input("What is the cost of your favorite chips? (Please do not enter a dollar sign value - numeric digits only): ")))    # Asks user to input cost of favorite chips and appends it to the Subway list (step 3)
    subway.append(float(input("What is the cost of your favorite cookie? (Please do not enter a dollar sign value - numeric digits only): ")))   # Asks user to input cost of favorite cookie and appends it to the Subway list (step 4)
    subway.append(float(input("What is the cost of your favorite drink? (Please do not enter a dollar sign value - numeric digits only): ")))    # Asks user to input cost of favorite drink and appends it to the Subway list (step 5)
    # input prompts are clear so that the user knows exactly what they are inputing the cost for and asks user not to use a dollar sign (step 6)
    subway_cost = subway[0] + subway[1] + subway[2] + subway[3]     # this variable calculates the total cost of the users Subway order before tax
    food_tax = 0.05
    tax = subway_cost * food_tax    # this variable calculates the total sales tax (multiplies the cost of the users order by the 5% food sales tax)
    total_cost = subway_cost + tax      # this variable calculates the final total of the users Subway order including sales tax
    print(f"The total cost of your Subway order is ${round(total_cost, 2)}.")       # displays the total cost of the users Subway order and rounds it to 2 decimal places (I have used this variable in the past and verified its use on Programiz) (step 8)

def main():
    user_name()
    tuition_info()
    subway_order()

if __name__ == "__main__":
    main()