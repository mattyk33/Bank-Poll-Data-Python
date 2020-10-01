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