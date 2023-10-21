# A palindrome, also called palindrome, palindrome, palindrome or palindrome, is a word, or phrase, that is
# phrase that reads the same in one direction as in the other. Example ANA can be read backwards and forwards and means the same thing.
# backwards and means the same thing.

def is_palindrome(word):
    """Checks if a word is a palindrome.

    Args:
      word: A string.

    Returns:
      True if the word is a palindrome, False otherwise.
    """

    if not isinstance(word, str):
        return 'You must pass a string'

    word = word.lower().replace(" ", "")

    # Check if the word is the same forwards and backwards.
    return word == word[::-1]

def main():
  print(is_palindrome("ana"))

if __name__ == '__main__':
  main()