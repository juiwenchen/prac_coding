"""impl Quick Sort.

    Time complexity is N*log(N) in the best and avarage scenarios
    N^N is the worst scenario, when the duplicate and the numbers are sorted already.
    https://www.youtube.com/watch?v=0SkOjNaO1XY
"""
def quick_sort(array: list, left: int, right: int):
    """Implement Quick Sort.

    The elements in the given array recursively by find the pivot of the array and sort the left array of the pivot and 
    right array of the pivot.

    :param: array: a list of elements
    :param: left: pointer of left
    :param: right: pointer of right
    """
    # Check if the left equals to right. It means only one element is left in the given array and it's no need to sort.
    if right <= left:
        return
    
    # Find the index of the pivot <--- This is the core of Quick Sort
    pivot_idx = partition(array, left, right)

    # Sort the left group to the pivot
    quick_sort(array, left=left, right=pivot_idx - 1)
    # Sort the right group to the pivot
    quick_sort(array, left=pivot_idx, right=right)


def partition(array: list, left, right):
    """Sort the given list into two sides of the chosen value (pivot).

    The numbers smaller than the pivot are on the left, while those bigger than the pivot put on the right. 

    :param: array: [description]
    :param: left: [description]
    :param: right: [description]
    """
    pivot = array[right]
    idx_pivot = right
    for idx in range(left, right + 1, 1): # iterate including the right idx
        if array[idx] > pivot and idx < idx_pivot: 
            # The numbers smaller than the pivot shall be on the left
            # Check if the number bigger than pivot and it's on the left of the pivot
            # Then swap the location in the list
            swap_temp = array[idx]
            array[idx] = pivot
            array[idx_pivot] = swap_temp
            idx_pivot = idx
    
    return idx_pivot




def main():
    array = [12, 4, 5, 6, 7, 3, 1, 15]
    quick_sort(array, 0, len(array) - 1)
    print(array)

if __name__ == "__main__":
    main()
