import csv
import re

with open('output.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		if (row.match("BINF") != NULL){
			print(', '.join(row))
		}

p = re.compile('BINF*')
print(p)

