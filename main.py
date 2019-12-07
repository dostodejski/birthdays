#! /usr/bin/env python3
import argparse
parser = argparse.ArgumentParser(description='These are the birthdays of Albert Einstein and Alan Turing')
#define arguments
parser.add_argument('Albert Einstein', help='Albert Einstein was a physicist')
parser.add_argument('--Alan Turing', help= 'Alan Turing was a scientist')
args = parser.parse_args()

from mypackage.birthdays import return_birthday

return_birthday('Albert Einstein')
return_birthday('Alan Turing')
