#! /usr/bin/env python3
birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def return_birthday(name, birth):
    birth= birthdays[name]
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birth))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

import argparse
#from mypackage.birthdays import return_birthday
parser = argparse.ArgumentParser(description='program that gives back birthdays of scientists')
#define arguments
parser.add_argument("birth", help= "scientist name")
#parser.add_argument("-v",)
#parser.add_argument('--Alan Turing', help= 'Alan Turing is not in this list')
#ciao=return_birthday('Albert Einstein')
args = parser.parse_args()
risultato = args.birth
print (risultato)


