# print numbers from 1 to 100 using while loop
# very easy let's start coding!
number = 1
while number <= 99:
    number += 1
    print(number)

# reverse order 

n = 100
while n >= 1: # this is the stopping condition
    n -= 1
    print(n)


# print the multiplication table of number n?

n = 1 
while n <= 9:
    n += 1
    print(n*3)



# for loop
# Q1 = print the elements of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]

numbers = [1,4,9,16,25,36,49,64,81,100]

for el in numbers:
    print(el)


# filtering numbers
filter = [1,4,9,16,25,36,49,64,81,100]
# 25 ko filter krenge 
x = 25
for k in filter:
    if k == x:
        print("founded",k)
        k +1 



# RANGE
# print 1, 100
for p in range(101):
    print(p)

# print 100, 1
for h in range(100,0, -1):
    print(h)

# print the multiplication table of a number n!

n = int(input("enter number: "))
for t in range(1,11): # 1 se 10
    print(n * t)


# PASS statement!



