import conversions as c


# Prints the conversion menu options to the console.
def print_menu_options():
    print("Conversions Menu:\na. Feet to Meters\nb. Meters to Feet\n")


# Prints an error message to the console.
def print_error(error_message):
    print("Invalid input: " + error_message)


# Prompts the user to decide whether to roll the dice.
# Returns True if the user chooses "Y", False if they choose "N".
def user_choice_loop():
    while True:
        user_input = input("Would you like to perform another conversion? (y/n): ").strip().lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            print("Bye!")
            return False
        else:
            print_error("Enter either 'Y' or 'N'.")


# Loops until the user enters a valid conversion choice ('a' or 'b').
# Returns the user's choice as a string.
def menu_choice_validation_loop():
    while True:
        print_menu_options()
        user_input = input("Select a conversion (a/b): ").strip().lower()
        if user_input == "a" or user_input == "b":
            return user_input
        else:
            print_error('Your choices are "a" or "b"')


# Attempts to convert a string input into a float.
# If the input is not a valid number, prints an error message and returns None.
def parse_float(prompt_message):
    while True:
        try:
            return float(input(prompt_message))
        except ValueError:
            print_error("Please enter a valid number.")


# Generic function to perform a unit conversion
def perform_conversion(conversion_type, prompt, conversion_function, unit):
    value = parse_float(prompt)
    result = conversion_function(value)
    print(f"\nThe answer is {round(result, 2)} {unit}.")


# Main function that runs the Feet and Meters Converter.
# Loops until the user decides to stop converting.
def main():
    print("Feet and Meters Converter")
    while True:
        user_input = menu_choice_validation_loop()

        if user_input == "a":
            perform_conversion("Feet to Meters", "Enter feet: ", c.calculate_feet_to_meter, "meters")
        elif user_input == "b":
            perform_conversion("Meters to Feet", "Enter meters: ", c.calculate_meter_to_feet, "feet")

        if not user_choice_loop():
            break  # Exit the loop if the user chooses "n"


main()
