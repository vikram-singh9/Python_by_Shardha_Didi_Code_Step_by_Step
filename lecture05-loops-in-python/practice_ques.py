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