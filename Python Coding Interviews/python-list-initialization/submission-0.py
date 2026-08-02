from typing import List


def create_list_with_value(size: int, index: int, value: int) -> List[int]:
    #size = size
    #[0] except for value at index 
    #return list of size 0s then replace val at index
    newList = [0] * size
    newList[index] = value
    return newList



# do not modify below this line
print(create_list_with_value(5, 3, 7))
print(create_list_with_value(1, 0, 5))
print(create_list_with_value(10, 9, 9))
print(create_list_with_value(10, 9, 0))
