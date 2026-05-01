"""Write a Python program to count the number 4 in a given list."""
def count(lst : list) -> int:
    """this function will return  the number of occuerence of
      number 4 in a given list .... 
      the commented line is the solution but in C-style & other pyhtons sol."""
    # no_4_occuernces = 0
    # for i in range (len(lst)):
    #     if lst[i] == 4:
    #         no_4_occuernces +=1
    # return no_4_occuernces
    # for item in lst:
    #     no_4_occuernces+=1 if item == 4 else 0
    # return no_4_occuernces
    # return sum(True for item in lst if item == 4)
    return lst.count(4)
if __name__ == "__main__":
    assert count([1, 2, 3, 4, 5, 4, 6]) == 2, "Test case failed"
    assert count([1, 2, 3, 5, 6]) == 0, "Test case failed"
    assert count([4, 4, 4, 4]) == 4, "Test case failed"
    assert count([]) == 0, "Test case failed"
    assert count([4, 5, 6, 7, 8]) == 1, "Test case failed"
    assert count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1, "Test case failed"
