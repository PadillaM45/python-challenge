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
x= 0
y = 0

with open(csvpath, newline='') as nfile:
    csvreader = csv.reader(nfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        monthscount += 1
        totalnet += int(row[1])


     
        totalchange = int(row[1]) - lastrow
        totalchangelst.append(totalchange)
        
        lastrow = int(row[1])   



        if totalchange > x:
            x = int(row[1])
            xmonth = str(row[0])
            xy = totalchange
        if totalchange < y:
            y = int(row[1])
            ymonth = str(row[0])
            yx = totalchange
    
    
    avgchange = sum(totalchangelst)/len(totalchangelst)
    lowest = min(totalchangelst)
    highest = max(totalchangelst)




print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {monthscount}")
print(f"Total: ${totalnet}")
print(f"Average Change: ${avgchange}")
print(f"Greatest Increase in Profits:,{xmonth} (${xy})")
print(f"Greatest Decrease in Profits:,{ymonth} (${yx})")



output_file = os.path.join('..', 'PyBank', 'outcome.text')


# with open(output_file, 'w',) as txtfile:
#     txtfile.write(f"Financial Analysis\n")
#     txtfile.write(f"---------------------------\n")
#     txtfile.write(f"Total Months: {monthscount}\n")
#     txtfile.write(f"Total: ${totalnet}\n")
#     txtfile.write(f"Average Change: ${avgchange}\n")
#     txtfile.write(f"Greatest Increase in Profits:, {xmonth}, (${x})\n")
#     txtfile.write(f"Greatest Decrease in Profits:,{ymonth} (${y})\n")