from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_set = set()
    for word in words:
        if word not in my_set:
            my_set.add(word)
        else:
            return True
    return False


# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
