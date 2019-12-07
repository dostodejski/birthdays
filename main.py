#! /usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description='Write text into the file')
#define arguments
parser.add_argument('Albert Einstein', choices[], help='Birthday of Albert Einstein' )
#parser.add_argument('Alan Turing', action='store_true', help= 'Birthday of Alan Turing')
args = parser.parse_args()

from mypackage.birthdays import return_birthday

return_birthday('Albert Einstein')
return_birthday('Alan Turing')
