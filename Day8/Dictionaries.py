# A dictionary is a collection of unordered, modifiable and paired (key: value) data type.
# a dict can hold values as: lists, tuples and sets
empty_dic = {}
dct = {'key':'value', 'test':'testing', 'hey':'hello', 'booking':'book'}
full_dict = {
    'list':['Alist', 'hey', 'test'],
    'set':{'aSet', 'banana', 2},
    'tuple':('AtuPle', 'eskimo', 4)
}
print(len(dct))  # prints the amount of items in dict
print(full_dict)

# We can also create a dict inside a dict and organize it in such way:
person = {
    'first_name':'Nat',
    'last_name':'Ir',
    'age':25,
    'profession':'Dev',
    'is_merried':'No',
    'address': {
      'street':'XYZ',
      'ZIP':'1234'
    }
}
print(person)
print(person['address']) # print value for spec key
print(person.get('age')) # this will be the correct way to utilize the above, if the address key is missing it'll result an error

# add key and value and add new value to existing key
person['pets'] = 'dog' # will add it to the bottom of the dict
person['skills'] = ['Linux', 'Aws', 'script']
person['skills'].append('python')
print(person)

# to change a value in one of the keys
person['first_name'] = 'Nate'

# checking for a key in Dict using in opertaor
print('address' in person)

# removing key and value 
person.pop('last_name') # will pop the mentioned key
last = person.popitem() # will pop the last key and value
del person['is_merried'] # this will delete the key and value
print(person)
print(last) # printing the poped item

# copy dict
person_copy = person.copy()

# clear a dict, will leave an empty directory
person.clear()
print(person)

# delete a dir, the copied dict will remain
del person
print(person_copy)

# creating a list of values
val = person_copy.values()
print(val)