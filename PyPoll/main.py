#import dependencies
import os
import csv

#file location
election_data_csv = os.path.join("../PyPoll", "election_data.csv")

#Need total voteds
Total_Votes = []

print("Election Results")
print("-----------------------")

#Open the file to read it
with open(election_data_csv, newline = "") as election_data:
    csvreader = csv.reader(election_data, delimiter = ",")

    #Skip Header names
    header = next(csvreader)

    #pull out total votes
    for row in csvreader:
        Total_Votes.append(row[0])
    print(f"Total Votes: {str(len(Total_Votes))}")

