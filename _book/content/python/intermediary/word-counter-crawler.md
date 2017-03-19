import requests
from bs4 import BeautifulSoup
import operator  # Buil-in module providing a set of convenient operators


def count_words(url, selector):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    links = soup.select(selector)

    for link in links:
        words = link.getText().lower().split()

        for word in words:
            word_list.append(word)

    cleanup_list(word_list)


def cleanup_list(word_list):
    cleaned_word_list = []

    for word in word_list:
        symbols = '!@#$%ˆ*()_+="\'[]<>&,./\|;'

        # Runs the loop until the length of symbols reached
        for symbol in range(0, len(symbols)):
            word = word.replace(symbols[symbol], '')  # Replace unwanted symbol with nothing

        if len(word) > 0:
            cleaned_word_list.append(word)

    create_dictionary(cleaned_word_list)


def create_dictionary(clean_words):
    word_store = {}  # Empty dictionary

    for word in clean_words:
        if word in word_store:
            word_store[word] += 1  # Increment value for the word in the dictionary
        else:
            word_store[word] = 1  # Add the word to dictionary with value of one

    # sort dictionary by the value
    for key, value in sorted(word_store.items(), key=operator.itemgetter(1)):  # In itemgetter, 1 means value, 0 the key
        print(key, value)


count_words('http://wwwhere.io/p1', '.link-description')
