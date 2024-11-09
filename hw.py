"""
Exercise-1: Count unique elements
Write a function "count_unique_elements(my_list: list) -> int" that takes a 
list of integers and returns the number of unique elements in the list.

Example:
count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]) -> 5
"""

def count_unique_elements(my_list: list) -> int:
    unique_elements = set(my_list)
    return len(unique_elements)

print(count_unique_elements([1, 2, 3, 1, 2, 4, 5, 4]))

"""
Exercise-2: Remove duplicates
Write a function "remove_duplicates(my_list: list) -> list" that takes a list of integers and 
removes all duplicates, returning the new list with unique elements in their original order.

Example:
remove_duplicates([1, 2, 3, 1, 2, 4, 5, 4]) -> [1, 2, 3, 4, 5]
"""

def remove_duplicates(my_list: list) -> list:
    unique_list = list(set(my_list))
    return unique_list
    pass
print(remove_duplicates([1,2,3,1,2,4,5,4]))


"""
Exercise-3: Reverse a list
Write a function "reverse_list(my_list: list) -> list" that takes a list of integers and 
returns a new list with the elements in reverse order.

Example:
reverse_list([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
"""

def reverse_list(my_list: list) -> list:
    my_list.reverse()
    return my_list
    pass
print(reverse_list([1, 2, 3, 4, 5]))


"""
Exercise-4: Find the maximum value in a list
Write a function "max_value(my_list: list) -> int" that takes a 
list of integers and returns the maximum value in the list.

Example:
max_value([1, 2, 3, 4, 6]) -> 6
"""


def max_value(my_list: list) -> int:
    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
print(max_value([1, 2, 3, 4, 6]))

"""
Exercise-5: Find the minimum value in a list
Write a function "min_value(my_list: list) -> int" that takes a 
list of integers and returns the minimum value in the list.

Example:
min_value([1, 2, 3, 4, 5]) -> 1
"""

def min_value(my_list: list) -> int:
    min_value = my_list[0]
    for num in my_list:
        if num < min_value:
            min_value = num
    return min_value
    pass
print(min_value([1, 2, 3, 4, 5]))

"""
Exercise-6: Sum all values in a list
Write a function "sum_values(my_list: list) -> int" that takes a 
list of integers and returns the sum of all values in the list.

Example:
sum_values([1, 2, 3, 4, 5]) -> 15
"""

def sum_values(my_list: list) -> int:
    sum_values = 0
    for num in my_list:
        sum_values += num
    return sum_values
    pass
print(sum_values([1, 2 ,3 ,4 ,5]))

"""
Exercise-7: Find the average of a list
Write a function "average(my_list: list) -> float" that takes a 
list of integers and returns the average value of the list.

Example:
average([1, 2, 3, 4, 5]) -> 3.0
"""

def average(my_list: list) -> float:
    sum_values = 0
    count = 0
    count = len(my_list)

    for num in my_list:
        sum_values += num
    return sum_values / count
    pass
print(average([1,2,3,4,5]))


"""
Exercise-8: Find the index of an element in a list
Write a function "find_index(my_list: list, element: int) -> int" that takes a 
list of integers and an element, and returns the index of the first occurrence of 
the element in the list. If the element is not in the list, return -1.

Example:
find_index([1, 2, 3, 4, 5], 3) -> 2
find_index([1, 2, 3, 4, 5], 6) -> -1
"""

def find_index(my_list: list, element: int) -> int:
    for index,value in enumerate(my_list):
        if value == element:
            return index
    return -1
    pass
print(find_index([1, 2, 3, 4, 5], 6))


"""
Exercise-9: Check if a list is sorted
Write a function "is_sorted(my_list: list) -> bool" that takes a list
of integers and returns True if the list is sorted in non-descending 
order (i.e., each element is greater than or equal to the previous element), 
False otherwise.

Example:
is_sorted([1, 2, 3, 4, 5]) -> True
is_sorted([1, 3, 2, 4, 5]) -> False
"""
def is_sorted(my_list: list) -> bool:
    for i in range(1, len(my_list)):
        if my_list[i] < my_list[i - 1]:
            return False
    return True
