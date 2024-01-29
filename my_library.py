# use list comprehension to count the number of 2s in a list of integers
def count_has_2(a: list[int]) -> int:
    return len([x for x in a if "2" in str(x)])
