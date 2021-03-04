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
# prints title of list
print("JSON Family Members")
# Prints Family members from JSON
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
# defines an empty list
parents = []
# defines an empty list
children = []
for person in family:
    if "parent" in person:
        # if parent = True, then the person is added to the end of the list called parents
        parents.append(person)
    elif "child" in person:
        # if child = True, then the person is added to the end of the list called children
        children.append(person)
# prints list of family members and their info
for person in family:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()


# prints title
print("Parents")
# prints list called parents
print(parents)
print()
# prints a column of people who are in list called parents
for person in parents:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()
# prints title of list
print("Children")
# prints list called children
print(children)
print()
# prints a column of people who are in list called parents
for person in children:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()


# defines an empty list
employed = []
# defines an empty list
school = []

for person in family:
    # if employed = True, then the person is added to the end of the list called employed
    if "employed" in person:
        employed.append(person)
    # if school = True, then the person is added to the end of the list called school
    elif "school" in person:
        school.append(person)
print()
# prints title of employed table
print("Employed")
# prints list called employed
print(employed)
print()
# prints column of people that are in employed list
for person in employed:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()
# prints title of school table
print("School")
# prints list called school
print(school)
# prints column of people that are in school list
for person in school:
    print(person['name'] + "," + str(person['age']) + "," + person['fav_city'] + "," + person['birthplace'])
print()