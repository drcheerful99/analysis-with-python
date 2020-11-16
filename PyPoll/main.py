# import dependencies
import os
import csv

# set path of the file
filepath = os.path.join("Resources/election_data.csv")
# print(filepath)

with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader = next(csvfile)

# declare various of variables for output:
candidates = {}
counts = 0
votesCast = 0
pct_of_votes = 0
most_votes = 0 


# count total # of votes cast
for row in csvreader:
    candidate = row[2]
    count += 1
    if candidate in candidates.keys():
        candidates[candidate] += 1
    else:
        candidates[candidate] = 1 

# count votes for each candidate
for candidate in candidates:
    votesCast += candidates[candidate]

    pct_of_votes =(((candidates[candidate])/ counts * 100),2)

    if candidates[candidate] > most_votes:
        winner = candidates
        most_votes = candidates[candidate]
 
print("Election Results")
print("-------------------------------")
print(f"Total Votes: {count}")
print("-------------------------------")
print(f"{candidate}: {int(pct_of_votes)} % {votesCast}")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")   


