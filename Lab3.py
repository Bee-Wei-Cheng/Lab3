print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1


def bubble_sort(arr, sorting_order):

    # Copy input list to results list
    arr_result = arr.copy()

    # Get number of elements in the list
    n = len(arr_result)

    for x in arr_result:
        if isinstance(x, int) == 0:
            return 3

    if n < 10 and n != 0:  # req-03
        return 2

    if n == 0:  # req-04
        return 0

    if n == 10:  # req-01
        # Traverse through all array elements
        for i in range(n - 1):
            # range(n) also work but outer loop will
            # repeat one time more than needed.

            # Last i elements are already in place
            for j in range(0, n - i - 1):

                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
                else:
                    arr_result = []
    else:  # req-02
        arr_result = 1

    return arr_result


def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 10, 9, 8, 7]
    choice = 1
    choice = input('Enter choice (0 for ascending and 1 for descending)')
    if choice == '0':
        result = bubble_sort(arr, SORT_ASCENDING)
        print("\nSorted array in ascending order: ")
        print(result)
    if choice == '1':
        print("Sorted array in descending order: ")
        result = bubble_sort(arr, SORT_DESCENDING)
        print(result)


if __name__ == "__main__":
    main()


