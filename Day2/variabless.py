
# Variables in Python

first_name = 'Natan'
last_name = 'Ir'
country = 'IL'
city = 'Rishon'
age = 69
is_married = False
skills = ['Banana', 'Python']
person_info = {
    'firstname':'Natan', 
    'lastname':'Ir', 
    'country':'IL',
    'city':'Rishon'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married, is_light_on = 'Natan', 'Ir', 'Israhel', 69, False, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
print('is light on?', is_light_on)

print(type(first_name))
print(type(person_info))
print(type(is_married))
print(len(first_name))    #print length of var

num_one, num_two = 5, 4     #set 2 vars
num_three = num_one + num_two       #sum of the 2 vars
print(num_three)        #print the var of the sum

num_four = num_one - num_two
print(num_four)

num_five = num_one * num_two
print(num_five)

num_six = num_one / num_two
print(num_six)

num_seven = num_one % num_two
print(num_seven)

num_eight = num_one ** num_two
print(num_eight)

# pi = 3.14
# radius = float(input("radius:"))
# A = pi * radius ** 2
# print("the area is:", A)

name = input('name: ')
last_name = input('last name:')
age = input('age: ')
print(name, last_name, age)
