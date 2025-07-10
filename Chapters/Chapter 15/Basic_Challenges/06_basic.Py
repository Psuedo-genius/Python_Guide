# Check if a string is a palindrome using recursion.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


s = input("Enter string: ").replace(" ", "").lower()
print("Palindrome:", is_palindrome(s))
