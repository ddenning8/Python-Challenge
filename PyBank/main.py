#open csv
import os
import csv

budget_data_csv = os.path.join("../PyBank","budget_data.csv")

print("Financial Analysis")

print("----------------------------------")

with open(budget_data_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    Total_Months = sum(1 for line in csvfile) - 1
    print("Total_Months: " + str(Total_Months))



 