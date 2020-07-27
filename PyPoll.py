#election-analysis
#PSEUDOCODE

#Importing/Add dependencies.
import csv
import os 

#Open a .CSV file. Set a variable, direct or indirect path to location, declare a function: ("r = reading", "w" = writting)
#Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt") #-- THIS LINE -- Create a filename variable to a direct or indirect path to the file.
#file_to_load = 'Resources/election_results.csv' #--THIS LINE -- a way to open the file when the path is known
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv") # a way when we do not know the path

#Open the election results and read the file. Using open() function
#open(file_to_save, "w") # THIS LINE -- see function "w" = write to a file.
#election_data = open(file_to_load, 'r') #--THIS LINE-- is another way to open/read the file. "With" method below is another way. 
#opening file with "with open()" method doesn't require close() method.
with open(file_to_load) as election_data:

    #To do: perform analysis.
    #print(election_data)
    #To do: read and analyze the data here.
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)

    #Print the header row.
    headers = next(file_reader)
    print(headers)

#Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file: #REMEMBER - with statement requires indentation!
#outfile = open(file_to_save, "w") # --THIS LINE -- using open()/close() method to open file in write mode. (1)* USED TOGETHER
    #Write some data to the file.
    #txt_file.write("Countites in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson") # one way of writting separate elements in the file - or see above.
#outfile.write("Hello World") # THIS LINE -- -- using open()/close() method to open file in write mode. (1)* USED TOGETHER

#Close the file.
#outfile.close()


#Close the file. Closing the file is important! You can loose some data if not done so.
#election_data.close()


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