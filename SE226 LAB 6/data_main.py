from data_package import (
    remove_duplicates, strip_whitespaces,
    calculate_mean, find_maximum, find_minimum
)

a_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

tokens = a_input.split(",")
cleaned_strings = strip_whitespaces(tokens)

is_valid = True
for s in cleaned_strings:
    if s.lstrip("-").replace(".", "", 1).isdigit() == False:
        is_valid = False

if is_valid == False:
    print("Data Error: Please make sure you only enter numbers separated by commas.")
else:
    numbers = [float(s) for s in cleaned_strings]
    unique_numbers = remove_duplicates(numbers)

    print(f"\nCleaned and unique data: {unique_numbers}")
    print("-" * 20)
    print(f"Mean:    {calculate_mean(unique_numbers)}")
    print(f"Maximum: {find_maximum(unique_numbers)}")
    print(f"Minimum: {find_minimum(unique_numbers)}")