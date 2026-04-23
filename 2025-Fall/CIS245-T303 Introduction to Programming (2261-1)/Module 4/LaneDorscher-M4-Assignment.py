# Author: Lane Dorscher
# Date Created: 10/2/2025

# Metric Converter: Miles to Kilometers
# Program will continually run until user decides to exit by typing 'exit' or 'quit'
# Includes error handling for non-numeric input
# Negative inputs are converted to positive values


MILES_TO_KM_METIC = 1.609344  # 1 mile = 1.609344 kilometers
EXIT_PHRASE = ['exit', 'quit', 'q'] # List of phrases that will exit the program

def main():
    print_welcome()

    while True:
        try:
            exit_flag, miles = get_user_input()

            if exit_flag:
                raise SystemExit("Exiting the Metric Converter. Goodbye!")
            if miles is None:
                continue
            
            km = convert_miles_to_km(miles)
            print(f"{miles} miles is approximately {km:.2f} kilometers.\n")
        except SystemExit as e:
            print(e)
            break

def print_welcome():
    print("\nWelcome to Metric Converter: Miles to Kilometers")
    print(f" For reference: 1 Mile = {MILES_TO_KM_METIC} Kilometers\n")

def get_user_input() -> (bool | float):  
    user_input = input("How many miles did you drive? (or type 'exit' to quit): ").strip().lower()

    if user_input in EXIT_PHRASE:
        return True, 0.0  # Indicate exit

    try:
        miles = float(user_input)
        miles = math_abs(miles)  # Ensure non-negative input
        
        return False, miles
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'exit' to quit.\n")
        return False, None

def convert_miles_to_km(miles: float) -> float:
    km = miles * MILES_TO_KM_METIC
    return km

def convert_km_to_miles(km: float) -> float:
    miles = km / MILES_TO_KM_METIC
    return miles

def math_abs(number : float) -> float:
    if number < 0:
        return -number
    return number

if (__name__ == "__main__"):
    main()