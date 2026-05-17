import math

# Reverse string
def reverse_string(word):
    return ''.join(reversed(word))

def test_reverse_string():
    assert reverse_string("Chloride") == "edirolhC"

# Palindrome

def is_palindrome(word):
    return word == word[::-1]

result = is_palindrome("abba")

def test_is_palindrome():
    assert is_palindrome("racecar") == True

# Factorial

def compute_factorial(number):
    return math.factorial(number)

def test_compute_factorial():
    assert compute_factorial(5) == 120