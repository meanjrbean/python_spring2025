# Prints an error message to the console.
def print_error(error_message):
    print("Error: " + error_message)


# Converts string to an integer.
def parse_int(number):
    try:
        return int(number)
    except ValueError:
        print_error("There was a problem parsing the provided number.")
        return None


# Reads numbers from a file, converts them to integers, and returns them as a list.
def parse_file(file_name):
    numbers = []
    try:
        with open(file_name, "r") as file:
            for num in file:
                number = parse_int(num.strip())
                if number is not None:
                    numbers.append(number)
                else:
                    print_error(f"Skipping invalid value: {num.strip()}")
    except IOError:
        print_error(f"Could not open file: {file_name}")
    return numbers


# Main function to process numbers in a file and separate them into even and odd files.
def main():
    file_name = "mod3numlist.txt"

    numbers = parse_file(file_name)  # Read and parse numbers

    with open("even_numbers.txt", "a") as even_file, open("odd_numbers.txt", "a") as odd_file:
        for num in numbers:
            if num % 2 == 0:
                even_file.write(f"{num}\n")  # Write even number
            else:
                odd_file.write(f"{num}\n")  # Write odd number

    print("Successfully parsed file!")


main()
