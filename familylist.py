import json
# dictionaries with family members' info
p1 = { "name":"Rama", "age":49, "city":"Vancouver"}
p2 = { "name":"Vidya", "age":48, "city":"Reykjavik"}
p3 = { "name":"Satvik", "age":13, "city":"Banff"}
p4 = { "name": "Aditi", "age": 16, "city": "Whistler"}
# a list of family members' dictionaries
family_members = [p1, p2, p3, p4]
# prints list of family members and their info
print("Family Members")
print(type(family_members))
print(family_members)
for person in family_members:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()
# turn list to dictionary of family members
Family_dict = {'people': family_members}
print("Dictionary of Family Members")
# Prints Dictionary of Family Members
print(type(Family_dict))
print(Family_dict)
family = Family_dict["people"]
for person in family:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()
# prepare list for JSON, this can be sent via a browser
json_family = json.dumps(Family_dict)
# the result is a JSON file:
print("JSON People")
# Prints Family members from JSon
print(type(json_family))
family = json.dumps(Family_dict["people"])
print(json_family)
x = json.loads(json_family)
family = x["people"]
for person in family:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()
# unwind family members back to JSON
Family_dict = json.loads(json_family)
print("Dictionary of people")
# write some code to Print family members from Dictionary
print(type(Family_dict))
x = json.loads(json_family)
family = x["people"]
for person in family:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])
print()