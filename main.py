from collections import Counter

# Q1. Write a program that reads in all the lines of the file
# (take any random or article from wikipedia), and then create a dictionary, where the key is the line number and value is another dictionary.
# This another dictionary should contain length of the words as keys, and the number of words having same length as values.

def word_calculator(fileName):
    dict_obj = {}
    with open(fileName) as f:
        for key, line in enumerate(f):
            #(key, val) = line.split()
            #dictObj[int(key)] = val
            words = line.split()
            words_count = Counter(words)
            word_dict = {}

            for word_index, word in enumerate(words_count):
                # word_dict = {
                #     len(word): (word_index + 1)
                # }
                #print(len(word))

                if len(word) in word_dict:
                    word_dict[len(word)].append(len(word))
                else:
                    word_dict[len(word)] = [len(word)]

            dict_obj[int(key + 1)] = word_dict
    print(dict_obj)






##################################################### Calling of various functions to show result of various questions

# Q1
word_calculator("lorem.txt")