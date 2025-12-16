"""
This module contains functions to analyze a text from a file.
"""

from operator import itemgetter

def file_content(file_path):
    """
    This function return content from a file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def count_lines(text):
    """
    This function counts lines in a text.
    """
    return len([line for line in text.split('\n') if line.strip()])


def count_words(text):
    """
    This function count words in a text.
    """
    words = text.split()
    return len(words)


def count_letters(text):
    """
    This function counts letters in a text.
    """
    return sum(1 for char in text if char.isalpha())


def clean_word(word):
    """
    This function removes all non-alphabetic characters from a word and returns it in lowercase.
    """
    return ''.join([char.lower() for char in word if char.isalpha()])


def calculate_frequencies(items):
    """
    This function calculates the frequency of items (words or letters) in a given list.
    """
    frequencies = {}
    total_items = len(items)
    for item in items:
        frequencies[item] = frequencies.get(item, 0) + 1
    sorted_frequencies = sorted(frequencies.items(), key=itemgetter(1, 0), reverse=True)
    return sorted_frequencies, total_items


def word_frequency(text):
    """
    This function calculates the frequency of each word in the given text.
    """
    words = [clean_word(word) for word in text.split()]
    sorted_word_freq, total_words = calculate_frequencies(words)
    result = []
    for word, count in sorted_word_freq[:7]:
        percent = (count/total_words)*100
        result.append(f"{word}: {count} | {percent:.1f}%")
    return result


def letter_frequency(text):
    """
    This function calculates the frequency of each letter in a given text.
    """
    letters = [char.lower() for char in text if char.isalpha()]
    sorted_letter_freq, total_letters = calculate_frequencies(letters)
    result = []
    for letter, count in sorted_letter_freq[:7]:
        percent = (count/total_letters)*100
        result.append(f"{letter}: {count} | {percent:.1f}%")
    return result


def all_results(text):
    """
    Prints the result of all the functions to analyze a text.
    """
    results = []
    results.append(f"Lines: {count_lines(text)}")
    results.append(f"Words: {count_words(text)}")
    results.append(f"Letters: {count_letters(text)}")
    results.extend(word_frequency(text))
    results.extend(letter_frequency(text))
    return "\n".join(results)
