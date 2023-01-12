
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

################on module 3.4.4 as of 5pm 1/11/23##############

#election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
#election_data.close()



# The data we want to retrieve




# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")




## 1. Total number of votes cast

## 2. Complete list of candidates who received votes

## 3. Percentage of votes each candidate won

## 4. Total number of votes each candidate won

## 5. Winner of electrion based on popular vote
