import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 54, 34, 32]
    test_arr = [11, 12, 22, 25, 32, 34, 34, 54, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 54, 34, 32]
    test_arr = [90, 64, 54, 34, 34, 32, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)


def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 54, 34, 32]

    result = Lab3.bubble_sort(input_arr, [])

    assert (result == [])


def test_bubble_sort_req02a():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 54, 34, 32, 10]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 1)


def test_bubble_sort_req02b():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 54, 34, 32, 10]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 1)


def test_bubble_sort_req03b():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 54, 34]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 2)


def test_bubble_sort_req03b():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 54, 34]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 2)


def test_bubble_sort_req04a():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == 0)


def test_bubble_sort_req04b():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)

def test_bubble_sort_req05():
    result = []
    input_arr = [1, "s", "b", 2, 4, 5, 6, 7, 8, 10, 1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 3)

