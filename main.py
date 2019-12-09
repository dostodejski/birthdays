#! /usr/bin/env python3
import argparse
#from mypackage.birthdays import return_birthday

#return_birthday('Albert Einstein')
#return_birthday('Alan Turing')

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)


def return_birthday(name):
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

parser = argparse.ArgumentParser(description='These are the birthdays of famous people')
#define arguments
parser.add_argument('name', help='it is his birthday', type= str)
#parser.add_argument('--Alan Turing', help= 'Alan Turing is not in this list')
args = parser.parse_arg
print (args.return_birthday(name))

