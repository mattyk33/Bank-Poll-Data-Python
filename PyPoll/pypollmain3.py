import os
import csv

# path to csvfile
csvpath = os.path.join('Resources', 'election_data.csv')

# variables

total_votes = 0
candidates = []
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = 0

# Read csvfile
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # For loop to read each row after header
    for row in csvreader:
        total_votes += 1
        candidates.append(row[2])

        # Conditional to count votes
        for i in row[2]:
            if i in candidates:
                candidate_index = candidates.index(i)
                candidate_votes.update(i = (candidate_index +1))
            else:
                candidates.append(i)
                candidate_votes.update({i: 1})

# For loop to calculate candidate percentages
for i, votes in candidate_votes:
    candidate_percentages[i] = (round((votes/ total_votes), 2)) * 100
    candidate_percentages.update({i, candidate_percentages[i]})

    if votes > winner_votes:
        winner_votes = votes
        winner = i

#print summary
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
print(f"{i}: {candidate_percentages[i]} ({votes})")
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")