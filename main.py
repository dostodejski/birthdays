#! /usr/bin/env python3

import argparse
from mypackage.birthdays import return_birthday
parser = argparse.ArgumentParser(description='program that gives back birthdays of scientists')
#define arguments
parser.add_argument("name", type=str, help= "scientist name")
#parser.add_argument("-v",)
#parser.add_argument('--Alan Turing', help= 'Alan Turing is not in this list')
#ciao=return_birthday('Albert Einstein')
args = parser.parse_args()
risultato = args.name
print (risultato)
#ciao= input('Inserisci il nome di uno scienziato:')
#return_birthday(ciao)
#print ('La sua data di nascita è:', blu)
#return_birthday


