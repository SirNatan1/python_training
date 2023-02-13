# declare an empty list
empty = []

# Declare a list with more than 5 items
fruits = ['Banana', 'Apple', 'Kiwi', 'Berry', 'Cherry']

# Find the length of your list
print('Num of fruits: ', len(fruits))

#Get the first item, the middle item and the last item of the list
first_fruit = fruits[0]
middle_fruit = fruits[1:4]
last_fruit = fruits[4]
print('the first fruit in the list is:', first_fruit)
print('the fruits in the middle are:', middle_fruit)
print('the last fruit in the list is:', last_fruit)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data = ['nat', '25', '1.80', 'male', 'IL']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print('The number of companies is: ', len(it_companies))

# Print the first, middle and last company
first_comp = it_companies[0]
middle_comp = it_companies[3]
last_comp = it_companies[6]
print('the first company:', first_comp)
print('the middle company:', middle_comp)
print('the last company:', last_comp)

# Print the list after modifying one of the companies
it_companies[0] = 'SAP'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('TCS')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(3, 'capgemini')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4] = 'APPLE'
print(it_companies)

# Check if a certain company exists in the it_companies list.
does_exist = 'IBM' in it_companies
print(does_exist)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
it_companies.clear()
print(it_companies)
