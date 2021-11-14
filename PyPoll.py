import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize the total vote counter.
total_votes = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)
     
     #Read the header row
     headers = next(file_reader)
     
     #print each row int he CSV file.
     for row in file_reader:
         #Add to the total vote count.
         total_votes += 1
print(total_votes)




    
