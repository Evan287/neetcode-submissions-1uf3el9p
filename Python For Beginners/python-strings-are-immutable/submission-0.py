def remove_fourth_character(word: str) -> str:
    # one var = 0:2, second var = 4:, concatenate two
    before_fourth = word[:3]
    after_fourth = word[4:]
    return before_fourth + after_fourth


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
