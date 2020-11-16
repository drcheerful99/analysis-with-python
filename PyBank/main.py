# import dependencies
import os
import csv

# set filepath to datasource
filepath = os.path.join("Resources/budget_data.csv")

# read sources file
with open(filepath, 'r) as filesource:
    csvreader = csv.reader(filesource, delimiter=",")
    csvHeader = next(csvreader)

# declare and initialize variables
totalMonths = 0
totalRevenue = 0
maxIncrease = 0
maxDecrease = 0  
avgChange = 0
profitNlosses = []
PorLdates = []

# calculate 
for row in csvreader:
    totalMonths += 1
    profitNlosses.append(int(row[1]))
    totalRevenue += int(row[1])
    PorLdates.append(row[0])

profitNlosses = []
for i in range(1, len(profitNlosses)):
    profitCahnge = profitNlosses[i] - profitNlosses[i-1]
    profitNlosses.append(int(profitCahnge))

for i in range(0, len(profitNlosses)):
    avgChange +=profitNlosses[i]
    averageChange = round(avgChange/(len(profitNlosses,20)))

for profit_loss in profitNlosses:
    if profit_loss == 0:
        maxIncrease == profit_loss
        maxDecrease == profit_loss
    if profit_loss > maxIncrease:
        maxIncrease = profit_loss
    elif profit_loss < maxDecrease:
        maxDecrease = profit_loss

maxIncrease_index = profitNlosses.index(maxIncrease)
maxIncreaseDate = PorLdates(maxIncrease_index)
maxDecrease_index = profitNlosses.index(maxDecrease)
maxDecreaseDate = PorLdates(maxDecrease_index)

# print out 

f = open("analysis/analysis.txt", "w")
print(f"Financial Analysis: \n")
print(f"=================== \n")
print(f"Total Months: {totalMonths}\n")
print(f"Total: {totalRevenue}\n")
print(f"Average Change: {avgChange}\n")
print(f"Greatest Increase in Profits: {maxIncreaseDate}{maxIncrease}\n")
print(f"Greatest Decrease in Profits: {maxDecreaseDate} {maxDecrease}\n")
f.close()