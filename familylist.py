import json
# dictionaries with family members' info and attributes for each person
p1 = { "name":"Rama", "age":49, "fav_city":"Vancouver", "birthplace":"Vizag", "parent":True, "employed":True}
p2 = { "name":"Vidya", "age":48, "fav_city":"Reykjavik", "birthplace":"Bangalore", "parent":True}
p3 = { "name":"Satvik", "age":13, "fav_city":"Banff", "birthplace":"San Diego", "child":True, "school":True}
p4 = { "name":"Aditi", "age": 16, "fav_city": "Whistler", "birthplace":"San Diego", "child":True, "school":True}
p5 = { "name":"Lalita", "age":70, "fav_city":"Bangalore", "birthplace":"Tamilnadu", "parent":True}

# a list of family members' dictionaries
family_members = [p1, p2, p3, p4, p5]

# Prints title of list
print("List of Family Members")
# prints data type of family members list
print(type(family_members))
# prints list of family members and their info
print(family_members)
for person in family_members:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()


# turn list to dictionary of family members
Family_dict = {'people': family_members}
# Prints title of Dictionary of Family Members
print("Dictionary of Family Members")
# Prints data type of Dictionary of Family Members
print(type(Family_dict))
# Prints Dictionary of Family Members
print(Family_dict)
family = Family_dict["people"]
for person in family:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()
# prepare list for JSON, this can be sent via a browser
json_family = json.dumps(Family_dict)
# the result is a JSON file:
print("JSON Family Members")
# Prints Family members from JSon
print(type(json_family))
family = json.dumps(Family_dict["people"])
print(json_family)
x = json.loads(json_family)
family = x["people"]
for person in family:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()
# unwind family members back to JSON
Family_dict = json.loads(json_family)
print("JSON Dictionary of Family Members")
# write some code to Print family members from Dictionary
print(type(Family_dict))
x = json.loads(json_family)
family = x["people"]
parents = []
children = []
for person in family:
    if "parent" in person:
        parents.append(person)
    else:
        children.append(person)
for person in family:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()

print("Parents")
print(parents)
print()
for person in parents:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()



print("Children")
print(children)
print()
for person in children:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()

employed = []
school = []

print("Education or Work")

for person in family:
    if "employed" in person:
        employed.append(person)
    elif "school" in person:
        school.append(person)
print()
print("Employed")
print(employed)
print()
for person in employed:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()
print("School")
print(school)
for person in school:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()