#election-analysis
#PSEUDOCODE

#Importing files. csv & os(when path unknown)
import csv
import os

#Open a .CSV file. Set a variable, direct or indirect path to location, declare a function: ("r = reading", "w" = writting)
#Assign a variable for the file to load and the path.
file_to_save = os.path.join("Analysis", "election_analysis.txt") #-- THIS LINE -- to read the file
#file_to_load = 'Resources/election_results.csv' #--THIS LINE -- a way to open the file when path is known
file_to_load = os.path.join("Resources","election_results.csv") # a way when we do not know the path

#Open the election results and read the file. Using open() function
#open(file_to_save, "w") # THIS LINE -- see function "w" = write to a file.
#election_data = open(file_to_load, 'r') #--THIS LINE-- is another way to open/read the file. "With" method below is another way.
with open(file_to_load) as election_data:

    #To do: perform analysis.
    print(election_data)

#Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
#Write some data to the file.
outfile.write("Hello World")
#Close the file.
outfile.close()


#Close the file. Closing the file is important! You can loose some data if not done so.
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