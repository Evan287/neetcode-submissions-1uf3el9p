from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    newList = []
    for i in range(-1, -4, -1):
        newList.append(my_list[i])
    newList.sort()
    return newList


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
