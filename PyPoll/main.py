import csv
import os

#Create new file for result publishing

absolute_pathnewfile = os.path.dirname(__file__)
relative_pathnewfile = "analysis/electionresults.txt"
newfilepath = os.path.join(absolute_pathnewfile, relative_pathnewfile)

with open(newfilepath, "w") as textfile:
    textfile.close

#Open election data
absolute_pathcsv= os.path.dirname(__file__)
relative_pathcsv = "Resources/election_data.csv"
csvpath = os.path.join(absolute_pathcsv, relative_pathcsv)


with open(csvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   election_data = list(csvreader)

# Flatten nested import result to one set of list indexes. Source: https://www.geeksforgeeks.org/python-flatten-list-to-individual-elements/

flattenedelection = []
for index in election_data:
    for subindex in index:
        flattenedelection.append(subindex)

# Make list that contains only election names
ElectionNames = []
for name in range(2, len(flattenedelection), 3):
    ElectionNames.append(flattenedelection[name])

ElectionNames.pop(0)

# Make list that contains only election IDs
ElectionIDs = []
for ID in range(0, len(flattenedelection), 3):
    ElectionIDs.append(flattenedelection[ID])

ElectionIDs.pop(0)

#Calculate results and stor them in variables for printing
CountCharles = ElectionNames.count("Charles Casper Stockham")
CountDiana = ElectionNames.count("Diana DeGette")
CountRaymon = ElectionNames.count("Raymon Anthony Doane")
Total = len(ElectionNames)

PercentCharles = round(CountCharles/Total * 100, 3)
PercentDiana = round(CountDiana/Total * 100,3)
PercentRaymon = round(CountRaymon/Total *100, 3)

#Determine winner from results
if PercentRaymon > PercentCharles and PercentRaymon > PercentDiana:
    Winner = "Raymon Anthony Doane"
elif PercentCharles > PercentDiana and PercentCharles > PercentRaymon:
    Winner = "Charles Casper Stockham"
else:
    Winner = "Diana DeGette"

      

#Print results to terminal
print(f"Election Results")
print(f"-----------------")
print(f"Total Votes: {Total}")
print(f"-----------------")
print(f"Charles Casper Stockham: {PercentCharles}% ({CountCharles})")
print(f"Diana DeGette: {PercentDiana}% ({CountDiana})")
print(f"Raymon Anthony Doane: {PercentRaymon}% ({CountRaymon})")
print(f"-----------------")
print(f"Winner: {Winner}")
print(f"-----------------")
    

#Print results to file
with open(newfilepath, "a") as textfile:
    print(f"Election Results", file=textfile)
    print(f"-----------------", file=textfile)
    print(f"Total Votes: {Total}", file=textfile)
    print(f"-----------------", file=textfile)
    print(f"Charles Casper Stockham: {PercentCharles}% ({CountCharles})", file=textfile)
    print(f"Diana DeGette: {PercentDiana}% ({CountDiana})", file=textfile)
    print(f"Raymon Anthony Doane: {PercentRaymon}% ({CountRaymon})", file=textfile)
    print(f"-----------------", file=textfile)
    print(f"Winner: {Winner}", file=textfile)
    print(f"-----------------", file=textfile)
    textfile.close