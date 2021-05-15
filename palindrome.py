#Palindrome checker

def is_palindrome(word):
    return True if word.lower() == word.lower()[::-1] else False


if __name__ == "__main__":
    user_input = input("Enter a word: ")
    if is_palindrome(user_input):
        print(user_input + " is a palindrome")
    else:
        print(user_input + " is not a palindrome")  
