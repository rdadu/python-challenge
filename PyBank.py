
import pandas as pd
import numpy as num
import os


budget_csv_path = os.path.join("Resources", "budget_data.csv")

budget_df = pd.read_csv(budget_csv_path, encoding="ISO-8859-1")

TotalPFDates = len(budget_df["Date"].unique())

TotalPL = budget_df["Profit/Losses"].sum()

budget_df["priorPF"] = budget_df["Profit/Losses"].shift(1)

budget_df["PF_Change"] = budget_df["Profit/Losses"] - budget_df["priorPF"]

average = round(budget_df['PF_Change'].mean(),2)
maximum = budget_df['PF_Change'].max()
minimum = budget_df['PF_Change'].min()

print("Financial Analysis")
print("------------------")
print(f"Total Profit/Loss: {TotalPL}")
print(f"Total Months: {TotalPFDates}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profits: {maximum}")
print(f"Greatest Decrease in Profits: {minimum}")

import sys
budget_out_csv_path = os.path.join("Resources","budget_out.csv")
sys.stdout = open(budget_out_csv_path, 'w')
print("Financial Analysis")
print("------------------")
print(f"Total Profit/Loss: {TotalPL}")
print(f"Total Months: {TotalPFDates}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profits: {maximum}")
print(f"Greatest Decrease in Profits: {minimum}")

