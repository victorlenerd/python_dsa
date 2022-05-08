def partition(arr, low, high):
    pivot = high
    firsthigh = low
    current = low

    while current < high:
        if arr[current] < arr[pivot]:
            arr[firsthigh], arr[current] = arr[current], arr[firsthigh]
            firsthigh += 1
        current += 1

    arr[firsthigh], arr[current] = arr[current], arr[firsthigh]

    return firsthigh


def randomized_select(arr, low, high, i):
    if low == high:
        return arr[low]     # 1 <= i <= high - low + 1 when low == high means that i = 1

    pivot = partition(arr, low, high)
    k = pivot - low + 1
    if i == k:
        return arr[pivot]
    elif i < k:
        return randomized_select(arr, low, pivot - 1, i)
    else:
        return randomized_select(arr, pivot + 1, high, i - k)


if __name__ == '__main__':
    arr = [6, 19, 4, 12, 14, 9, 15, 7, 8, 11, 3, 13, 2, 5, 10]
    sorted = arr.copy()
    sorted.sort()
    res = randomized_select(arr, 0, len(arr) - 1, 1)
    print(sorted)
    print(res)