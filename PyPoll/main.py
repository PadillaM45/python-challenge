import os
import csv


csvpath = os.path.join('..','PyPoll','election_data.csv')
total_votes = 0
khancount = 0
correycount = 0
licount=0
otooleycount=0
winner = ""


with open(csvpath, newline='') as nfile:
    csvreader = csv.reader(nfile, delimiter=',')
    csv_header = next(csvreader)


    for rows in csvreader:
        total_votes += 1

        if rows[2] == "Khan":
            khancount += 1
        elif rows[2] == 'Correy':
            correycount +=1
        elif rows[2] == "Li":
            licount += 1
        else:
            otooleycount += 1

        

    khantotal= (khancount/total_votes) * 100
    correytotal= correycount/total_votes* 100
    litotal = licount/total_votes*100
    otooleytotal= otooleycount/total_votes*100
    winner = max(khancount,correycount,licount,otooleycount)

    if winner == khancount:
        winner = "Khan"
    elif winner == correycount:
        winner == "Correy"
    elif winner == licount:
        winner == "Li"
    else:
        winner = "O'Tooley"

print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: %{round(khantotal)}({khancount})")
print(f"Correy: %{round(correytotal)}({correycount})")
print(f"Li: %{round(litotal)}({licount})")
print(f"O'Tooley: %{round(otooleytotal)}({otooleycount})")
print(f"---------------------------")
print(f"Winner: {winner}")
print(f"---------------------------")



output_file = os.path.join('..', 'PyPoll', 'output.text')
with open(output_file, 'w',) as txtfile:


    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: %{round(khantotal)}({khancount})\n")
    txtfile.write(f"Correy: %{round(correytotal)}({correycount})\n")
    txtfile.write(f"Li: %{round(litotal)}({licount})\n")
    txtfile.write(f"O'Tooley: %{round(otooleytotal)}({otooleycount})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"---------------------------\n")