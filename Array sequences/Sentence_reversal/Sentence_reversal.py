# Given a string of words, reverse all the words. For example:
# Given:
# 'This is the best'
# Return:
# 'best the is This'
# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
# '  space here'  and 'space here      '
# both become:
# 'here space'

def sen_rev1(s):
    words = []
    length = len(s)
    spaces = [' ']

    i = 0
    while i < length:
        # find start point
        if s[i] not in spaces:
            start_point = i
            # illiterate till find end point
            while i < length and s[i] not in spaces:
                i += 1
            # Make list
            words.append(s[start_point:i])
        i += 1

    rev_string = []
    index = len(words)
    while index:
        index -= 1
        rev_string.append(words[index])
    return ' '.join(rev_string)


# solve the problem with the use of split() and some slicing or use of reversed


print(sen_rev1('   My name is  Matthew'))

