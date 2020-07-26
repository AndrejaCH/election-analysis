#takes user input
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100

#print statement with string option
print("I recieved " + str(percentage_votes)+ "% of the total votes.")

#print statement with f-string
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I recieved {my_votes / total_votes * 100}% of the total votes.")

#multiline f-strings. \n = new line \t = indented line.
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What was the total number of votes in the election? "))
message_to_candidate = (
            f"You recieved {candidate_votes:,} number of votes. " #see {value}:, = add a thousands separator
            f"\nThe total number of votes in the election was {total_votes:,}. "
            f"\nYou recieved {candidate_votes / total_votes * 100:,.5f}% of the total votes.") #see the precison in numbers!

print(message_to_candidate)


