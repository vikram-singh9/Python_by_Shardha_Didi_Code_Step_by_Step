# sets in python
# set is the collection of unordered items.
# each element in the set must be unique and imutable.

nums = {1,2,3,4}
set2  ={1,2,2,2}
# repeated elements stored only once, so it resolved to {1,2}
# duplicate values allow nhn h set k andr
# list and dict accepatble nhn h set ke andar

collection = {1,2,3,4,5,6,7,8,8} # 8 ignore hoga!
print(collection)
print(type(collection))

#empty set

# collection = {} # this is not set this is a dictionary
collection = set() # empty set
# set mutable h pr uske elements immutable hai!

# methods of set

# add method
newEmptySet = set()
print(newEmptySet)
newEmptySet.add(1)
newEmptySet.add(2)
newEmptySet.add("apna college")
newEmptySet.add((1,2)) # tuple

print(len(newEmptySet))
print(newEmptySet)
# remove method
# remove krta hai ek item ko.. 
newEmptySet.remove("apna college")
print(newEmptySet)


# clear method
# poore set ko khali kar deta hai...
newEmptySet.clear()
print(len(newEmptySet))
print(newEmptySet)

# pop method
# random value ko print karwa deta hai
hobbies = {'movies', 'cricket', 'sports'}
print(hobbies.pop())
print(hobbies.pop())

# union method
# combines both set values and return new
set = {1,2,3,4}
set2 = {3,4,5}
print(set.union(set2))
set.remove(4)
print(set)

# intersection method 
# combine common values and return new
print(set.intersection(set2)) # 3 common
