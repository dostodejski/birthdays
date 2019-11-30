
'''


The goal of this module is to create a dictionary that associated famous people to their birthday. It will be the list of VIPs used in the main.py function. 

'''

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def print_birthdays():
    #This function will print the name of all the people in the dictionary
    #birthdys	
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    #This function will return the birthday of the desired person,
    #if that person is not in the list it will give a notice to the end-user
    #with a message.
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))
