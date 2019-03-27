#import dependencies
import os
import csv

#file location
election_data_csv = os.path.join("../PyPoll", "election_data.csv")

#Need total votes and candidates
Total_Votes = 0
Candidates = []
Candidate_Votes = []
Percent_Votes = []

print("Election Results")
print("-----------------------")

#Open the file to read it
with open(election_data_csv, newline = "") as election_data:
    csvreader = csv.reader(election_data, delimiter = ",")

    #Skip Header names
    header = next(csvreader)

    #pull out total votes
    for row in csvreader:
        Total_Votes += 1 #summing rows as total votes
        if row[2] not in Candidates: #If not in empty list add cand and count a 1 for vote
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            Candidate_Votes.append(1)
        else:
            index = Candidates.index(row[2]) #if already in list count as a vote
            Candidate_Votes[index] += 1
    print(f"Total Votes: {str(Total_Votes)}")

    for Votes in Candidate_Votes:
        Percent = (Votes/Total_Votes)*100
        Percent_New = "%.3f%%" % Percent #convert percent to 3 decimal places... found that on the interwebs
        Percent_Votes.append(Percent_New)

for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(Percent_Votes[i])}% ({str(Candidate_Votes[i])})")
print("-----------------------")
    




