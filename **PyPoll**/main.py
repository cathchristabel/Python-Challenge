# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join('Resources','election_data.csv')
file_to_output = os.path.join('election_result.txt')

# Track various parameters
total_votes = 0
candidate_list = []
candidate_votes = {}
winner_vote = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header row
    header = next(reader)
    
    for row in reader:
        total_votes = total_votes + 1
        chosen_candidate = row[2]
        
        if chosen_candidate not in candidate_list:
            candidate_list = candidate_list + [chosen_candidate]
            candidate_votes[chosen_candidate] = 0
            
        candidate_votes[chosen_candidate] = candidate_votes[chosen_candidate] + 1

    for candidate in candidate_list:
        if candidate_votes[candidate] > winner_vote:
            winner = candidate
            winner_vote = candidate_votes[candidate]

with open(file_to_output, "w") as txt_file:
    # Print the output to terminal and to txt file
    result_header = (f"\nElection Results\n"
                     f"----------------------------\n"
                     f"Total Votes: {total_votes}\n"
                     f"----------------------------\n")
    print(result_header)
    txt_file.write(result_header)
    
    for entry in candidate_votes:
        result_candidate = f"{entry}: {candidate_votes[entry]/total_votes*100:.3f}% ({candidate_votes[entry]})\n" 
        print(result_candidate)
        txt_file.write(result_candidate)
    
    result_winner = (f"----------------------------\n"
                     f"Winner: {winner}\n"
                     f"----------------------------")
    print(result_winner)
    txt_file.write(result_winner)