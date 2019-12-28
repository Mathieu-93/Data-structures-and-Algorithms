def pair_sum(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
            print(seen)
        else:
            output.add((min(num, target), max(num, target)))
            print(output)
    # return len(output)
    print('\n'.join(map(str, list(output))))


pair_sum([3, 5, 1, 2, 3, 2, 2], 4)
