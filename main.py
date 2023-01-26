from functools import wraps
import time
from itertools import islice
from math import sqrt
import csv


# Q1. Write a program that reads in all the lines of the file
# (take any random or article from wikipedia), and then create a dictionary, where the key is the line number and value is another dictionary.
# This another dictionary should contain length of the words as keys, and the number of words having same length as values.

## Program to calculate the word calculator
def word_length_count(file_name):
    results = {}
    # Open the file for reading
    with open(file_name, 'r') as file:
        # Iterate through the lines of the file
        for line_number, line in enumerate(file):
            line = line.strip()
            words = line.split()
            word_lengths = {}
            # Iterate through the words
            for word in words:
                length = len(word)
                # If the length is already a key in the dictionary, increment the count
                if length in word_lengths:
                    word_lengths[length] += 1
                # Otherwise, add the length as a new key with a count of 1
                else:
                    word_lengths[length] = 1
            # Add the line number and word length counts dictionary to the results dictionary
            results[line_number] = word_lengths
    print(results)


# Q2. Write a decorator that measures the execution time of a function and logs the result to a file.

## Function to calculate execution time of a function
def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        with open('log.txt', 'w') as f:
            f.write(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result

    return timeit_wrapper

@timeit
def get_sum_of_square_numbers_to_calculate_execution_time(num):
    total = sum((x for x in range(0, num**2)))
    return total


# Q3. Write a generator function that yields the next prime number on each iteration.
def is_prime(n):
    if (n <= 1):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i = i + 2

    return True

def prime_generator():
    n = 1
    while True:
        n += 1
        if is_prime(n):
            yield n

def print_prime_numbers(num):
    array = [x for x in islice(prime_generator(), num)]
    print(array)


# Q4. Write a function that takes a list of strings and returns a new list with all strings that are anagrams of a palindrome
# (i.e., a word or phrase that can be rearranged to form a palindrome).
# If you can use list comprehension then it will be better.
def anagram_of_palindrome(strings):
    def is_anagram_of_palindrome(string):
        char_count = {}
        # Iterate through the string, updating the count of each character
        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        odd_count = 0
        # Iterate through the dictionary, counting the number of characters with odd counts
        for count in char_count.values():
            if count % 2 != 0:
                odd_count += 1
        # Return true if the string is an anagram of a palindrome, otherwise false
        return odd_count <= 1
    anagrams = []
    # Iterate through the input list, checking each string
    for string in strings:
        if is_anagram_of_palindrome(string):
            anagrams.append(string)
    print(anagrams)


# Q5. Write a function or lambda function (preferably) that takes a list of strings and returns a new list
# with all strings sorted in descending order of length.
def list_for_descending_order_string(list_to_sort):
    sorted_list = sorted(list_to_sort, key=lambda x: len(x), reverse=True)
    print(sorted_list)


# Q6. Write a function that reads in a CSV file and returns a list of dictionaries,
# where each dictionary represents a row in the CSV file with the keys being the column names and
# the values being the cell values.
def read_csv(file_name):
    with open(file_name, "r") as f:
        reader = csv.DictReader(f)
        formatted_list = list(reader)
    print(formatted_list)


# Q7. Write a function that takes a list of numbers and returns the sum of the numbers that are divisible by 3 or 5.
# The function should use a generator expression to accomplish this.
def divisble_numbers(list_of_nums, total=0):
    if list_of_nums:
        for num in list_of_nums:
            if num % 3 == 0 or num % 5 == 0:
                yield total + num

def sum_of_divisble_numbers(list_of_nums, total=0):
    nums = divisble_numbers(list_of_nums)
    for num in nums:
        total += num
    print('The sum of all the nos. divisible by 3 or 5 is: ', total)


# Q8. Write a function that handles the ValueError exception that may be raised
# when trying to convert a string to an integer.
# The function should prompt the user to enter a new string until a valid integer is entered.
def convert_string_to_int(msg="Please enter a number: "):
    input_data = input(msg)
    try:
        num = int(input_data)
        print(num)
    except ValueError:
        # Handle the exception
        convert_string_to_int("Please enter a valid number: ")




##################################################### Calling of various functions to show result of various questions

# Q1
word_length_count("lorem.txt")

# Q2
if __name__ == '__main__':
    get_sum_of_square_numbers_to_calculate_execution_time(10)

# Q3
num = input('Please enter any number upto which you want to generate prime nos.: ')
if num:
    print_prime_numbers(int(num))

# Q4
input_list = ['racecar', 'hello', 'level', 'carcare', 'carecar', 'civic', 'lehol', 'vicic']
anagram_of_palindrome(input_list)

# Q5
list_to_sort = ["dog", "cat", "bird"]
list_for_descending_order_string(list_to_sort)
list_to_sort = ["python", "java", "c++"]
list_for_descending_order_string(list_to_sort)

# Q6
read_csv("sample.csv")

# Q7
sum_of_divisble_numbers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sum_of_divisble_numbers([0, 15, 30, 45, 60, 75, 90, 105])

# Q8
convert_string_to_int()