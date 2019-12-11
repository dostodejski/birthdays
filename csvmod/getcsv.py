from mypackage.birthdays import birthdays
import csv
toCSV = [birthdays]
keys = toCSV[0].keys()

with open('birthdays.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(toCSV)
