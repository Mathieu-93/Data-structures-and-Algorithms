# Given a string,determine if it is compreised of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return false.

def unique(s):
    char = set()
    for let in s:
        if let in char:
            return False
        else:
            char.add(let)
    return True


print(unique("jdiwaoaA"))
