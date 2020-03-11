#pypol
#define path to csv file the imports below are module imports but are also called packages
#read file

import os
import csv
dir_path = os.path.dirname(os.path.realpath(__file__))
#if it's in same directory you can just specify the file
csvpath = os.path.join(dir_path,'PyPoll_data.csv')
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    next(csvreader)
    # data = list(csvreader)
    # votecount = len(data)
    # print(votecount)
    #next(csvreader)
    candidate_name = []
    #dictionary with name as key
    candidate_votes = {}
    winner_votes = 0
    winner_candidate = ""
    candidate_pct = {}
    votecount = 0
    winner = 0
    for x in csvreader:
        votecount = votecount +1
        if x[2] not in candidate_name:
            candidate_name.append(x[2])
            candidate_votes[x[2]] = 0
        candidate_votes[x[2]] = candidate_votes[x[2]] + 1
    print("Voting Results")
    print("")    
    #print(votecount)
    print(("Total Votes :  ") + str(votecount))
    print(candidate_name)
    print(candidate_votes)

    for k in candidate_votes:        
        #votes = candidate_votes[k]
        if candidate_votes[k] > winner:
            winner = candidate_votes[k]
            winner_candidate = k
        candidate_pct[k]= (candidate_votes[k]/votecount) * 100
    

    print(candidate_pct)
    print(winner_votes)
    print(winner_candidate)
dir_path = os.path.dirname(os.path.realpath(__file__))
output_file = os.path.join(dir_path, "output.csv")

with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerows(candidate_pct)
    #writer.writerows(winner_votes)
    writer.writerows(winner_candidate)



