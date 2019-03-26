#open csv
import os
import csv

budget_data_csv = os.path.join("../PyBank","budget_data.csv")

with open(budget_data_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        print(row)
        
