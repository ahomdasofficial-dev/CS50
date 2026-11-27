# Dictionary in Python

# Dictionaries are used to store data values in key:value pairs
# they are unordered, mutable(changeable) and don't allow duplicate keys
# dict={
#     "name":"shradha",
#     "age": 23,
#     "marks":3993
    

# }
# null_dict={}
# null_dict["name"]="apna college"

# dict["name"]="ahom"
# dict["surnama"]="khapra"
# print(dict)

# student={
#     "name ": "ahom Das",
#     "subjects": {
#         "phy":97,
#         "chem": 98,
#         "math": 95
#     }
# }
# print(student["subjects"]["chem"])
# print(type(list(student.keys())))

# Dictionaries are unordered mutable and don't allow duplicate keys



# Dictionary Method

# student={
#     "subjects": {
#         "phy": 97,
#         "chem": 98,
#         "math":95,

#     }
# }



# set in python

# set is the collection of the unordered items/
# each element in the set must be unique and immutable 

# collection={1,3,4,5,"hello","world"}
# print(collection)
# print(
#     type(collection)
# )

# collection=set()#empty set; syntaxx
# print(type(collection))

# set methods
# set.add (el) #adds of elements
# set.remove(el) #removes the element
# set.clear() #
# #set.union (set2)#remobines both set values and returns new 
# set.intersection(set2)#combines common value and returns new


# store following word meaning in a python dictionary:

# dictionary={
#     "table":"a piece of furniture",
#     "cat": "a small animal",

# }

# print(dictionary)


# you are given a list subjects for students. assume one classroom is required for 1 subject. how many classroom are needed by all students.
# subjects={
#     "python", "java", "c++", "python", "javascript", "java",
#     "python", "java", "c++"
# }
# print(len(subjects))


# wap to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary and add one one by one. use subjecct name as key and marks as value
# marks={

# }

# int(input("enter your phy marks:"))
# int(input("enter your chem makrs:"))
# int(input("enter your bio marks:"))

# marks.update({"physic": marks })
# marks.update({"chem:":marks})
# print(marks)