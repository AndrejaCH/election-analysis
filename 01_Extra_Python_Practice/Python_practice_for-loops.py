#a simple for loop example, print all elements from the list.
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

#range() sample. print all elements within a range.
for num in range(5):
    print(num)

#A LIST:
counties = ["Arapahoe", "Denver", "Jefferson"]       

#get the elements form a list in a range of a lenght of a list.
for i in range(len(counties)):
    print(counties[i])

#get the elements form a list.
for county in counties:
    print(county)

#A DICTIONARY
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#get THE KEYS from a dictionary.
for county in counties_dict:
    print(county)

#get THE KEYS from a dictionary.
for county in counties_dict.keys():
    print(county)

#get THE VALUES from a dictionary.
for voters in counties_dict.values():
    print(voters)

#get THE SPECIFIC VALUE from a dictionary, specifying a KEY.
print(counties_dict["Denver"])

#get ALL THE VALUES from a dictionary, referring to KEYS.
for county in counties_dict:
    print(counties_dict[county])

#get ALL THE VALUES from a dictionary, referring to KEYS, using GET() method.
for county in counties_dict:
    print(counties_dict.get(county))

#get the KEY-VALUE PAIRS of a dictionary
for county, voters in counties_dict.items():
    print(county, voters)



