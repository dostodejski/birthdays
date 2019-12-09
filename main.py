#! /usr/bin/env python3

import argparse
from mypackage.birthdays import return_birthday
parser = argparse.ArgumentParser(description='These are the birthdays of famous people')
#define arguments
parser.add_argument('-b', action= "store_true", default=None)
parser.add_argument("-v", "--verbose", action="store_true")
#parser.add_argument('--Alan Turing', help= 'Alan Turing is not in this list')
#ciao=return_birthday('Albert Einstein')
args = parser.parse_args()
ciao= input('Inserisci il nome di uno scienziato:', type=str)
print ('La sua data di nascita è:', return_birthday(ciao))
#return_birthday


