# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', write a function to
#  determine if the input string is valid.

# An input string is valid if: 

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

def is_valid_parenthesis(s: str) -> bool:
    # cancella pass e scrivi qui il tuo codice
    listed: list= list(s)
    check: list= []
    brackets: dict = {"(": ")", "[": "]", "{": "}"}
    for i in listed:
        if i in brackets:
            check.append(i)
        elif i == brackets[check[-1]]:
            check.pop()
        else:
            return False
    return True

print(is_valid_parenthesis("()")) # Output: True

print(is_valid_parenthesis("()[]{}")) # Output: True

print(is_valid_parenthesis("(]")) # Output: False

print(is_valid_parenthesis("([)]")) # Output: False

print(is_valid_parenthesis("{[]}")) # Output: True

print(is_valid_parenthesis("")) # Output: True