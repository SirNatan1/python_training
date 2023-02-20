# By default python scripts are executed from top to bottom.
# This can be altered in two ways:
# Conditional execution: a block of one or more statements will be executed if a certain expression is true
# Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true

# If condition
# In Python, if is used to check if a condition is true and to execute the block code.
# Indentation is important
a = int(input('enter a number: '))
if a > 0:
    print('A is a positive num')

#If Else
# If the 'if' condition exists then it will run the first section, if not it'll move to the else section
# 'else' dosent have a condition as it will be a result of something that dosent exist in if

fruit = 'banana'
veggie = 'cucamber'
if fruit == 'banana':
    print('''this is a fruit, it's a''', fruit)
else:
    print('this is not a fruit it might be a:', veggie)

# If elif
# 'elif' is a continuation of 'if', and unlike else, it uses a condition.
# if a condition will not exist in 'if' it'll move next, to 'elif' condition, from there it can go either to another elif or to else or end
fruits = ['banana', 'orange', 'melon', 'strawberry', 'lemon', 'kiwi', 'apple', 'pear', 'peach', 'cherry']
veggies = ['cucamber', 'pepper', 'tomato', 'carrot', 'potato', 'avocado', 'raddish']
test = input('enter a fruit or a veggie: ')
if test in fruits:
    print('this is a fruit')
elif test in veggies:
    print('this is a veggie')
else:
    print('this is unkown thing')

# short ver
b = 3
print('A is positive') if b > 0 else print('B is negative')

# Nested Conditions
# when a conditional statement (if/elif/else) is placed inside another conditional statement, this allows to create more complex condition logic
# in this example we can see that the firsst if section has a condition and if it's met there's another condition nested inside of it
x = int(input('enter the value for x: '))
y = int(input('enter the value for y: '))
if x > 0:
    if y > 0:
        print("Both x and y are positive.")
    else:
        print("x is positive but y is not.")
else:
    print("x is not positive.")

# If condition with logical operators
# it's possible to use a logical operator in a condition I used it in the elif section
# another example
num = int(input('enter a number: '))
if num > 0 and num % 2 == 0:
    print('the number is even and positive')
elif num > 0 and num % 2 != 0:
    print('the number is a possitive int')
elif num == 0:
    print('the number is 0')
else:
    print('the number is negative')

# If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')