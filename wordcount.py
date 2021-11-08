"""Count words in file."""
import sys

def tokenize(file_name):

    file = open(file_name)
    words = []

    for line in file:
        line = line.split()
        words.extend(line)
        
    return words

def count_words(words):
    word_counts = {}
    for word in words:
        word = word.rstrip(''''.,?!")]:;_-''')
        word = word.lstrip(''''.,?!([:;_-"''')
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def print_word_counts(word_counts):
    for word, count in word_counts.items():
        print(f"{word} {count}")

words = tokenize(sys.argv[1])
word_counts = count_words(words)
print_word_counts(word_counts)

#original code
# def word_count(file_name):

#     file = open(file_name)
#     word_counts = {}

#     for line in file:
#         line = line.split()
        
    #     for word in line:
    #         word = word.rstrip(''''.,?!")]:;_-''')
    #         word = word.lstrip(''''.,?!([:;_-"''')
    #         word_counts[word] = word_counts.get(word, 0) + 1

    # file.close()

    # return word_counts






