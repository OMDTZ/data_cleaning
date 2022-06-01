import sys, os
import csv

infile = open(sys.argv[1])
reader = csv.reader(infile)
data = list(reader)
headers=data.pop(0)

   
outfile = open('example.csv','w')
writer = csv.writer(outfile)

for row in data:
    energy = ''
    if row[14].lower() == 'grid_luku':
        energy = 'Electricity'
    else:
        energy = row[14]
    newrow = []
    newrow.extend(row[0:14])
    newrow.append(energy)
    newrow.extend(row[14][15:])
    writer.writerow(newrow)
    
