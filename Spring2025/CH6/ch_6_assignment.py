# Prints an error message to the console.
def print_error(error_message):
    print("Error: " + error_message)


# Prints the command menu to the console.
def command_menu_print():
    print(f"\nCOMMAND MENU\nview - View a contact\nadd - Add a contact\ndel - Delete a contact\nexit - Exit program")


# Prints contacts from a file to the console.
def view_contacts(file_name):
    try:
        with open(file_name, "r") as file:
            count = 0
            for contact in file:
                count += 1
                print(f"{count}. {contact.strip()}")
    except IOError:
        print_error(f"Could not open file: {file_name}")


# Prompts user for contact information and appends to file.
def add_contacts(file_name):
    name = input("Enter contact name:")
    email = input("Enter email:")
    phone_number = input("Enter phone number:")
    contact_info = [name, email, phone_number]
    contact = ", ".join(contact_info)

    try:
        with open(file_name, "a") as file:
            file.write(contact)
    except IOError:
        print_error(f"Could not add contact to {file_name}. Please try again.")


# Prints current contacts to the console and then prompts user to choose which one to delete.
def delete_contacts(file_name):
    view_contacts(file_name)

    try:
        delete_number = int(input("\nEnter the number of the contact to delete: "))
    except ValueError:
        print_error("Invalid input. Please enter a number.")
        return

    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

        if delete_number < 1 or delete_number > len(lines):
            print_error("Invalid contact number. Please try again.")
            return

        new_content = ""
        count = 0
        for line in lines:
            count += 1
            if count != delete_number:
                new_content += line

        with open(file_name, "w") as file:
            file.write(new_content)

        print("\nContact deleted successfully!\n")
    except IOError:
        print_error(f"Could not modify {file_name}. Please try again.")


# Prompts the user to enter a command menu option
def user_choice_loop(file_name):
    print()
    while True:
        user_input = input("Command: ").strip().lower()
        if user_input == "view":
            # Show view function
            view_contacts(file_name)
            return True
        elif user_input == "add":
            # Show add function
            add_contacts(file_name)
            return True
        elif user_input == "del":
            # Show delete function
            delete_contacts(file_name)
            return True
        elif user_input == "exit":
            print("Bye!")
            return False
        else:
            print_error("Invalid choice. Try again.")
        print()


# Main function to check for a file before allowing them to make edits
def main():
    loop = True
    while loop:
        file_name = input("Please enter name of file:")
        try:
            file =  open(file_name, "r")
            file.close()
            while loop:
                command_menu_print()
                loop = user_choice_loop(file_name)
        except FileNotFoundError:
            print_error("Could not find file. Please try again.")


main()
