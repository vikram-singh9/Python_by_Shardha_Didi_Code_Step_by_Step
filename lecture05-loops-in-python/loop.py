# two types of loops 1 for loop and 2 while loop

# while loop
count = 1
while count <= 10:
    print("vikram")
    count += 1

# iteration loop ka chakar lagana (1 iteration means ek baar loop ka chakar lagaya!) 
# iterator means jis variable ka use use kya chakr lagane k lye!

i = 5 # i is iterator here
while i <= 50:
    print("vikram singh")
    i += 1

# n  =0 
# while n >= 0:  infinte loop 
#     n += 1
#     print(n)




# break and continue in while loop!

# BREAK used to terminate the loop when encountered.

m = 1
while m <= 5:
    print(m)
    if(m==3): # 3 pe break karega aage nhn chlega 
        break
    m += 1

# CONTINUE
# terminates execution in the current iteration and continues excution of the loop with the next iteration.

o = 0
while o <= 10:
    if(o==6): # 6 print nhn hoga!
        o+=1
        continue # skip in the current iteration (skip karo uske bad aage chalao simple)
    print(o)
    o += 1


    # FOR LOOP

# for loop is used for sequencial travesal. For travesring list, string,tuples etc.

# lets create a list!
actors = ["Tony Stark", "Chris Evans", "Ryan Rynolds","ajay"]

for name in actors: # list mn jo values h wo print hokr aa jayenge
    print(name)

name = "shardha didi"

for char in name:
    print(char)

# for loop in tuple

tup = (1,2,3,4) 

for num in tup:
    print(num)

# KONSA LOOP KAB USE KARNA HAI
# while loop
# jb kisi iterator pe hamen kam karna hai uski value ko update krna hai ya koi stopping condition hai..

# for loop
# jab bhi kisi data type pe traverse karna hai jese list tuple sequence tw ham for loop use kr rhe honge..





# FOR LOOP WITH ELSE optional
# simply ham chahte h jab loop mn kaam khtam ho jaye tow uske baad kuch print karana chaye! that's it


str = "VIKRAM"
for char in str:
    print(str)
else:
    print("end")


# Range()

# range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default) , and stops before a specified number!

# range(start?, stop, step?) # ? is optional

for el in range(5): # range (stop)
    print(el)

seq = range(5)
print(seq)

for i in seq:
    print(i)

for l in range(2,20): # range(start, stop)
    print(l)

for p in range(2,20,3): # range(start, stop, step) step means kitne se badana hai.. 2 5 8 so on
    print(p)

