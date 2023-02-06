fruits = ['banana', 'orange', 'mango', 'lemon']
# defineing a list into a var
first_fruit = fruits[0]
# defining a var that will take the 0 value in the list which is banana
last_fruit = fruits[-1]
# defining a var which will get its value from the last
fruit_range = fruits[1:]
#this defines the range of the 1 fruit untill the last
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
print(first_item)
print(rest)

#another example
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
# We defined a list that puts the value in co-responding var the *rest goes untill the end
# only if theres a var defined after it in which defaultly take the values of the last in the list
print(rest)
print(tenth)
