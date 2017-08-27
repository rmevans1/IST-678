import csv

#Open attendees1.csv
f = open('attendees1.csv')

#Create csv object from open file
csv_f = csv.reader(f)

#Create an empty array for attendees 1
attendees1 = []

#loop through attendees1
for row in csv_f:
    #add email to attendees1 array
    attendees1.append(row[2])

#close file
f.close()

#Open attendees2.csv
f = open('attendees2.csv')

#Create csv object from open file
csv_f = csv.reader(f)

#Create an empty array for attendees 2
attendees2 = []

#loop through attendees2
for row in csv_f:
    #add email to attendees2 array
    attendees2.append(row[2])

#close file
f.close()

#convert attendees1 & attendees2 to a set
# a set cannot have duplicate values
attendees1 = set(attendees1)
attendees2 = set(attendees2)

#get difference between attendees2 & attendees1
print(attendees2.difference(attendees1))