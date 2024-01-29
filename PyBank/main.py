import os
import csv


#Create function that calculates values of dictionary as integers.  Source:  https://www.techieclues.com/blogs/converting-a-dictionary-to-a-dictionary-of-integers-in-pythony

def convert_to_int_dict(input_dict):
    int_dict = {}
    for key, value in input_dict.items():
        int_value = int(value)
        int_dict[key] = int_value
    return int_dict


#Create function that calculates the average of a specified dictionary.  Source:  https://www.tutorialspoint.com/How-to-sum-values-of-a-Python-dictionary

def averageoflist(input):
    
    denominator = len(input)
    average = sum(input)/denominator

    return average

#Create new file for results output

absolute_pathnewfile = os.path.dirname(__file__)
relative_pathnewfile = "analysis/results.txt"
newfilepath = os.path.join(absolute_pathnewfile, relative_pathnewfile)

with open(newfilepath, "w") as textfile:
    textfile.close
    
#Open csv file and store it in budget_data variable as dictionary

absolute_pathcsv= os.path.dirname(__file__)
relative_pathcsv = "Resources/budget_data.csv"
csvpath = os.path.join(absolute_pathcsv, relative_pathcsv)

with open(csvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   budget_data = dict(csvreader)

#Remove header key
budget_data.pop("Date")

#convert string values to integers 
Revisedbudget_data = convert_to_int_dict(budget_data)

#Create list to isolate dictonary values using loop
LossProfitDiff = []
x = 0

for value in Revisedbudget_data.values():
    LossProfitDiff.insert(x, value)
    x = x + 1

#Create list to isolate dictonary keys using loop
Keys = []
x = 0

for key in Revisedbudget_data.keys():
    Keys.insert(x, key)
    x = x + 1

Keys.pop(0)

#make list of differences by profit/loss
RevLossProfitDiff = []

for i in range(1, len(LossProfitDiff)):
    value2 = LossProfitDiff[i]
    value1 = LossProfitDiff[i-1]
    result = value2 - value1
    RevLossProfitDiff.append(result)


#Create a new dictonary from the split lists:  https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
Sortdict = dict(zip(Keys, RevLossProfitDiff))

#Sort the list in ascending order to find greatest decrease: https://realpython.com/sort-python-dictionary/
SortdictDecrease = dict(sorted(Sortdict.items(), key=lambda item: item[1]))

#Sort the list in descending order to find greatest increase: https://realpython.com/sort-python-dictionary/
SortdictIncrease = dict(sorted(Sortdict.items(), key=lambda item: -item[1]))

Average = round(averageoflist(RevLossProfitDiff), 2)

TotalMonths = len(budget_data)

Total = sum(Revisedbudget_data.values())

#Print results to terminal
print(f"Financial Analysis",)
print(f"-----------------",)
print(f"Total Months: {TotalMonths}")
print(f"Total: ${Total}")
print(f"Average: ${Average}")
print(f"Greatest Increase in Profits: {list(SortdictIncrease.keys())[0]} (${list(SortdictIncrease.values())[0]})")
print(f"Greatest Decrease in Profits: {list(SortdictDecrease.keys())[0]} (${list(SortdictDecrease.values())[0]})")
    

#Print results to file
with open(newfilepath, "a") as textfile:
    print(f"Financial Analysis", file=textfile)
    print(f"-----------------", file=textfile)
    print(f"Total Months: {TotalMonths}", file=textfile)
    print(f"Total: ${Total}", file=textfile)
    print(f"Average: ${Average}", file=textfile)
    print(f"Greatest Increase in Profits: {list(SortdictIncrease.keys())[0]} (${list(SortdictIncrease.values())[0]})", file=textfile)
    print(f"Greatest Decrease in Profits: {list(SortdictDecrease.keys())[0]} (${list(SortdictDecrease.values())[0]})", file=textfile)
    textfile.close


