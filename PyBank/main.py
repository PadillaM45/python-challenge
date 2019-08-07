import os
import csv


csvpath = os.path.join('..','PyBank','budget_data.csv')

monthscount = 0
totalnet = 0
lastrow = 0
totalchange = 0
totalchangelst = []
xmonth = ''
ymonth = ''


with open(csvpath, newline='') as nfile:
    csvreader = csv.reader(nfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        monthscount += 1
        totalnet += int(row[1])
        x = int(row[1])
        y = int(row[1])

     
        totalchange = int(row[1]) - lastrow
        lastrow = int(row[1])   
        totalchangelst.append(totalchange)


        if int(row[1]) > x:
            x = int(row[1])
            xmonth = str(row[0])

        if int(row[1]) < y:
            y = int(row[1])
            ymonth = str(row[0])
    
    
    avgchange = sum(totalchangelst)/len(totalchangelst)
    lowest = min(totalchangelst)
    highest = max(totalchangelst)




print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {monthscount}")
print(f"Total: ${totalnet}")
print(f"Average Change: ${avgchange}")
print(f"Greatest Increase in Profits:,{xmonth} (${highest})")
print(f"Greatest Decrease in Profits:,{ymonth} (${lowest})")




