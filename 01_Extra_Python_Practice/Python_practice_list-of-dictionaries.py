voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#another way to iterate through the list of dictionaries.
for county_dict in range(len(voting_data)):
    print(voting_data[county_dict])

#Using range() to iterate over the list of dictionaries and print out key, values.
for i in range(len(voting_data)):
    print(voting_data[i])

#Get/print (only) the values and keys from a list of dictionary - using nested loop.
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#retrieve the number of voters form a list of dictionaries:
for county_dict in voting_data:
    for key, value in county_dict.items():
        print(value)

#to get only registred voters.
for county_dict in voting_data:
	print(county_dict['registered_voters'])

#to get only counties.
for county_dict in voting_data:
	print(county_dict['county'])