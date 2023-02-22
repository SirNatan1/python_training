# A for loop is used to iterate over a sequence, such as a list, tuple, or string. The loop executes a set of statements
# for each item in the sequence, and the variable that holds the current item changes on each iteration.
num = [0, 1, 2]
for number in num:  # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)  # the numbers will be printed line by line, from 0 to 5
# another example 'for' loop with a string
lang = input('enter the language: ')
for letter in lang:
    print(letter) # this will print each letter by itself since we created an iteration
for i in range(len(lang)):
    print(lang[i]) # this will also print each letter in a new line, as we have created a index var which will print all the letters in the range

# A loop with a tuple
tple = (3, 4, 5, 6, 7)
for numb in tple:
    print(numb)

# A for loop with dictionary, gives you the key of the dictionary
name = {
    'name':'Nate',
    'Last_name':'Iki',
    'age':'120',
    'Status':'alive',
    'Skills':['Eat', 'Sleep', 'Python'],
    'marrige':'no'
}
for key in name:
    print(key) #this will print out all the keys
for key, value in name.items():
    print(key, value)   # this will print all keys and their values since we also use the .items() this returns a view object containing the key-value pairs of the dictionary as tuples.

# Loops in a set
comps = input('Enter at least 3 comapny names, make sure to seperate with a coma: ')
split = comps.split(",")  # converts string into list
usr_set = set(split)  # converts list into set
for company in usr_set:
    print(company)

# Breaks and continues
n = (0,1,2,3,4)
for numba in n:
    print(numba)
    if numba == 3:
        break
# we can take from above that the loop stops when it reaches 3
# With the continue statement we can skip the current iteration, and continue with the next:
c = (0,1,2,3,4,5)
for nu in c:
    print(nu)
    if num == 3:
        continue
    print('the next number is:', nu + 1) if nu != 5 else print("loop's end")
print('outside the loop')

# Range functions
lst = list(range(11)) # creating a variable which is a list range from 0 to 10
print(lst) # this will print out the value which is the list from 0 to 10
st = set(range(1, 11)) # 2 arguments indicate start and end of the sequence, step set to default 1
print(st)


