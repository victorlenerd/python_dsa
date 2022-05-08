def partition(items, low, high):
    firsthigh = low
    pivot = high
    currentItem = low

    while currentItem < high:
        if items[currentItem] < items[pivot]:
            items[currentItem], items[firsthigh] = items[firsthigh], items[currentItem]
            firsthigh += 1
        currentItem += 1

    items[currentItem], items[firsthigh] = items[firsthigh], items[currentItem]

    return firsthigh


def quicksort(items, low, high):
    if low < high:
        pivot = partition(items, low, high)
        quicksort(items, low, pivot - 1)  # sort elements to the left of the pivot
        quicksort(items, pivot + 1, high) # sort elements to the right of the pivot


if __name__ == '__main__':
    print("Implementation for QuickSort")

    data = [2, 3, 4, 6, 4, 1, 6, 8, 9, 5]

    data.sort()
    quicksort(data, 0, len(data) - 1)
    print(data)