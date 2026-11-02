import random

# Deterministic Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


# Randomized Quick Sort
def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)

    arr[random_index], arr[high] = arr[high], arr[random_index]

    return partition(arr, low, high)


def randomized_quick_sort(arr, low, high):
    if low < high:
        p = randomized_partition(arr, low, high)

        randomized_quick_sort(arr, low, p - 1)
        randomized_quick_sort(arr, p + 1, high)


# Main Program
n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

arr1 = arr.copy()
arr2 = arr.copy()

quick_sort(arr1, 0, n - 1)
randomized_quick_sort(arr2, 0, n - 1)

print("\nDeterministic Quick Sort:", arr1)
print("Randomized Quick Sort:", arr2)