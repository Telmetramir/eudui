def find_peak_element(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] > arr[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return arr[low]
