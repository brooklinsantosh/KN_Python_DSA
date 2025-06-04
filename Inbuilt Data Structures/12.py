""" 
Count Word Frequency

Design a Python function named count_word_frequency to count the frequency of words in a sentence and 
store the counts in a dictionary.
"""

def count_word_frequency(sentence):
    if len(sentence)==0:
        return {}
    from collections import Counter
    return Counter(sentence.split(' '))

if __name__ == "__main__":
    print(count_word_frequency("hello world hello"))


