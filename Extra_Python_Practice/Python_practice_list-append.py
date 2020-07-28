#Appending elements to a list
counties = ["Arapahoe","Denver","Jefferson"]

#Append method:
counties.append("El Passo")
print(counties)

#Insert method:
counties.insert(2, "El Passo")
print(counties)

#Remove method:
counties.remove("El Passo")
print(counties)

#Pop method:
counties.pop(3)
print(counties)

counties.pop(1)
print(counties)

#Change the name in the list:
counties[0] = "El Paso"
print(counties)