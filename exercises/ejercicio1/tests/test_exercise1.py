from ejercicio1.exercise1 import is_palindrome

# test if a word is a palindrome
def test_is_palindrome() -> None:
    assert is_palindrome("ana")

# test if the word pass as arg is not a palindrome
def test_is_not_palindrome() -> None:
    assert is_palindrome("juan") == False

# test if the word pass as arg is not a str
def test_is_palindrome_int() -> None:
    assert is_palindrome(123) == 'You must pass a string'


