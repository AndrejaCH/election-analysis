#election-analysis
#PSEUDOCODE

#Importing files. csv & os(when path unknown)
import csv
import os

#Open a .CSV file.
#Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv' #--THIS LINE -- a way to open the file when path is known
file_to_load = os.path.join("Resources","election_results.csv") # a way when we do not know the path

#Open the election results and read the file.
#election_data = open(file_to_load, 'r') --THIS LINE-- is another way to open/read the file. "With" method below is another way.
with open(file_to_load) as election_data:

    #To do: perform analysis.
    print(election_data)

#Close the file.
election_data.close()


#Total number of votes cast
##Count all the votes form entire dataset {total_votes}

#A complete list of candidates who received votes
##Get all candidate names from the dataset + condition who recieved the votes.

#Total number of votes each candidate received
##Set condition for candidate name and count their votes {candidate_name:number_of_votes}

#Percentage of votes each candidate won
## {candidate_name:number_of_votes} / {total_votes} * 100

#The winner of the election based on popular vote
##condition = the most votes: winner = candidate name.