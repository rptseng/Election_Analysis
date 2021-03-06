# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election

1. Calculate the toal number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes of each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.0, Visual Studio  Code

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The number of votes cast by county were:
  - Jefferson with 10.5% of votes and 38,855 votes.
  - Denver with 82.8% of votes and 306,055 votes.
  - Arapahoe with 6.7% of votes and 24,801 votes.
- Denver was the county with the largest voter turnout at 306,055 votes.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.

## Challenge Overview
In order to use this code to process data from other elections, we could modify by creating a list of dictionaries rather than keep two separate dictionaries ("candidate_votes" and county_votes"). We would also be able to modify the f-string printouts written to the .txt file so that f"County Votes" and f"Largest County Turnout" are not hard-coded with the word "County" and instead substituted with a variable from the list of dictionaries. This would allow you to apply the code to express results for elections in other denominations than County, like a city, province, state, region etc.

## Challenge Summary
![Results_Summary](https://github.com/rptseng/Election_Analysis/blob/main/Resources/Results_Summary.PNG)
