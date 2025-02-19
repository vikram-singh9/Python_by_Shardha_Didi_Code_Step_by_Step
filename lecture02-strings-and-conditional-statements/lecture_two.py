#  strings

str1 = 'this\n is a string. hello iam string'
print(str1)


# operation in strings
# concatination str  + str2
str2 = 'hello' + 'world'
print(str2)

# length of str

len1 =len(str1)
print(len(str1))
# space bhi count horhi hai

name = 'vikram'
print(len(name))


# indexing

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# slicing

teacher = 'shardha didi'
college = 'apna college'
print(teacher[0:5])
print(teacher[0:7])
print(teacher[0:len(teacher)])
print(college[5:len(college)])


# strings functions

sentenece = 'i am a coder'

print(sentenece.endswith('er'))

print(sentenece.startswith('i'))

print(sentenece.capitalize())

print(sentenece.replace('coder','developer'))

print(sentenece.find('am'))

print(sentenece.count('i'))


# practice questions
# name = input('enter your name')
# print(name)

# print(len(name))

jumla = 'hi iam a $ symabal $ my symble hai'
print(jumla.count('$'))



# conditional statements

age = 23 
if(age):
    print('you are 23 years old')
else:
    print('you are younger than 23 or older ')


a = 20
b = 20
c = 30

if(b> a) : 
    print('b is greater than a ')
elif(c<b):
    print('c is greater than b')
else :
    print('a is greater than b and c')


# practice questions

marks = int(input('enter your marks'))

if(marks >= 90):
    print('grade A')
elif(marks <= 90 and marks >= 80):
    print('grade B')
elif(marks <= 80 and marks >= 70):
    print('grade C')
else:
    print('grade D')

userInput = int(input('enter any number to check even and odd'))

if(userInput % 2 == 0):
    print('even')
else:
    print('odd')


a = int(input('enter any number'))
b = int(input('enter any number'))
c = int(input('enter any number'))

if(a >= b and a >= c):
    print('a is the greatest number',a)
elif(b>=c):
    print('b is the greatest number',b)
else:
    print('c is the greatest number',c)

numberByUser = int(input('enter number to find out mutliple of 7 => '))
if(numberByUser % 7 == 0) :
    print(numberByUser, 'multiple of 7')
else:
    print(numberByUser,'is not a multiple of 7')







