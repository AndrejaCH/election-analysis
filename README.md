# Election Analysis for U.S. Congressional Precinct in Colorado

*Python election analysis*

## Project Overview
### Purpose
The purpose of this analysis is to generate a vote count report to certify U.S. congressional race in Colorado precinct and represent:

   1. The total number of votes cast.
   2. The complete list of counties in the congressional precinct, including 
   the percentage of votes from each county out of the total count and the voter turnout for each county. 
   3. The county with the highest turnout.
   4. The complete list of candidates who received votes, including 
   the percentage of votes each candidate won and the total number of votes each candidate received.
   5. The winner of the election based on popular vote.


### Background
The results are gathered with three primary voting methods:
  - Mail-in ballots, that are hand-counted at the central office.
  - Punch cards, that are collected and fed into a machine that tabulates votes and then sends the results to the central office.
  - DRE (direct-recording electronic counting) memory cards are read by a computer, and sent to the central office.

Altogether the votes cast by these three methods will determine the final election results.  After the votes are counted, all results are gathered in a .csv file. The file contains three columns with the following headers: 
  - Ballot ID (Column A). 
  - County (Column B).
  - Candidate Name (Column C).

## Resources
- Data Source: [election_results.csv](Resources/election_results.csv)
- Software: Python 3.7.7, Visual Studio Code 1.47.3 
- Report: [election_results.txt](Analysis/election_results.txt)

## Results
### Per Candidate
- The analysis of the election shows that:
  - There were **369,711** votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received **23.0%** of the vote and **85,213** of votes.
    - Diana DeGette received **73.8%** of the vote and **272,892** of votes.
    - Raymon Anthony Doane received **3.1%** of the vote and **11,606** of votes.
- The winner of the election was:
    - **Diana DeGette**, who received **73.8%** of the vote and **272,892** of votes.

### Per County
- The analysis of the election shows that:
- The counties results were:
    - Jefferson with a **10.5%** vote of the total count and **38,855** voter turnout.
    - Denver with an **82.8%** vote of the total count and **306,055** voter turnout.
    - Arapahoe with a **6.7%** vote of the total count and **24,801** voter turnout.
- The county with the largest voter turnout was:
    - **Denver** with an **82.8%** vote of the total count and **306,055** voter turnout.


<p align="center">
<img src="Graphics/TerminalResults.PNG" width="30%" height="30%"> <img src="Graphics/TxtFileResults.PNG" width="30%" height="30%">
</p>

<p align="center">
An example of output from a command line in VS Code and in txt file.
</p>

### Overview of the methods and code
#### Open, read & write the file
One of the most important things in data analytics is opening, reading, and writing a file. Opening and reading a file is the first step that needs to be done in order to start data analysis. Writing a report is as important and since writing a file has a similar syntax it is included in this chapter.

***1. Import dependencies:***

```python s=
import csv
import os
```

- `import csv` - allows to easily pull in data from external CSV files and perform operations on them (and also comes with the following functions):
   - `reader()` - reads each roe from the csv file and return data as a lists of strings (each row is a new list).
      
It is important to know how the data are returned after reading, and knowing the properties of a dataset! `reader()`, will return data as a list (each row is a new list). Lists are mutable and ordered (indexed), so we can access (loop through) the elements via indexes.
   - `next()` - skips the first row (most commonly used to skip a header row).

- `import os` - allows to interact with the operating system, and comes also with the following 2 submodules (this module is used when we do not now direct `path` to a file, but we know the name of directory):
   - `path()` - allows us to access files on different operating systems.
   - `join()` - joins file path components together when they are provided as separate strings; then, it returns a direct path with the appropriate operating system                              separator, forward slash for macOS or backward slash for Windows.

*note: there is also a way to open a file with a direct path.  `file_to_load = 'Resources/election_results.csv'` In this case, we don’t need to `import dependency `import os`.*

***2. Declare a variable, and load a file from the path.***

```python s=
file_to_load = os.path.join("Resources", "election_results.csv")
```
file_to_load - declaring a variable for the file
Resources - directory of the file
election_results.csv - name of the file

*Important directory has to be provided exactly, letter case matters!*

***3. Open and read the file:***

```python s=
with open(file_to_load) as election_data:
   file_to_read = csv.reader(election_data)
