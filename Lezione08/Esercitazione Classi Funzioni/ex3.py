# Given a string s which consists of lowercase or uppercase letters, write a function that returns
#  the length of the longest palindrome that can be built with those letters. Letters are case sensitive,
#  for example, "Aa" is not considered a palindrome here.

def longest_palindrome(s: str) -> int:
    # cancella pass e scrivi qui il tuo codice
    listed_s: list = list(s)
    char_count: dict= {}
    result: list= []
    for char in listed_s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for key in char_count.keys():
        while char_count[key] >= 2:
            result.insert(0, key)
            result.insert(-1, key)
            char_count[key] -= 2
    for key in char_count.keys():
        if char_count[key] > 0:
            result.insert((len(result) // 2) +1, key)
            break
    return len(result)

print(longest_palindrome("abccccdd")) #7

print(longest_palindrome("a")) #1

print(longest_palindrome("Aa")) #1

print(longest_palindrome("abccccba")) #8

print(longest_palindrome("abcabcabc")) #7