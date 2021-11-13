import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n------------------\nArapahoe\nDenver\nJefferson")

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     file_reader = csv.reader(election_data)
     #print the header row
     headers = next(file_reader)
     print(headers)


    
