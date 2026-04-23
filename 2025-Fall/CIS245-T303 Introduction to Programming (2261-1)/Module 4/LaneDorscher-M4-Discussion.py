
# Metric Converter: Gallons to Liters
# Program will continually run until user decides to exit by typing 'exit' or 'quit'
# Includes error handling for non-numeric input


GAL_TO_LITER_METIC = 3.78541178 # Conversion factor from gallons to liters
EXIT_PHRASE = ['exit', 'quit', 'q'] # List of phrases that will exit the program

def main():
    print_welcome()

    while True:
        try:
            exit_flag, gallons = get_user_input()

            if exit_flag:
                raise SystemExit("Exiting the Metric Converter. Goodbye!")
            if gallons is None:
                continue
            
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is approximately {liters:.3f} liters.\n")
        except SystemExit as e:
            print(e)
            break


## Gets user input and validates it
## Returns a tuple (exit_flag, gallons)
def get_user_input() -> (bool | float):  
    user_input = input("Enter gallons to convert to liters (or type 'exit' to quit): ").strip().lower()

    if user_input in EXIT_PHRASE:
        return True, 0.0  # Indicate exit

    try:
        gallons = float(user_input)
        gallons = math_abs(gallons)  # Ensure non-negative input
        
        return False, gallons
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'exit' to quit.\n")
        return False, None


def print_welcome():
    message = ("\nWelcome to Metric Converter: Gallons to Liters"
        + f"\n For reference: 1 Gallon = {GAL_TO_LITER_METIC} Liters\n")
    
    print(message)

def gallons_to_liters(gallons: float) -> float:
    liters = gallons * GAL_TO_LITER_METIC
    return liters

def liters_to_gallons(liters: float) -> float:
    gallons = liters / GAL_TO_LITER_METIC
    return gallons

def math_abs(number : float) -> float:
    if number < 0:
        return -number
    return number

if __name__ == "__main__":
    main()