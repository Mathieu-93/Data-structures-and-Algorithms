def anagram(s1, s2):
    # Create a chain of sign without spaces and capital letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # It's crucial to have the same length
    if len(s1) != len(s2):
        return False

    # Empty dictionary
    count = {}

    # Assign to every character number
    for i in s1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # Subtract till achieve empty dictionary
    for j in s2:
        if j in count:
            count[j] -= 1
        else:
            count[j] = 1
    # return False when dictionary have any characters
    for k in count:
        if count[k] != 0:
            return False
    return True


# Simply test
print("Test alghoritm is dog equal to god?:")
print(anagram('dog', 'god'))
print("Clint Eastwood play in Old west action?")
print(anagram('clint eastwood', 'old west action'))
