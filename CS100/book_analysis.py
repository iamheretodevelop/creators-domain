import math
import string
import sys

def read_file(filename):
    with open(filename, "r") as file:
        lines = []
        for line in file:
            lines.append(line)
    return lines 

def get_words_from_string(line):
    lowercase = line.lower()
    lower_case = ""
    for char in lowercase:
        if char in string.punctuation:
            lower_case += " "
        else:
            lower_case += char
    string_list = lower_case.split()
    return string_list

def get_words_from_line_list(list_of_lines):
    word_list = []
    for char in list_of_lines:
        list_line = get_words_from_string(char)
        for word in list_line:
            word_list.append(word)
    return word_list    
 


def count_frequency(word_list):
    word_count = {}
    for i in word_list:
        if i in word_count:
            word_count[i] += 1
        else:
            word_count[i] = 1
    return word_count



def find_most_common_word(freq_map):
    k = 0
    if len(freq_map) == 0:
        return ""
    for i in freq_map:
        if freq_map[i] > k:
            k = freq_map[i]
            word_common = i
    

    return word_common 



def write_result(filename):
    
    with open("result.txt", "w") as f:
        print("File:" , filename, file = f)
        number_lines = read_file(filename)
        number_words = get_words_from_line_list(number_lines)
        number_distinct = count_frequency(number_words)
        most_common = find_most_common_word(number_distinct)
        print("Number of lines:" , str(len(number_lines)), file = f)
        print("Number of words:", str(len(number_words)), file = f)
        print("Number of distinct words:", str(len(number_distinct)), file = f)
        print("Most commonly used word:", most_common, file = f)
        
