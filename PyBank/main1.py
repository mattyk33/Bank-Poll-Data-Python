import os
import csv

# path to csvfile
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# variables
total_months = 0
net_profit = 0
month_change = 0
total_month_change = 
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Read csvfile
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # For loop to read each row after header
    for row in csvreader:
        total_months +=1
