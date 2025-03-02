# This is a reusable object that is used to track the range of shipping costs within the script
class ShippingCost:
    min_cost = 0.00
    max_cost = 0.00
    shipping_cost = 0.00

    # define the class initializer
    def __init__(self, min_cost, max_cost, shipping_cost):
        self.min_cost = min_cost
        self.max_cost = max_cost
        self.shipping_cost = shipping_cost

    # define the "toString" method used by Python for print formatting
    def __str__(self):
        if self.min_cost == 0.00:
            return f"< {self.max_cost:<8} ${self.shipping_cost}"
        elif self.max_cost == 0.00:
            return f"> {self.min_cost:<8} FREE"
        else:
            return f"{self.min_cost}-{self.max_cost:<8} ${self.shipping_cost}"


# Global list of ShippingCost objects and is used to calculate the total cost
current_shipping_cost = \
    [
        ShippingCost(0.00, 30.00, 5.95),
        ShippingCost(30.00, 49.99, 7.95),
        ShippingCost(50.00, 74.99, 9.95),
        ShippingCost(75.00, 0.00, 0.00)
    ]


# Helper function that prints the shipping cost's to the console
def display_selection():
    costs = {"< $30.00": "$5.95", "$30.00 - $49.99": "$7.95", "$50.00 - $49.99": "$9.95", "> $75.00": "FREE"}
    sorted_list = sorted(costs, key=lambda x: x[1])
    # Column widths
    col1_width = 25  # Name column
    col2_width = 10  # Amount column
    print(f"{'Order Amount'.ljust(col1_width)} {'Shipping Cost'.ljust(col2_width)}")
    print("-" * (col1_width + col2_width + 2))

    for row in costs:
        print(f"{row.ljust(col1_width)} {costs[row].ljust(col2_width)}")

    print()


# This function accepts an error message as a string and prints it to the console.
def print_error(error_message):
    print("Invalid input: " + error_message)


# This function attempts to parse a string into an integer.
# Returns an integer if successful.
# Returns None if it fails.
def parse_float(number):
    try:
        num = float(number)
        return num
    except ValueError:
        return None


# Function handles checking user's input for a key to exit a loop.
# Returns True if "Y"
# Returns False if "N"
def user_choice_loop():
    loop = True
    while loop:
        user_input = input("Would you like to try again? Y/N ")
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "n":
            print("Goodbye!")
            return False
        else:
            print_error("Enter either 'Y' or 'N'. Try again.")


# This is the main function that we run the program with.
def main():
    display_selection()
    loop = True
    while loop:
        user_input = input("Enter cost of items ordered: ")
        user_cost = parse_float(user_input)
        if user_cost is None:
            print_error("Please enter a number and try again.")
            continue
        elif user_cost < 1:
            print_error("You must enter a positive number. Try again.")
            continue
        else:
            if user_cost >= 75.00:
                user_total = user_cost
                print(f"Shipping Cost = FREE \nTotal Cost = ${round(user_total,2)}")
            for cost in current_shipping_cost:
                if cost.max_cost >= user_cost >= cost.min_cost:
                    user_total = cost.shipping_cost + user_cost
                    print(f"Shipping Cost = ${cost.shipping_cost}\nTotal Cost = ${round(user_total,2)}")

        loop = user_choice_loop()


if __name__ == "__main__":
    main()
