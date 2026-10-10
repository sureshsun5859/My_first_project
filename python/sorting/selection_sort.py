#selection sort algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        for j in range(i+1, n):
            # Update min_index if a smaller element is found
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
# Example usage
if __name__ == "__main__":
    sample_array = [64, 25, 12, 22, 11]
    sorted_array = selection_sort(sample_array)
    print("Sorted array is:", sorted_array)