#data structure
#list is mutable, non-hommogenous, an ordered sequence of items.
#real life example of lists is grocery list.
#dictionary is mutable
student_details = ["abc",12,"123@anywhere", 480, True]
contacts = {
    "name":"Jane Doe",
    "number": 123456789,
    "age":23,
    "city":"New York"
}
print(contacts)
#Accessing the value from the dictionary
print(contacts["name"])

contacts = ["Jane Doe",123456789,23,"New York"]
print(contacts.keys())
#use of for loop
for key in contacts:
    print(key,contacts[key])
#if condition to check whether a key exists or not in a dictionary
if person in contacts:
    print(contacts["country"])
else:
    print("key does not exist")
#as dictionary is mutable we can add key value pairs
ycontacts["country"] = "United states"
print(contacts)