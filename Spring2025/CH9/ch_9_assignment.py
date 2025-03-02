import random

"""
Programmer: Riley Perez
Assignment: Module 6 - Assignment
Date Completed: 3/2/25
Course: CITC 2391 - C01
Instructor: Martin Bell
"""


# Returns a set of all US states
def get_states_capitals():
    return {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "Saint Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismarck",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne"
    }


# Quiz's user's about the US states and their capitals. This also keeps track of their correct and incorrect score.
def quiz():
    states_capitals = get_states_capitals()  # Pull in set of states with their capitals
    states = list(states_capitals.keys())  # Get a list of all US states
    correct = 0  # Initialize correct answer tally
    incorrect = 0  # Initialize incorrect answer tally

    while True:
        state = random.choice(states)  # Get random state
        capital = states_capitals[state]  # Get the random state capital
        user_input = input(f"What is the capital of {state}? (or enter 0 to quit): ").strip()  # Get user's input

        if user_input.lower() == "0":  # If user_input is "0" then break the loop
            print(f"You answered correctly {correct} times and incorrectly {incorrect} times. Goodbye!")
            break
        elif user_input.lower() == capital.lower():  # If user_input is the random states capital then correct
            print("Correct!")
            correct += 1
        else:  # If user_input is not random states capital then incorrect
            print(f"Incorrect! The capital of {state} is {capital}.")
            incorrect += 1


if __name__ == "__main__":
    quiz()
