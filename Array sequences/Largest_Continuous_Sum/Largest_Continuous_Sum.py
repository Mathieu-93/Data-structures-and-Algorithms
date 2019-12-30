# PROBLEM
# Given an array of integers (positive and negative) find the largest continuous sum.

def large_cont_sum(arr):
    if len(arr) == 0:
        return 0

    sum_max = current = arr[0]
    it = 0

    start_point = []

    for num in arr[1:]:
        it += 1
        print("Iteration nr " + str(it) + " sum_max " + str(sum_max) + " num " + str(num) + " current " + str(current))
        current = max(current + num, num)
        sum_max = max(current, sum_max)
        if num < current + num and sum_max > current:
            start_point.append(num)
        if sum_max > num + current:
            end_point = num

    print("Start point " + str(start_point[0]))
    print("End point " + str(end_point))
    return sum_max


print(large_cont_sum([2, 3, -9, 4, -1, 4, 3, 2, -4]))
