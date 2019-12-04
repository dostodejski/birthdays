import sys


if len(sys.argv) > 1:
    to_print = sys.argv[1]
else:
    print("Give me an argument to print")
    exit()

print("The name of this program is {}".format(sys.argv[0]))
print("You entered {}".format(to_print))
