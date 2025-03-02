# Helper function that prints the greeting to console
def get_greeting():
    print("The Quarterly Sales Program\n")


# Helper function to parse and validate a float with user re-entry prompt
def parse_float(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Error: Invalid entry. Please enter a valid number.")


# Gets user input for quarterly_sales list
def get_quarterly_sales():
    quarterly_sales = []
    for i in range(1, 5):  # Iterate through 4 quarters
        sales = parse_float(f"Enter sales for Q{i}: ")
        quarterly_sales.append(sales)
    return quarterly_sales


# Calculates and displays the provided quarterly sales
def process_sales(user_quarterly_sales):
    total = sum(user_quarterly_sales)
    lowest = min(user_quarterly_sales)
    highest = max(user_quarterly_sales)
    average = total / len(user_quarterly_sales)

    # Print the results to console with proper formatting
    print(f"\nTotal: ${total:.1f}")
    print(f"Average Quarter: ${average:.1f}")
    print(f"Lowest Quarter: ${lowest:.1f}")
    print(f"Highest Quarter: ${highest:.1f}")


def main():
    get_greeting()
    user_quarterly_sales = get_quarterly_sales()
    process_sales(user_quarterly_sales)


if __name__ == '__main__':
    main()
