#! /usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description='Write text into the file')
#define arguments
parser.add_argument(action="store_true")
parser.add_argument(choices=[])
args = parser.parse_args()

from mypackage.birthdays import return_birthday

return_birthday('Albert Einstein')
return_birthday('Alan Turing')
