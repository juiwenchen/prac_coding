from typing import List

def merge_sort(array: List):
    """Implement merge sort.
    
    1. Cut the list in half recursively till only one element is left. (dive)
    2. Compare the left and the right, and merge them in the ascending order recursively (conquer)
    This method is also known as dive-and-conquer

    The time complexity is n*log(n). n is the number of the elements in the list.
    The space complexity is O(n) as the deepest stack is n
    :param array: [description]
    :return [description]
    """
    if len(array) <= 1: 
        return array

    # Cut in half recursively
    middle = len(array) // 2
    left = merge_sort(array[0:middle])
    right = merge_sort(array[middle: len(array)])

    # Sort and merge 
    sorted_array = merge_array(left, right)
    
    return sorted_array


def merge_array(left: List, right: List) -> List:
    """Merge the left and right lists in the ascending order.

    :param left: [description]
    :param right: [description]
    :return sorted list
    """
    sorted_array = []
    left_pointer = right_pointer = 0

    while (left_pointer < len(left) and right_pointer < len(right)):
        # Make comparison between the elements in the two sorted lists
        if left[left_pointer] <= right[right_pointer]:
            sorted_array.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_array.append(right[right_pointer])
            right_pointer += 1

    # Add the rest to the list 
    # The magic here is the slice as it won't cause error of the index out of range
    sorted_array.extend(left[left_pointer:])
    sorted_array.extend(right[right_pointer:])

    return sorted_array

    
def main():
    array = [3, 5, 8, 7, 1, 6, 2]
    sorted_array = merge_sort(array)
    print(sorted_array)

if __name__ == "__main__":
    main()
