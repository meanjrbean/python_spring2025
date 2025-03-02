# Returns a set of words from a file
def create_set_from_file(file_name):
    data_list = set()

    # Open the file for reading
    try:
        with open(file_name, "r") as file:
            # Read each line in the file
            for line in file:
                words = line.replace(",", "").replace(".", "").lower().split(" ")  # Remove periods and commas
                data_list.update(words)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")

    return data_list


# Analysis two files and prints to the console
def file_analysis(first_file, second_file):
    words_file1 = create_set_from_file(first_file)
    words_file2 = create_set_from_file(second_file)

    all_unique_words = (words_file1 | words_file2)  # Union
    common_words = words_file1 & words_file2  # Intersection
    only_in_file1 = words_file1 - words_file2  # Difference
    only_in_file2 = words_file2 - words_file1  # Difference
    unique_to_each_file = words_file1 ^ words_file2  # Symmetric Difference

    print("\nUnique words in both files:", all_unique_words)
    print("\nWords appearing in both files:", common_words)
    print("\nWords appearing only in the first file:", only_in_file1)
    print("\nWords appearing only in the second file:", only_in_file2)
    print("\nWords appearing in either file but not both:", unique_to_each_file)


if __name__ == '__main__':
    file_analysis("first_file.txt", "second_file.txt")
