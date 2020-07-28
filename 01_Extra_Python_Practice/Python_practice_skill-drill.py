counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#get key, values form a dictonary and print them in a full sentence - using f-strings. 
for county, voters in counties_dict.items():
    print(f'{county} county has {voters} register voters.')

#get key, values form a dictonary and print them in a full sentence - using coversion.
for county, voters in counties_dict.items():
    print(county + "county has " + str(voters) + " register voters.")

#print key, values using f-string and number formatting.
for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} register voters.')


#skill-drill: list of dictionaries: print
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#prints from list of dictionaries and reurns KEY and VALUES seperately with number formatting.
for county_dict in voting_data:
	print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} voters")