print(is_sorted([1, 2, 6, 4, 5]))
print(is_sorted([1, 2, 3, 4, 5]))


"""
Exercise-10: Count the frequency of an element in a list
Write a function "count_frequency(my_list: list, element: int) -> int" that 
takes a list of integers and an element, and returns the number of 
times the element appears in the list.

Example:
count_frequency([1, 2, 3, 4, 5, 1, 2, 3], 3) -> 2
"""

def count_frequency(my_list: list, element: int) -> int:
    count = 0
    for item in my_list:
        if item == element:
            count += 1
    return count
print(count_frequency([1, 2, 3, 4, 5, 1, 2, 3], 3))
"""
Exercise-11: Find the mode of a list
Write a function "find_mode(my_list: list) -> int" that takes a list of 
integers and returns the mode (i.e., the value that appears most frequently) 
of the list. If there are multiple modes, return any of them.

Example:
find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]) -> 2
"""

from collections import Counter

def find_mode(my_list: list) -> int:
    frequency = Counter(my_list)
    return frequency.most_common(1)[0][0]

print(find_mode([1, 2, 3, 4, 5, 1, 2, 2, 3]))

"""
Exercise-12: Remove all occurrences of an element in a list
Write a function "remove_all(my_list: list, element: int) -> list" 
that takes a list of integers and an element, and returns a new list 
with all occurrences of the element removed.

Example:
remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3) -> [1, 2, 4, 5, 1, 2]
"""

def remove_all(my_list: list, element: int) -> list:
    return [item for item in my_list if item != element]

print(remove_all([1, 2, 3, 4, 5, 1, 2, 3], 3))

"""
Exercise-13: Rotate a list to the left by k positions
Write a function "rotate_left(my_list: list, k: int) -> list" that takes a 
list of integers and an integer k, and returns a new list with the elements rotated k positions to the left.

Example:
rotate_left([1, 2, 3, 4, 5], 2) -> [3, 4, 5, 1, 2]
"""
def rotate_left(my_list: list, k: int) -> list:
    k = k % len(my_list)
    return my_list[k:] + my_list[:k]

print(rotate_left([1, 2, 3, 4, 5], 2))


"""
Exercise-14: Rotate a list to the right by k positions
Write a function "rotate_right(my_list: list, k: int) -> list" that 
takes a list of integers and an integer k, and returns a new list 
with the elements rotated k positions to the right.

Example:
rotate_right([1, 2, 3, 4, 5], 2) -> [4, 5, 1, 2, 3]
"""

def rotate_right(my_list: list, k: int) -> list:
    k = k % len(my_list)
    return my_list[-k:] + my_list[:-k]

print(rotate_right([1, 2, 3, 4, 5], 2))


"""
Exercise-15: Find the intersection of two lists
Write a function "find_intersection(list1: list, list2: list) -> list" that 
takes two lists of integers and returns a new list with the elements that are present in both lists.

Example:
find_intersection([1, 2, 3, 4], [3, 4, 5, 6]) -> [3, 4]
"""
def find_intersection(list1: list, list2: list) -> list:
    return [value for value in list1 if value in list2]

print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]))


"""
Exercise-16: Find the union of two lists
Write a function "find_union(list1: list, list2: list) -> list" that takes 
two lists of integers and returns a new list with the elements that are 
present in either list (i.e., the union of the lists).

Example:
find_union([1, 2, 3, 4], [3, 4, 5, 6]) -> [1, 2, 3, 4, 5, 6]
"""
def find_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))

print(find_union([1, 2, 3, 4], [3, 4, 5, 6]))


"""
Exercise-17: Find the difference of two lists
Write a function "find_difference(list1: list, list2: list) -> list" that takes 
two lists of integers and returns a new list with the elements that are 
present in the first list but not the second list.
Assume that list does not contain duplicates.

Example:
find_difference([1, 2, 3, 4], [3, 4, 5, 6]) -> [1, 2]
"""

def find_difference(list1: list, list2: list) -> list:
    pass



