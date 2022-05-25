# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    isAnagram = 1
    for x in word:
        for y in anagram:
            if x == y:
                isAnagram = 1
                break
            else:
                isAnagram = 0
        if isAnagram == 0:
            break
    if isAnagram == 1:
        return True  
    else:
        return False

print("Check if two words are anagrams: hello & check")
print(find_anagram("hello", "check"))
print("Check if two words are anagrams: below & elbow")
print(find_anagram("below", "elbow"))


