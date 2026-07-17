# find palindrome using slicer

def is_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

word = input("Enter a string: ")
print(is_palindrome(word))
