# dictionary are used to store data values in key:value pairs
# they are unordered,mutable(changeable) & don't allow duplicate keys

# example
dict = {
    "name" : "vikram",
    "cgpa" : 9.4,
    "marks" : [98, 97, 95]
}

print(dict)


info = {
    #you can write anything in dic its mutable like list
    "name" : "vikram singh",
    "subjects" : ['python', 'javascript', 'java', 'c++'],
    22: 23,
    "topics": ('dic', 'set'),
    "is_adult" : True,
    "marks":94.4
}
print(type(info))
print(info["is_adult"])
print(info)

# change keys values
info["name"] = "shardha didi"
info["marks"] = 98.00
# add key values
info["surname"] = "khapra"
info["age"] = 23
print(info)


null_dict = {}
null_dict ["name"] = "vikram"
print(null_dict)

# nested dictionary

student = {
    "name" :"asad",
    "score":{
        "chem":23,
        "bio":23.4
    }
}

print(student["score"]["bio"])


# methods of dictionary

# keys()

print(student.keys())
# keys nikal ke de dega

# values()
print(student.values())
# values nikal ke de dega

# items()
# returns all (key val) pairs as tuple
print(student.items())

# get(key)
# kisi bhi key ki value laake deta hai! 
print(student.get("name"))
print(student["name"]) # => ye galat tarika h error dega lekin small code mn same result dega!

# upadate method
# inserts the speciefied items to the dictionary!
student.update({"city" : "umerkot"})
print(student)







