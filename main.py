#! /usr/bin/env python3
birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def return_birthday(name):
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

import argparse
#from mypackage.birthdays import return_birthday
parser = argparse.ArgumentParser(description='program that gives back birthdays of scientists')
#define arguments
parser.add_argument("name", help= "scientist name")
#parser.add_argument("birthdays",)
#parser.add_argument('--Alan Turing', help= 'Alan Turing is not in this list')
#ciao=return_birthday('Albert Einstein')
args = parser.parse_args()
risultato = args.birthdays[name]
print (risultato)


