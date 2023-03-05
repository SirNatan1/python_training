# A function in Python is a block of reusable code which means, we can define a function and call it at any point you need
# It will allow to break the code into smaller modular pieces, which can help keep the code more organized
# define a function syntax:
#    def function_name():
#         codes
#         codes
#  function_name()   # calls the function, If you dont call the function it will not be executed

# function without params
def full_name():
    First_name = 'Nate'
    Last_name = 'Ira'
    Space = ' '
    full_name = First_name + Space + Last_name
    print(full_name)
full_name()

def calc():
    num_one = 1
    num_two = 2
    toatl = num_one + num_two
    print(toatl)
calc()

# Function that returns a value
# Function can also return values, meaning, it will execute the tasks inside it and will save the value.
# Functions with values are defined with the 'return' statement which specifies the value that the function will return
# The returned value can be assigned to a variable, used in an expression, or passed as an argument to another function
# If the function doesnt have a value it will print out 'None'
def genereate_full_name():
    first_name = input('please enter a name: ')
    last_name = input('please enter a last name: ')
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(genereate_full_name())

def calcu():
    NumOne = int(input('Please enter a number to add to: '))
    NumTwo = int(input('Please enter the number you want to add: '))
    result = NumOne + NumTwo
    return result
print(calcu())


# Function with Params:
# Similar to values we can also pass different data types as Parameters
# You define the parameter in the () of the function defined, after it you will pass give the param the value
# the function will execute the whole code segment and will use the given value
def greet(name):
    message = name + ', Welcome home!'
    return message
print(greet('Dante'))
# above we can see that the name was the parameter and  when we called the function we mentioned the value that is needed

def add_ten(num):
    ten = 10
    return num + ten
number = int(input('Please write a number: '))
print(add_ten(number))
# I've added an input option above
