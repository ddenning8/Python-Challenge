#import dependencies
import os
import csv

#file location
budget_data_csv = os.path.join("../PyBank", "budget_data.csv")

#what are the things I need?
Total_Months = []
Total = []

#open file to read
with open(budget_data_csv, newline = "") as budget_data:
    csvreader = csv.reader(budget_data, delimiter = ",")

    #skip column names
    header = next(csvreader)

    #get data into correct lists
    for rows in csvreader:
        Total_Months.append(rows[0])
        Total.append(int(rows[1]))

#print what I got so far
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {len(Total_Months)}")
print(f"Total: ${sum(Total)}")

#get change between the two months
Monthly_Change = []

#go through rows and pull difference
for i in range(len(Total) - 1): #-1 b/c last row point can't be subtracted
    Monthly_Change.append(Total[i+1] - Total[i])

print(f"Average Change: ${round(sum(Monthly_Change)/len(Monthly_Change) , 2)}")

#Find max and min totals from the previous list.
Max_Total_Value = max(Monthly_Change)
Min_Total_Value = min(Monthly_Change)

#Reference that max and min number to the beginning month AKA index. need +1 because change associated with next month
Max_Month = Monthly_Change.index(max(Monthly_Change)) + 1
Min_Month = Monthly_Change.index(min(Monthly_Change)) + 1 

print(f"Greatest Increase in Profits: {Total_Months[Max_Month]} (${(str(Max_Total_Value))})")
print(f"Greatest Decrease in Profits: {Total_Months[Min_Month]} (${(str(Min_Total_Value))})")