```

- `with open()` - statement opens the file and ensures the proper acquisition of data without having to close the file, to ensure that the data isn’t lost or corrupted.
- `as <new_variable_name>` - passing a variable to a new name.
- `file_to_read` - new variable 
- `csv.reader()` - please see the explanation in the pharagraph above. 
- `file_to_read` - a new variable that we will use in the for loop to access the elements via indexes.
- `election_data` - passing an argument to a function, a file that we want to function to read.

*Note: function `with open(file_to_load, “r”)` doesn’t have declared method “r” as in “read mode”, because skipping it, set default settings, that is read or “r” mode.

***4. Declare a header row and skip the first row:***

```python s=
header = next(file_to_read)
```
- `next()` - function will skip first row in file_to_read

<p align="center">
<img src="Graphics/OpenAndReadFullCode.PNG" width="60%" height="60%"> 
</p>

***5. Additional code for writing a file:***

```python s=
file_to_save = os.path.join("Analysis", "election_results.txt")
```
This line of code will create a file in the “Analysis folder” if one doesn’t exist yet. The folder must already exist.

```python s=
with open(file_to_save, "w") as txt_file:
```
In this function, we must specify the method `“w”` as in `write mode` in order to be able to write in a file.

```python s=
txt_file.write(election_results)
```
With the function `.write()` we declare that we want to write in txt_file (this is a new variable that was passed on from “original variable file_to_save”). In parentheses, we declare what we want to be written (refers to a variable election_results).

<p align="center">
<img src="Graphics/OpenAndWriteFullCode.PNG" width="60%" height="60%"> 
</p>

#### Looping through dictionaries and the lists
In order to correctly retrieve elements or loop through specific data sets, it is essential to know their properties. Lists are mutable and ordered (indexing is possible), dictionaries are mutable and unordered (indexing is not possible), dictionary keys are immutable and unique, while values are more flexible and can be mutable.

```python s=
   #retrieving unique values with a conditional statement and membership operator.
   if candidate_name not in candidate_options:

          # Add the candidate name to the candidate list with the append() method.
          candidate_options.append(candidate_name)
            
          # And begin tracking that candidate's voter count. 
          #Assign and store new value with `= 0` to the key (candidate_name) in the dictionary candidate_votes.
          candidate_votes[candidate_name] = 0

   # Add a vote to that candidate's count. Indentation is important 
   #(it has to be aligned with if statement, otherwise values wouldn’t be stored properly)
   candidate_votes[candidate_name] += 1
```

*Note this line of code is inside the `for loop`.*

#### get() method 

With get() method we can retrieves values from a dictionary based on their keys:
votes - accessing values with a variable
candidate name - key
candidate_votes - dictionary

```python s=
For candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
```

#### Finding a winner
The following code determines a winner based on the highest vote count. 

Declaring and initializing variables

```python s=
winning_candidate = ""
winning_count = 0
winning_percentage = 0
```
Determine winning vote count, winning percentage, and candidate.
```python s=
if (votes > winning_count) and (vote_percentage > winning_percentage):
    winning_count = votes
    winning_candidate = candidate_name
    winning_percentage = vote_percentage
```           

All values *votes* are compared against each other by declaring a new variable `wining_count`. When the condition is `True`, meaning the highest value is found, the value is passed to new variables `winning_count` `winning_candidate` ` winning_percentage`.

## Summary 
Writing scripts in Python has many advantages, automating processes, fast execution of the code fast, and reusing the code for similar projects. This code quickly returns numerous data for U.S. Congressional Precinct in Colorado and can be easily used but for other elections as well.
This code will automatically:
- find candidates names,
- find counties,  
- count votes for each candidate and calculate vote %
- count turnout per county and calculate their %
- declare a candidate winner base on the highest vote count and % 
- declare a county with the highest turnout.

Using this code can be used on similar projects such as other congressional districts election, senatorial districts, local election, and more.

- This code reads csv files but can be easily converted to read other files such as *json*, by importing other dependencies for example `import json`.
- This code reads candidate name on 2nd index and county on 1st index, but in case of a different structure of the data set this can be easily converted.
- By importing dependency `datetime` we could perform real-time results for election in progress. `datetime` dependency will capture exact time when the analysis is executed.
- Since Python script finds unique names of candidates and counties we cab reuse this code on a much larger dataset with more candidates and counties or other areas.
- This code accesses the dataset in a specific directory and writes a report to a specific file, but this can be easily fixed by renaming a directory and file in the code itself.




