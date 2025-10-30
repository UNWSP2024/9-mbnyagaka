# Program #2: Random Number File Writer
#Mark Nyagaka
#10-30-25

# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).

import random

def write_random_numbers():
    try:
        amount = int(input("How many random numbers would you like to write (1–1000)? "))

        if amount < 1 or amount > 1000:
            print("Please enter a number between 1 and 1000.")
            return

        with open("random_numbers.txt", "w") as file:
            for i in range(amount):
                number = random.randint(1, 500)
                file.write(str(number) + "\n")

        print(f"{amount} random numbers have been written to 'random_numbers.txt'.")

    except ValueError:
        print("Invalid input. Please enter an integer value.")

    print("In the write_random_numbers function")

# You don't need to change anything below this line:
if __name__ == '__main__':
    write_random_numbers()