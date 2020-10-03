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
        i = (row[2])

        # Conditional to count votes
        if i in candidate_votes:
            candidate_votes[i] += 1
        else:
            candidate_votes[i] = 1

# print summary
save_file = "election_data" + "_results.txt"
csvpath = os.path.join("Analysis", save_file)
with open(csvpath,'w') as text:
    print("Election Results")
    text.write("Election Results" + "\n")

    print("-----------------------------")
    text.write("------------------------------" + "\n")

    print(f"Total Votes: {total_votes}")
    text.write(f"Total Votes: {total_votes}" + "\n")

    print("-----------------------------")
    text.write("------------------------------" + "\n")

    # For loop to calculate candidate percentages
    for key, votes in candidate_votes.items():
        percent = round(((votes/total_votes)*100), 3)
        print(f"{key}: {percent}% ({votes})")
        text.write(f"{key}: {percent}% ({votes})" + "\n")
    
        # Conditonal to find winner
        if votes > winner_votes:
            winner_votes = votes
            winner = key
    print("-----------------------------")
    text.write("------------------------------" + "\n")

    print(f"Winner: {winner}")
    text.write(f"Winner: {winner}" + "\n")

    print("-----------------------------")
    text.write("------------------------------" + "\n")