import os
import csv

# path to csvfile
csvpath = os.path.join('Resources', 'election_data.csv')

# variables
total_votes = 0
candidate = []
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = []

# Read csvfile
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # For loop to read each row after header
    for row in csvreader:
        total_votes += 1
        candidate.append(row[2])
        if candidate in candidate_candidate_votes:

#print summary
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")

print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")