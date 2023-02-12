fruits = ['banana', 'orange', 'mango', 'lemon']
# defineing a list into a var
first_fruit = fruits[0]
# defining a var that will take the 0 value in the list which is banana
last_fruit = fruits[-1]
# defining a var which will get its value from the last
fruit_range = fruits[1:]
#this defines the range of the 1 fruit untill the last without 0 which is the first value
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print(first_fruit)
print(last_fruit)
print(fruit_range)

#another way to define list is as such
lst = ['item','item2','item3', 'item4', 'item5']
# a defined list in a var
first_item, second_item, third_item, *rest = lst
# each new defined var will take its value to the co responding location in the list, *rest takes all
# this method is called unpacking
print(first_item)
print(rest)

#another example
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
# We defined a list that puts the value in co-responding var the *rest goes untill the end
# only if theres a var defined after it in which defaultly take the values of the last in the list
print(rest)
print(tenth)

# modify list, this will change the coresponding value
fruits[0] = 'pataya'
print(fruits)
fruits[1] = 'Pineapple'
print(fruits[1])

# checking item in list using "in" operator
# If we would to put this var in the begining we would get a True result
doesnt_exist = 'banana' in fruits
print(doesnt_exist)
does_exist = 'pataya' in fruits
print(does_exist)

# adding item to list using append, each item is added to the end of the list
fruits.append('Melon')
print(fruits)

# inserting item to list using insert, its done by adding the specific location of the desired item
fruits.insert(2, 'Orange')
fruits.insert(4, 'Berry')
print(fruits)

# remove item from list using remove, specify which item on the list will be removed
fruits.remove('Orange')
print(fruits)

# remove item using POP by specifing index, if empty it removes the last item in list
fruits.pop(3)
print(fruits)

# removing using del, del allows deletion of the specified values (can be a value, range or the whole list)
del fruits[0:2]
print(fruits)
del fruits[1]
print(fruits)
# del fruits
# print(fruits) this will result an error because now theres no such list

#copying a list by specifing the name of the new list and the name of the list we want to copy
lst2 = lst.copy()

# clearing a list, will empty the values inside the list
lst.clear()
print(lst)
print(lst2)

# joining list with + appender (also possible with .extend), this will combine the items in the exising lists into the new list
lst.insert(0, 'Table')
lst.insert(1, 'Chair')
lst.insert(2, 'Aireplane')
lst.insert(3, 'Sack')
lst3 = lst + lst2
print(lst3)

# counting the number of times the item in a list
print(lst.index('Chair'))
print(lst2.index('item2'))

# reversing the list
lst3.reverse()
print(lst3)

# sorting
lst.sort() # will sort the list in alphabetic order
print(lst)
lst.sort(reverse=True) # will reverse the order
print(lst)
print(sorted(lst)) # will also sort in order