# Import what we need
import os
import csv

# Declare Path
csvpath = os.path.join("/Users/austinolea/Desktop/GIT_REPOS/python_challenge/Resources/election_data.csv")

# Open CSV and Read
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip first line
    next(csvfile)

    # Candidates List Holders
    candidate_duplicate = []
    candidate_list = []

    # For Loop to Fill Lists
    for row in csvreader:
        candidate_duplicate.append(row[2])
    candidate_list = set(candidate_duplicate)  # remove duplicates using set properties
    candidate_list = list(candidate_list)  # convert to list
    number_of_candidates = len(candidate_list)  # number of candidates

    # The Total Number of Votes Cast
    total_votes = len(candidate_duplicate)
    print("Election Results")
    print("-------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------")

    # Store Candidates and Votes to Dictionary
    PyPoll = {}

    # For Loop to go Through Dictionary
    for i in range(number_of_candidates):
        PyPoll[candidate_list[i]] = candidate_duplicate.count(candidate_list[i])

        # Print Vote Count For Each Canadite
        print("")
        print(candidate_list[i])
        print(float(PyPoll[candidate_list[i]]) / total_votes * 100)
        print(PyPoll[candidate_list[i]])
        print("-------------------")

    # Iterate through dictionary
    # Have a placeholder for Max
    winning_vote_share = total_votes * .52
    poll_win = winning_vote_share

    for x, y in PyPoll.items():
        if y > poll_win:
            poll_win_vote_count = y
            poll_win_name = x

print("")
print("-------------------")
print("Winner!:")
print(f"{poll_win_name} - {poll_win_vote_count}")
print("-------------------")
print("")

# Output files
output_file = os.path.join("/Users/austinolea/Desktop/GIT_REPOS/python_challenge/PyPoll/analysis/summary.txt")

summary = (f"Election Results:\n"
           f"\n"
           f"-------------------\n"
           f"Total Votes: {str(total_votes)}\n"
           f"-------------------\n"
           f"\n"
           f"-------------------\n"
           f"{PyPoll}\n"
           f"-------------------\n"
           f"\n"
           f"Winner!:\n"
           f"{poll_win_name} - {poll_win_vote_count}\n"
           f"-------------------\n"
           f"\n"
           )

with open(output_file, "w") as file:
    file.write(summary)
