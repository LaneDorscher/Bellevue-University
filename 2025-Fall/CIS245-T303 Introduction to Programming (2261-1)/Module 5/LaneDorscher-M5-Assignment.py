## Author: Lane Dorscher
## Date: 10/12/2025

def print_welcome():
    print("Welcome to the File Processing Program!\n")

def get_user_input(prompt: str) -> str:
    return input(prompt)

def validate_phone_number(phone_str: str) -> bool:
    # Phone format should be 999-999-9999
    if len(phone_str) != 12:
        return False

    parts = phone_str.split("-")
    if len(parts) != 3:
        return False

    expected_lengths = [3, 3, 4]
    for i, num_str in enumerate(parts):
        if len(num_str) != expected_lengths[i]:
            return False
        if not num_str.isnumeric():
            return False

    return True

def get_phone_number() -> str:
    while True:
        phone = get_user_input("Enter user's phone number (formatted as 999-999-9999): ")
        if validate_phone_number(phone):
            return phone
        else:
            print("Phone number is not valid. Try again!\n")

def write_to_file(file_name: str, name: str, address: str, phone: str):
    with open(file_name, "a") as file:
        file.write(f"{name},{address},{phone}\n")

def read_and_display_file(file_name: str):
    print("\nFile contents:\n----------------")
    with open(file_name, "r") as file:
        for line in file:
            print(line.strip())

def main():
    print_welcome()

    file_name = get_user_input("Enter the designated file name: ")
    user_name = get_user_input("Enter your name: ")
    street_address = get_user_input("Enter your address: ")
    phone_number = get_phone_number()

    write_to_file(file_name, user_name, street_address, phone_number)
    read_and_display_file(file_name)

if __name__ == "__main__":
    main()
