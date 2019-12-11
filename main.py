#! /usr/bin/env python3

import argparse
<<<<<<< HEAD
from mypackage.birthdays import birthdays, return_birthday

=======
>>>>>>> b950932c1f5be427ec29b1ab8145b389437791c7
parser = argparse.ArgumentParser(description='program that gives back birthdays of scientists')
#define arguments
parser.add_argument("name", help= "insert one of the scientist name of the #list", type=str, default=None)
parser.add_argument("--birthdays", type=str, help="Names inside the birthday dictionary", choices = ["Albert Einstein", "Benjamin Franklin", "Ada Lovelace", "Donald Trump", "Rowan Atkinson"])
args = parser.parse_args()
<<<<<<< HEAD

risultato = return_birthday(args.name)
=======
result = return_birthday(args.name)
>>>>>>> b950932c1f5be427ec29b1ab8145b389437791c7





