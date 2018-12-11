
import pandas as pd
import numpy as num
import os


elect_csv_path = os.path.join("Resources", "election_data.csv")
print(elect_csv_path)


elect_df = pd.read_csv(elect_csv_path, encoding="ISO-8859-1")

TotalVoters = len(elect_df["Voter ID"].unique())
TotalCounties = len(elect_df["County"].unique())
TotalCandidate = len(elect_df["Candidate"].unique())

elect_df_gb = elect_df.groupby(['Candidate'])

Cand_Votes_df = elect_df_gb.count()

Cand_Votes_df = Cand_Votes_df.rename(columns={"Candidate": "Candidate",
                                        "Voter ID": "Vote_Percentage",
                                        "County": "Total_Votes"})


#For each row in the Cand Votes df
#Print the Candidate
#Print Total Votes
#Calculate Percentage by Total Votes / Total Voters and format to percentage
#Reindex df so Highlight Votes is not Top 
#Print the row.

print("Election Results")
print("---------------------------")
print(f"Total Votes: {TotalVoters}")
print("---------------------------")
print("---------------------------")
print("Winner:")
print("---------------------------")
 
