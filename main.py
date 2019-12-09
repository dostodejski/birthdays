#! /usr/bin/env python3
import argparse
from mypackage.birthdays import return_birthday

return_birthday('Albert Einstein')
return_birthday('Alan Turing')

parser = argparse.ArgumentParser(description='These are the birthdays of Albert Einstein and Alan Turing')
#define arguments
parser.add_argument('birthdays', help='it is his birthday', type= str)
parser.add_argument('--Alan Turing', help= 'Alan Turing is not in this list')
args = parser.parse_args()

