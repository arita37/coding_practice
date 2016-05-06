def split(array):
    """Return two splitted arrays from an array

    If len(array) is odd, then the right array will be larger
    """
    return array[:len(array)/2], array[len(array)/2:]


def merge(left, right):
    """Return merged and sorted array from two sorted arrays
    
    left, right -- arrays that are sorted from left to right
    """
    # corner cases
    if left[-1] < right[0]:
        return list(left) + list(right)
    elif right[-1] < left[0]:
        return list(right) + list(left)

    # make all possible comparisons
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # for remaining elements in the lists that were never compared
    if left:
        result.extend(left)
    if right:
        result.extend(right)

    return result


def checkSorted(array):
    """Check if an array is sorted from left to right"""
    for i in xrange(len(array)-1):
        if array[i] > array[i+1]:
            return False
    return True


def mergeSortRecur(array):
    """Return sorted array recursively"""
    if len(array) <= 1:
        return array

    # if not already sorted, recursively split and merge
    # in the final split, two 1-element arrays will merge
    if not checkSorted(array):
        left, right = split(array)
        left = mergeSortRecur(left)
        right = mergeSortRecur(right)

        result = merge(left, right)
        return result

    else:
        return list(array)


def mergeSortIter(array):
    """Return sorted array iteratively"""

    # split into 1-element arrays
    array = list([a] for a in array)

    # merge neighboring arrays and set next elemnt to None
    while len(array) != 1:
        for idx, item in enumerate(array):
            if idx != (len(array) - 1) and array[idx] != None:
                array[idx] = merge(item, array[idx+1])
                array[idx+1] = None

        array = [a for a in array if a != None]     # remove None elements
    return array[0]



if __name__ == "__main__":
    from numpy.random import randint
    
    # check even array
    array = list(randint(1, 10, size=10))
    assert mergeSortRecur(array) == sorted(array)
    assert mergeSortIter(array) == sorted(array)

    # check odd array
    array = randint(1, 10, size=11)
    assert mergeSortRecur(array) == sorted(array)
    assert mergeSortIter(array) == sorted(array)
