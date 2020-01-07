def balance_check(s):
    if len(s) % 2 != 0:
        return False

    opening = set('({[')
    matches = set([('(', ')'), ('{', '}'), ('[', ']')])
    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_paren = stack.pop()
            if (last_paren, paren) not in matches:
                return False
    return len(stack) == 0


print(balance_check('{}{[]}'))
