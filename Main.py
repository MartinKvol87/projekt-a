import csv

file = open("MerakiData.csv")

# Læser CSV filen fra Meraki Dashboard
csvReader = csv.reader(file)

header = []
header = next(csvReader)

rows = []
for row in csvReader:
    rows.append(row)
file.close()


