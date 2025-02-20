# list in python
# mutable data type in python 
marks = [23.9,34.3,434,2343,4,3,231,32,343.34,23.43]
print(marks[2])
print(type(marks))

list = [12,'hello',False,12.4]
print(list)
print(list[2])

# list methods

# append
# add something to the end of the list
number = [1,2,3]
number.append(4)
print(number)



# sort 
# sort the list in ascending order
ascending = [1,5,8,3,5]
print(ascending.sort()) #none
print(ascending) #actual result

# for descending order = sort.(reverse= True)
ascending.sort(reverse=True)
print(ascending)


# also works with strings
veg = ['potato', 'cauliflower', 'cabbage', 'spinach']
veg.sort()
print(veg)


# reverse
# reverse the list
veg.reverse()
print(veg)


listing = [1,2,3,4,5,6,7,8,9]
# listing.reverse()
# print(listing)

# insert
# jahan marzi h wahan ham put kr sakte hn koi bhi chiz ek list mn..
# pehle index uske baad koi bhi chiz jo add karna hai wo likhte hn...
listing.insert(4,10)
listing.insert(0,90)
print(listing)


stringList = ['a','g','t','q','b','d','c','f','e']
stringList.insert(1,90)
print(stringList)

# pop and remove 
# pop removes the last element from the list
stringList.pop(8)
print(stringList)

# remove removes the element from the list
stringList.remove(1)
print(stringList)
