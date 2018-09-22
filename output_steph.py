import csv
import re
with open('output.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		result = prog.search(row)
		if (result):
		    print (result)
