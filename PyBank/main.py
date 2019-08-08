import os
import csv


csvpath = os.path.join('..','PyBank','budget_data.csv')

monthscount = 1
totalchange = 0
totalchangelst = []
xmonth = ''
ymonth = ''

with open(csvpath, newline='') as nfile:
    csvreader = csv.reader(nfile, delimiter=',')
    csv_header = next(csvreader)
    row = next(csvreader)
    lastrow = int(row[1])
    totalnet = int(row[1])
    x= 0
    y= 0


    for row in csvreader:
        monthscount += 1
        totalnet += int(row[1])


     
        totalchange = int(row[1]) - lastrow
        totalchangelst.append(totalchange)
        
        lastrow = int(row[1])   



        if int(row[1]) > x:
            x = int(row[1])
            xmonth = str(row[0])
        
        if int(row[1]) < y:
            y = int(row[1])
            ymonth = str(row[0])

    
    avgchange = sum(totalchangelst)/len(totalchangelst)
    lowest = min(totalchangelst)
    highest = max(totalchangelst)


print(sum(totalchangelst))
print(len(totalchangelst))
print(lowest)

print(totalchangelst)

print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {monthscount}")
print(f"Total: ${totalnet}")
print(f"Average Change: ${avgchange}")
print(f"Greatest Increase in Profits:,{xmonth} (${highest})")
print(f"Greatest Decrease in Profits:,{ymonth} (${lowest})")



output_file = os.path.join('..', 'PyBank', 'outcome.text')


with open(output_file, 'w',) as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {monthscount}\n")
    txtfile.write(f"Total: ${totalnet}\n")
    txtfile.write(f"Average Change: ${avgchange}\n")
    txtfile.write(f"Greatest Increase in Profits:, {xmonth}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:,{ymonth} (${lowest})\n")