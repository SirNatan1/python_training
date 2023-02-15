# Set is a collection of items. Set is a collection of unordered and un-indexed distinct elements.
# In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
# To create a set, you can use the set() function or enclose a comma-separated list of elements within curly braces { }
# The diffrence between set and a tuple: Tuples are immutable, which means that once a tuple is created, you can't add, remove, or modify elements in it. Sets allow changes and mods
# Ordering: Tuples are ordered items in a tuple can be accessed by index. Sets are unordered the items cant be accessed by index.
# Duplication: Tuples can contain duplicate values, while sets can't.
# Syntax: Tuples are defined using parentheses () and commas, while sets are defined using curly braces {}.

# empty set
st = {}
# or
stt = set()

fruit = {'Banana', 'Melon', 'Berry', 'Cherry', 'Burger'}
print(fruit)

# set length
print(len(fruit))

# checking for an item
exist = 'Melon' in fruit
print(exist)
not_exist = 'Avocado' in fruit
print(not_exist)

# Adding item (not possible to change since we cant index)
fruit.add('Lime')
print(fruit)

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
vegies = {'Brocoli', 'Potato', 'Onion', 'Carrot'}
# or 
# vegies = {['Brocoli', 'Potato', 'Onion', 'Carrot']}
# fruit.update(vegies)
# print(fruit)

# remove item from set, the pop() remove a random item from a list and it returns the removed item.
# fruit.remove('Banana')
# print(fruit)
# fruit.pop()
# print(fruit)

# Clearing a set
# vegies.clear()
# Or
# removed_item = vegies.clear()

# Deleting a set
del st

# Converting a list to a set, notice that in set we are not able to see duplication
lst = ['item1', 'item2', 'item3', 'item4', 'item3', 'item4']
sets = set(lst)
print(sets)

# We also can join sets, unlike the update function it will cojoint 2 sets into a 3rd one.
vegies_n_fruits = fruit.union(vegies)
print(vegies_n_fruits)

# Intersection, returns a set of items which are included in the 2 mentioned sets
test = {'pizza', 'cheese', 'dough', 'sauce', 'toping'}
test2 = {'oven', 'pizza', 'heat', 'bread', 'dough'}
# test3 = test.intersection(test2)
# also possible
test3 = test & test2
print(test3)

# Subset and Super Set, a set A is considered a subset of another set B if all elements of set A are also elements of set B.
whole_num = {0, 1, 2, 3, 4, 5, 6, 7, 8}
even_num = {2, 4, 6, 8}
some_num = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(whole_num.issubset(even_num))
# print(whole_num.issuperset(even_num))
# sub = whole_num.issubset(even_num)
# superr = whole_num.issuperset(even_num)
# print(sub)
# print(superr)
print(even_num.issubset(whole_num))
print(even_num.issuperset(whole_num))

# Checking the Difference Between Two Sets, returns a new set that contains all the elements that are in the first set but not in the second set.
print(whole_num.difference(even_num))

# Symmetric Difference Between Two Sets, returns a new set that contains all the elements that are in either the first or second set, but not in both.
print(whole_num.symmetric_difference(some_num))

#Joining Sets. If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
jointtest = whole_num.isdisjoint(even_num)
print(jointtest) #returns false because there are common items
