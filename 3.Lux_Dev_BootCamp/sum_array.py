# Given an array of integers, find the sum of its elements.
# From HackerRank

def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum

print(simpleArraySum([1, 2, 3, 4, 10, 11]))

