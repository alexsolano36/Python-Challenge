#import modules
import csv
import os

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

#open csv
with open(PyPollscsv, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)
        
        for row in csvreader:
            #count votes
            count = count +1
            
            #candidate names
            candidatelist.append(row[2])
        
        #set of unique candidate names
        for x in set(candidatelist):
            unique_candidate.append(x)
            
            #total number of votes per candidate
            y = candidatelist.count(x)
            vote_count.append(y)
            
            #percent of total votes per candidate
            z = (y/count)* 100
            vote_percent.append(z)
        
        winning_vote_count = max(vote_count)
        winner = unique_candidate[vote_count.index(winning_vote_count)]
        

print("Election Results")
print("Total Votes: " + str(count))

for i in range(len(unique_candidate)):
    print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")")
print("The winner is: " + winner)

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("Total Vote: " + str(count) + "\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) + "% (" + str(vote_count[i]) + ")\n")
        text.write("The winner is: " + winner + "\n")
