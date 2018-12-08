import csv
import os

# * In this challenge, you are tasked with creating a Python script for analyzing the 
# financial records of your company. You will give a set of financial data called 
# [budget_data.csv](PyBank/Resources/budget_data.csv). 

budget_csv_path = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    # skip header row

    csv_reader = next(csv_reader)
   #  The total number of months included in the dataset - would be a rowcount of the file minus the header

    csv_data = list(csv.reader)
    TotalPFDates = len(csv_data) - 1

    # Read through each row of data after the header

    for row in csv_reader:

#   * The total net amount of "Profit/Losses" over the entire period
        TotalPL = TotalPL + row[2]

    print(f"Total Months: {TotalPFDates}")
    print(f"Total PL: {TotalPL}")

#   * The average change in "Profit/Losses" between months over the entire period
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period
# 

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal
# and export a text file with the results.