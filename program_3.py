# Program #3: Average Numbers
#Mark Nyagaka
#10-30-25

# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.

# The program should handle the following exceptions:
# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file
# are converted to a number.

def sum_numbers_from_file():
    try:
        with open("numbers.txt", "r") as file:
            total = 0
            count = 0

            for line in file:
                try:
                    number = int(line.strip())
                    total += number
                    count += 1
                except ValueError:
                    print(f"Warning: Could not convert '{line.strip()}' to an integer. Skipping...")

            if count > 0:
                average = total / count
                print(f"Total of all numbers: {total}")
                print(f"Average of numbers: {average:.2f}")
            else:
                print("No valid numbers found in the file.")

    except IOError:
        print("Error: The file 'numbers.txt' could not be opened or read.")

    print('In the sum_numbers_from_file function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()