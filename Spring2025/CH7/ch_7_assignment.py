def read_data():
    # Initialize an empty list to store the list of lists
    data_list = []

    # Open the file for reading
    try:
        with open("nutrition_data.csv", "r") as file:
            # Read each line in the file
            for line in file:
                # Strip the newline character and split by comma
                line_data = line.strip().split(",")
                # Append the list to the main list
                data_list.append(line_data)
    except FileNotFoundError:
        print("Error: The file 'nutrition_data.csv' was not found.")
        return []

    return data_list  # Return the main list


# This function will build five separate lists containing nutrition information and return only the users selection
def create_separate_list(nutrition_list, user_choice):
    dairies = []
    meats = []
    veggies = []
    fruits = []
    grains = []

    for line in nutrition_list:
        match line[0]:
            case "Dairy":
                dairies.append(line)
            case "Meat":
                meats.append(line)
            case "Vegetables":
                veggies.append(line)
            case "Fruit":
                fruits.append(line)
            case "Grains":
                grains.append(line)
            case _:
                print("Error: Unrecognized food category.")

    match user_choice:
        case 1:
            return dairies
        case 2:
            return meats
        case 3:
            return veggies
        case 4:
            return fruits
        case 5:
            return grains
        case _:
            return print("Error: Unrecognized food category.")


# Helper function prints the menu options to the console.
def display_menu():
    print("Nutrition by Food Group")
    print("1. Dairy")
    print("2. Meat")
    print("3. Vegetables")
    print("4. Fruit")
    print("5. Grains")


# Helper function prints the user's selected choice to the console
def display_selection(user_selected_list):
    sorted_list = sorted(user_selected_list, key=lambda x: x[1])
    # Column widths
    col1_width = 20  # Name column
    col2_width = 10  # Amount column
    col3_width = 8   # Calories column
    print(f"{'Name'.ljust(col1_width)} {'Amount'.ljust(col2_width)} {'Calories'.rjust(col3_width)}")
    print("-" * (col1_width + col2_width + col3_width + 2))

    for row in sorted_list:
        print(f"{row[1].ljust(col1_width)} {row[2].ljust(col2_width)} {str(row[3]).rjust(col3_width)}")

    print()


# Helper function to parse and validate a float with user re-entry prompt
def parse_int(prompt):
    while True:
        user_input = input(prompt)
        try:
            parsed_int = int(user_input)
            if parsed_int in range(1, 6):
                return parsed_int
            else:
                print("Error: Invalid entry. Please enter a valid menu option.")
        except ValueError:
            print("Error: Invalid entry. Please enter a valid number.")


def validate_user_choice(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "y" or user_input == "n":
            return user_input
        else:
            print("Error: Invalid option. Try again.")


def main():
    loop = "y"
    while loop == "y":
        nutrition_list = read_data()
        display_menu()
        user_input = parse_int("Enter your food group choice: (1-5): ")
        print()
        user_selected_list = create_separate_list(nutrition_list, user_input)
        display_selection(user_selected_list)

        loop = validate_user_choice("Would you like to perform another conversion? (y/n): ")


if __name__ == '__main__':
    main()
