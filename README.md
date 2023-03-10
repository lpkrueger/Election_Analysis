# Election Analysis
Module 3, Python - UNCCH Data Analytics Bootcamp, Spring 2023

## Project Overview
Colorado board of elections employees have requested assistance with an election audit of the tabulated results for a U.S. congressional precinct in Colorado. The objective is to generate a vote count report to certify this U.S. congressional race, including: 

1. The total number of votes cast
2. The number and percentage of votes cast by each participating county
3. A list of candidates who received votes
4. The total number and percentage of votes received by each candidate in the race
5. The winner of the election based on the popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.10.5
- IDE: Visual Studio Code 1.74.3

## Election Audit Results
The analysis of the election results, including county data, are as follows (Python terminal output):

    Election Results
    -------------------------
    Total Votes: 369,711
    -------------------------

    County Votes:
    Jefferson: 10.5% (38,855)

    Denver: 82.8% (306,055)

    Arapahoe: 6.7% (24,801)

    -------------------------
    Largest County Turnout: Denver
    -------------------------

    Charles Casper Stockham: 23.0% (85,213)

    Diana DeGette: 73.8% (272,892)

    Raymon Anthony Doane: 3.1% (11,606)

    -------------------------
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%
    -------------------------


The text file output of the election results can be found at this link (.txt file output):
[election_analysis](https://github.com/lpkrueger/Election_Analysis/blob/main/analysis/election_analysis.txt)

## Election Audit Summary
This script employs "for" loops to step through each row of the data file and count votes by both county and candidate.
This script can be used for any election, provided the data are supplied in a .csv file containing 3 columns columns for ballot ID, county, and candidate. If alternate election data contains a different column order or format, this script can be modified accordingly to suit the available data by changing the column indexes. If a different election were to be audited that contained additional candidates or attributes (e.g. specific precinct data), this script can also be modified to parse and display those data using similar techniques to the way that candidate and county statistics were presented here. 


## Method
The Python script used to perform this analysis is as follows: 

 ```
# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
winning_county_count = 0
winning_county_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_list:

        # 6b: Retrieve the county vote count. 
        Cvotes = county_votes.get(county_name)
        
        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(Cvotes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {county_vote_percentage:.1f}% ({Cvotes:,})\n")
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (Cvotes > winning_county_count) and (county_vote_percentage > winning_county_percentage):
            winning_county_count = Cvotes
            winning_county = county_name
            winning_county_percentage = county_vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        #f"Winning Vote Count: {winning_county_count:,}\n"
        #f"Winning Percentage: {winning_county_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
