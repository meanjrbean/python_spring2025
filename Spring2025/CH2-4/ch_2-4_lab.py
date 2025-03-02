# This function accepts an error message as a string and prints it to the console.
def print_error(error_message):
    print("Invalid input: " + error_message)


# This function attempts to parse a string into an integer.
# Returns an integer if successful.
# Returns None if it fails.
def handle_integer_parsing(number):
    try:
        num = int(number)
        return num
    except ValueError:
        print_error("cannot convert to integer.")


# Function handles the validation before calculating.
# Returns True if validation passes.
# Returns False if validation fails.
def handle_calculation_validation(start, end):
    if start > end:
        print_error("starting number cannot be greater than the stop number.")
        return False

    return True


# Function handles checking user's input for a key to exit a loop.
# Returns True if "Y"
# Returns False if "N"
def user_choice_loop():
    loop = True
    while loop:
        user_input = input("Would you like to try again? (Y/N): ")
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "n":
            return False
        else:
            print_error("Enter either 'Y' or 'N'.")


# This function handles the calculations and printing of the columns and rows.
def handle_calculations(start, end):
    num_start = handle_integer_parsing(start)
    num_end = handle_integer_parsing(end)

    if num_start is None or num_end is None:
        return

    if handle_calculation_validation(num_start, num_end) is False:
        return

    # Column widths
    col1_width = 8
    col2_width = 8
    col3_width = 8

    print(f"{'Number'.ljust(col1_width)} {'Squared'.ljust(col2_width)} {'Cubed'.ljust(col3_width)}")
    print("-" * (col1_width + col2_width + col3_width + 2))

    for num in range(num_start, (num_end + 1)):
        squared = num ** 2
        cubed = num ** 3
        print(f"{str(num).ljust(col1_width)} {str(squared).ljust(col2_width)} {str(cubed).ljust(col3_width)}")

    print()


# This is the main function that we run the program with.
def main():
    loop = True
    print("Table of Powers")
    while loop:
        range_start = input("Enter a starting number: ")
        range_end = input("Enter a stop number: ")
        handle_calculations(range_start, range_end)
        loop = user_choice_loop()


if __name__ == '__main__':
    main()
