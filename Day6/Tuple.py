# Tuple is a collection of different types of data which is ordered and unchangeable.
# Tuple can hold strings, Integers, lists.

# Create an empty Tuple
empty_tuple = ()
# or another syntax
empty_tuple = tuple()

# Tuple with values
test_tuple = (1, "hello", [1, 2, 3])

#tuple length
print(len(test_tuple))

# Accessing Tuple Items
first_tuple = test_tuple[0]
second_tuple = test_tuple[1]
Last_tuple = test_tuple[2]
print(first_tuple)
print(second_tuple)
print(Last_tuple)

# Slicing tuples (range)
print(test_tuple[1:3])

# Change Tuple to list, append
fruits = ('Banana', 'Orange', 'Melon', 'Avocado')
lst = list(fruits)
lst.append('Berry')
print(lst)

# checking for item in tuple
exist = 'Orange' in fruits
print(exist)

# joining tuples
fruits_n_tuple = fruits + test_tuple
print(fruits_n_tuple)

# delete tuble
del fruits_n_tuple