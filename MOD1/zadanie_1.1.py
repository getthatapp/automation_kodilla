def is_palindrome(s):
    # sprawdzam czy s jest stringiem
    if not isinstance(s, str):
        raise ValueError("Argument s must be a string")

    s = s.replace(" ", "").lower()
    return s == s[::-1]


assert is_palindrome("anna") == True, 'Test 1 not passed'
assert is_palindrome("hello") == False, 'Test 2 not passed'
assert is_palindrome("A man a plan a canal Panama") == True, 'Test 3 not passed'
assert is_palindrome(1234) == None, "Test 4 not passed"

print(is_palindrome("abba"))
