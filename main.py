from collections import Counter
from functools import wraps
import time
from itertools import islice
from math import sqrt
from collections import defaultdict


# Q1. Write a program that reads in all the lines of the file
# (take any random or article from wikipedia), and then create a dictionary, where the key is the line number and value is another dictionary.
# This another dictionary should contain length of the words as keys, and the number of words having same length as values.

## Program to calculate the word calculator
def word_calculator(fileName):
    dict_obj = {}
    with open(fileName) as f:
        for key, line in enumerate(f):
            # (key, val) = line.split()
            # dictObj[int(key)] = val
            words = line.split()
            words_count = Counter(words)
            word_dict = {}

            for word_index, word in enumerate(words_count):
                # word_dict = {
                #     len(word): (word_index + 1)
                # }
                # print(len(word))

                if len(word) in word_dict:
                    word_dict[len(word)].append(len(word))
                else:
                    word_dict[len(word)] = [len(word)]

            dict_obj[int(key + 1)] = word_dict
    print(dict_obj)


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
def get_sum_of_square_numbers(num):
    """
    Simple function that returns sum of all numbers up to the square of num.
    """
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
def get_anagrams(source):
    d = defaultdict(list)
    for word in source:
        key = "".join(sorted(word))
        d[key].append(word)
    return d
def print_anagrams(input):
    d = get_anagrams(input)
    print(d)
    for key, anagrams in enumerate(d):
        if len(anagrams) > 1:
            print(key, anagrams)


# Q5. Write a function or lambda function (preferably) that takes a list of strings and returns a new list
# with all strings sorted in descending order of length.
def list_for_descending_order_string(list_to_sort):
    # list_to_sort = sorted(list_to_sort,key=lambda l:l[0], reverse=True)
    list_to_sort.sort(key=len, reverse=True)
    print(list_to_sort)

##################################################### Calling of various functions to show result of various questions

# Q1
#word_calculator("lorem.txt")

# Q2
# if __name__ == '__main__':
#     get_sum_of_square_numbers(10)

# Q3
# num = input('Please enter any number upto which you want to generate prime nos.')
# if num:
#     print_prime_numbers(int(num))

# Q4
# input_list = ['racecar', 'hello', 'level', 'carcare', 'carecar', 'civic', 'lehol', 'vicic']
# print_anagrams(input_list)

# Q5
# list_to_sort = ["dog", "cat", "bird"]
# list_to_sort = ["python", "java", "c++"]
# list_for_descending_order_string(list_to_sort)
