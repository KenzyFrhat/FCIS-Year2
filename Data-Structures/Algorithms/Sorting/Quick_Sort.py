def partition(arr, low, high):
    pi = arr[high] #pivot 
    j = low -1 
    for i in range(low + 1, high + 1):
        if arr[i] < pi:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[high], arr[j + 1] = arr[j + 1], arr[high]
    return  j + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    sorted_arr = quick_sort(arr, 0, n - 1)
    print("Sorted array is:", sorted_arr) 