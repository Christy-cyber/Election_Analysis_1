# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path.
file_to_load  = os.path.join("Resources", "election_results.csv")

# Create a filename variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis_1.txt")

# Intitialize total votes to 0
total_votes = 0

# Declare candidate options
candidate_options = []
# Declare the empty dictionary for candidate votes
candidate_votes = {}
# Winning candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Use the with statement to open the file as a text tile
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    # Go back to your notes in 3.4.4 to see what was deleted.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1

        # Harvest the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
                # Add it to the list of candidates.
                candidate_options.append(candidate_name)

                # Begin tracking vote count.
                candidate_votes[candidate_name] = 0

        # Add vote count for each candidate.
        candidate_votes[candidate_name] += 1

        

# Determine the percentage of votes for each candidate.  Loop through counts.
for candidate_name in candidate_votes:
    
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes and convert to decimal.
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage :.1f}% of the vote.")

    # To do: print each candidate's name, vote count, and percentage of votes
    # to the terminal.

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage

        # Set winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# To do: print the winning candidate, vote count, and percentage to the 
# terminal

winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------\n")
print(winning_candidate_summary)





