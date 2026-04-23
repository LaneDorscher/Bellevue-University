## Author: Lane Dorscher
## Date: 09/20/2025
## Description: This program calculates the cost of fiber optic cable installation based on user input. 
##              The cost per foot varies depending on the total feet ordered allowing the user to save money when ordering in bulk.

# Constants and Variables
COMPANY_NAME = "FibreTech"
WELCOME_MSG = "Welcome to " + COMPANY_NAME + "\'s Fiber Optic Cost Calculator!"
FEET_MESSAGE = "Feet of Fiber: "

## Functions
def getFloatInput(str):
    num = 0.0
    while True:
        try:
            num = float(input(str))
            return num
        except ValueError:
            print("Invalid input! Must be a number!\n")

def getCostPerFt(feet):
    cost = 0.87
    if (feet >= 500.0):
        cost = 0.50
    elif (feet >= 250.0):
        cost = 0.70
    elif (feet >= 100.0):
        cost = 0.80
    else:
        cost = 0.87
    return cost




## Main Code

def main():
    print(WELCOME_MSG)
    feet = getFloatInput(FEET_MESSAGE)
    costPerFt = getCostPerFt(feet)
    totalCost = feet * costPerFt
    print(f"The cost per foot is: ${costPerFt:.2f}")
    print(f"The total cost for {feet} feet of fiber optics is: ${totalCost:.2f}")

if (__name__ == "__main__"):
    main()



