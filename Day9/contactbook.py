# Contact Book: Create a command-line tool to manage contacts that uses a dictionary to store information such as name, email, phone number, and address.
# create a contact book which will print out the contact, if it will not be found add conditinals for it.

def contactbook():

    names = {'Ethan':{
        'Name':'Ethan',
        'Last Name':'Joey',
        'Phone Num':'12345667',
        'Address':{
          'Country':'England',
          'City':'Wels',
          'Street':'Oxford'
        }
    },
    'Marco':{
        'Name':'Marco',
        'Last Name':'Polo',
        'Phone Num':'12345667',
        'Address':{
          'Country':'Italy',
          'City':'Venice',
          'Street':'Piazza'
        }
    },
    'Bilbo':{
        'Name':'Bilbo',
        'Last Name':'Baggins',
        'Phone Num':'12345666',
        'Address':{
          'Country':'Gondor',
          'City':'Ragadon',
          'Street':'Bay'
        }
    },
    'Ed':{
        'Name':'Ed',
        'Last Name':'She-ran',
        'Phone Num':'12345666',
        'Address':{
          'Country':'Canada',
          'City':'Montreal',
          'Street':'Maple'
        }
    },
    'Leo':{
        'Name':'Leo',
        'Last Name':'Nardo',
        'Phone Num':'12345666',
        'Address':{
          'Country':'Uganda',
          'City':'yes',
          'Street':'yes'
        }
    }}

    name = input('''Please enter a name you're looking for, dont forget to start with capital: ''')

    if name in names:
        print(names[name])
    else:
        print('This name dosent exist in the contactbook')

contactbook()