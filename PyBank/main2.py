import os
import csv

# path to csvfile
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# variables
total_months = 0
net_profit = 0 
current_month_profit = 0
previous_month_profit = 0
profit_change = 0
profit_changes = []
months = []

# Read csvfile
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader, none)

    # For loop to read each row after header
    for row in csvreader:
        total_months +=1
        months.append(row[0])
        net_profit += int(row[1])
        current_month_profit = int(row[1])
        if total_months > 1:
            profit_change = current_month_profit - previous_month_profit
            profit_changes.append(profit_change)
            previous_month_profit = current_month_profit






