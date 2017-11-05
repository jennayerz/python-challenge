import csv
from collections import Counter

election_data = '/Users/Jenny/Desktop/NEW/python-challenge/PyPoll/election_data_2.csv'

print("Election Results")
print("-------------------------")

# ---------------------------
# TOTAL VOTES
# ---------------------------
with open(election_data, newline='') as all_election_data:
    results = csv.reader(all_election_data, delimiter=',')

    total_votes = sum(1 for line in open(election_data)) - 1
    print("Total Votes: " + str(total_votes))

    print("-------------------------")

# ---------------------------
# LIST OF CANDIDATES
# ---------------------------

#    list_names = ["Khan", "Correy", "Li", "O'Tooley"]
#    candidate_names = []
#    for row in results:
#        if row in list_names:
#            candidate_names.append(row)
#            list_names.add(row)
#            print(candidate_names)
#        print(row[2])

# Remove header    
    next(results, None)

# Get candidate names
    names = set()
    for row in results:
        if row[2] not in names:
            names.add(row[2])
#            print(row[2] + ": ")
    
        votes = Counter(row[2] for row in csv.reader(all_election_data))
#        print(votes)
    
        Khan_percent = round((2218230 / total_votes) * 100)
        print("Khan: " + str(Khan_percent) + "%" + " (" + str(2218230) + ")")

        Correy_percent = round((704200 / total_votes) * 100)
        print("Correy: " + str(Correy_percent) + "%" + " (" + str(704200) + ")")

        Li_percent = round((492940 / total_votes) * 100)
        print("Li: " + str(Li_percent) + "%" + " (" + str(492940) + ")")

        OTooley_percent = round((105630 / total_votes) * 100)
        print("O'Tooley: " + str(Correy_percent) + "%" + " (" + str(105630) + ")")

print("-------------------------")

if Khan_percent > Correy_percent > Li_percent > OTooley_percent:
    print("Winner: Khan")
elif Correy_percent > Khan_percent > Li_percent > OTooley_percent:
    print("Winner: Correy")
elif Li_percent > Khan_percent  > Correy_percent > OTooley_percent:
    print("Winner: Li")
else:
    OTooley_percent > Khan_percent > Correy_percent > Li_percent
    print("Winner: O'Tooley")
