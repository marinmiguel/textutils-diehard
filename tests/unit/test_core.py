#Count the number of unique words in a string.
#Args: text(str): The input string.
#Return: int: The count of unique words in the string.

import textutils.core as c

def test_unique_words():
    text = "hello world hello"
    assert c.unique_words(text) == {'hello': 2, 'world':1}

def test_unique_words_case_insensitive():
    text = "Hello HELLO world"
    assert c.unique_words(text) == {"hello": 2, "world": 1}

def test_unique_words_with_punctuation():
    text = "Hello, world! Hello... world?"
    assert c.unique_words(text) == {"hello": 2, "world": 2}

def test_unique_words_empty_string():
    text = ""
    assert c.unique_words(text) == {}

def test_unique_words_single_word():
    text = "hello"
    assert c.unique_words(text) == {"hello": 1}

def test_unique_words_multiple_spaces():
    text = "hello    world   hello"
    assert c.unique_words(text) == {"hello": 2, "world": 1}

def test_unique_words_only_punctuation():
    text = "... !!! ???"
    assert c.unique_words(text) == {}