#if-else statement and memvership operators
counties = ["Arapahoe", "Denver", "Jefferson"]

#print individual element.
if counties[1] == "Denver":
    print(counties[1])

#membership operators IN
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

#membership operator IN and OR condition.
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties")

#for loop practice.
for county in counties:
    print(county)

#for loop with range() method.
for i in range(len(counties)):
    print(counties[i])