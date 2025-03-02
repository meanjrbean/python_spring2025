import random


# Define the past or previous dice rolls.
PAST_DICE_RESULTS = [0, 0]

# Define Dice Combinations.
DICE_COMBINATIONS = {
    (1, 1): "Snake Eyes!",
    (6, 6): "Boxcars!",
    (2, 2): "Ballerina!",
    (4, 4): "Square Pair!",
    (6, 4): "Tennessee!"
}


# Prints an error message to the console.
def print_error(error_message):
    print("Invalid input: " + error_message)


# Prompts the user to decide whether to roll the dice.
# Returns True if the user chooses "Y", False if they choose "N".
def user_choice_loop():
    while True:
        user_input = input("Would you like roll the dice? Y/N ").strip().lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            print("Goodbye!")
            return False
        else:
            print_error("Enter either 'Y' or 'N'.")


# Generates a random number between 1 and 6.
# Ensures that the number is different from the previous roll.
def roll(previous_num):
    result = random.randint(1, 6)
    if previous_num != result:
        return result
    else:
        return roll(previous_num)


# Returns a name for special dice combinations based on the roll result.
def get_combination_names(roll_result):
    if isinstance(roll_result, list) and len(roll_result) == 2:
        return DICE_COMBINATIONS.get((roll_result[0], roll_result[1]), None)
    return None


# Checks if the rolled dice match a special combination and prints the name if applicable.
def check_dice_combination(roll_result):
    message = get_combination_names(roll_result)
    if message is not None:
        print(message)


# Rolls two dice, ensuring they don't match their previous values.
# Updates the global dice_results list and prints the results.
def roll_dice():
    results = [roll(PAST_DICE_RESULTS[0]), roll(PAST_DICE_RESULTS[1])]
    PAST_DICE_RESULTS[0] = results[0]
    PAST_DICE_RESULTS[1] = results[1]

    print(f"Die 1: {results[0]}\nDie 2: {results[1]}")
    check_dice_combination(results)


# Main function that starts the dice rolling program.
# Continues looping until the user chooses to stop.
def main():
    print("Dice Roller")
    while user_choice_loop():
        roll_dice()


# Run the program
main()
