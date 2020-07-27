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

#Add the total vote counter = Initialize a total vote counter.
total_votes = 0

#Create an empty list candidate_options to hold candidate_name
candidate_options = []

#Create/declare an empty dictionary to hold candidate name and its votes count.
candidate_votes = {}

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

    #Read the header row.
    headers = next(file_reader)
    #Print the header row.
    #print(headers)

    #Print each row in the CSV file.
    for row in file_reader:
        #print(row) -we don't need to print it.
        #Increment the total_votes by 1 (add the total vote count).
        total_votes += 1

        #Print the candidate name for each row
        candidate_name = row[2]

        #Add the candidate_name to the candidate_options list using append() method. 
        #Selecting only unique names we set condition with "if statements" and membership operators.
        #Reads as: If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Create a key"candidate_name" for candidate_name(=value as in Raymon Anthony Doane) AND...
            #...Begin tracking that candidate's vote count.
            #Initializing each candidate vote to zero.
            candidate_votes[candidate_name] = 0

        #Incrementing candidate votes by 1. INDENTATION = has to be aligned with If statement that for loop apply to this line of code.
        candidate_votes[candidate_name] += 1 
    
#Print the total votes (pay attention to indentation.)
#print(total_votes)
#Print candidate_options.
#print(candidate_options)
#Print candidate votes dictionary.
print(candidate_votes)

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