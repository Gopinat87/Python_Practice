#to find 2nd largest number

def second_largest(arr):
    if len(arr) < 2:
        return -1

    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return -1

    return second


arr = [10, 20, 5, 20, 8, 15]
print(second_largest(arr))