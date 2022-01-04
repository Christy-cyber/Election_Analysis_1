
import csv
import os

# Assign a variable to load a file from a path.
file_to_load  = os.path.join("Resources", "election_results.csv")

# Create a filename variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis_1.txt")

# Use the with statement to open the file as a text tile
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    # Go back to your notes in 3.4.4 to see what was deleted.
    headers = next(file_reader)
    print(headers)

 
 



