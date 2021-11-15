import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize the total vote counter.
total_votes = 0

#Declare a new list for candidate name
candidate_options = []

#Create votes dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
     file_reader = csv.reader(election_data)
     
     #Read the header row
     headers = next(file_reader)
     
     #print each row int he CSV file.
     for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
        #Print candidate name from each row
        candidate_name = row[2]
        #Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #Begin tracking candidate's vote count.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
#Print the candidate vote dictionary
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) *100
        # 4. Print the candidate name and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #Determine winning vote count and candidate
        #Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                #if true then set winning_count = votes and winning_percent = vote percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name

#  To do: print out the winning candidate, vote count and percentage to terminal
winning_candidate_summary = (
       f"-------------------------\n"
       f"Winner: {winning_candidate}\n"
       f"Winning Vote count: {winning_count:,}\n"
       f"Winning Percentage: {winning_percentage:.1f}%\n"
       f"-------------------------\n")
print(winning_candidate_summary)                
# print(f"{winning_candidate} won the election with a total of {winning_count:,} votes and {winning_percentage:.2f}% of the total vote")








    
