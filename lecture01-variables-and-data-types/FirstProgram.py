print('Hello World')

# variables

name = 'vikram'
age = 12
lastName = 'singh'

print('my name is ',name ,'and my age is ',age)

male = True
print(male)


numbers = [1,2,3,4,4,5,55]
print(numbers[6])


# data types

name = 'vikram'
age = 12
lastName = False
dec = 12.3
listigs = [1,2,3,4,5,6,7,8,9,10]

print(type(name))
print(type(age))
print(type(lastName))
print(type(dec))
print(type(listigs))


c = 2 + 3j
d = complex(5, -4)
print(type(c))  # <class 'complex'>

# ✅ Tuple (tuple)
# Tuple bhi ordered hoti hai, lekin immutable hoti hai (iska data change nahi hota).

colors = ("red", "green", "blue")
print(type(colors))  # <class 'tuple'>


# range

r = range(5)  # 0,1,2,3,4
v = range(11)
print(list(r))  # [0, 1, 2, 3, 4]
print(list(v))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Set Types
# Sets unordered collections hote hain, jo duplicate values allow nahi karte.


s = {1, 2, 3, 4, 4, 5}  
print(s)  # {1, 2, 3, 4, 5} (duplicates removed)



# ✅ Frozen Set (frozenset)
# Frozen set immutable hota hai, yani ek baar create hone ke baad change nahi hota.

fs = frozenset([1, 2, 3, 4])
print(type(fs))  # <class 'frozenset'>


# Dictionary (dict)
# Dictionary keys aur values store karta hai.

student = {"name": "Vikram", "age": 21, "city": "Delhi"}
print(student["name"])  # Vikram


# Binary Types
# Binary data ko handle karne ke liye use hota hai.

# ✅ Bytes (bytes)

b = b"Hello"
print(type(b))  # <class 'bytes'>

# Bytearray (bytearray)

ba = bytearray(5)
print(type(ba))  # <class 'bytearray'>


# ✅ Memory View (memoryview)
# Memory view ek object hai, jo memory ko view karta hai.

mv = memoryview(b"Hello")
print(type(mv))  # <class 'memoryview'>


# ✅ None (NoneType)
# NoneType ek special type hai, jo ek value ko represent karta hai. 

n = None
print(type(n))  # <class 'NoneType'>


# Agar ek data type ko doosre me convert karna ho:

a = 5
b = float(a)  # int -> float
c = str(a)    # int -> string
print(b, c)   # 5.0, '5'


# operators

a = 10
b = 20

print(a + b)  # 30
print(a - b)  # -10
print(a * b)  # 200
print(a / b)  # 0.5
print(a % b)  # 10
print(a ** b)  # 100000000000000000000
print(a // b)  # 0


# comparison operators

print(a == b)  # False
print(a != b)  # True       


# logical operators

print(a and b)  # False
print(a or b)  # True
print(not a)  # False


# identity operators

print(a is b)  # False
print(a is not b)  # True


# assignment operators

a = 10
b = 20

a += b  # a = a + b
print(a)  # 30  

a -= b  # a = a - b
print(a)  # -10

a *= b  # a = a * b
print(a)  # 200 

a /= b  # a = a / b
print(a)  # 0.5

a %= b  # a = a % b
print(a)  # 10      

a **= b  # a = a ** b
print(a)  # 100000000000000000000

a //= b  # a = a // b
print(a)  # 0   


# bitwise operators

a = 10
b = 20  

print(a & b)  # 0
print(a | b)  # 30
print(a ^ b)  # 30
print(~a)  # -11
print(a << 1)  # 20
print(a >> 1)  # 5


# # membership operators

# print(a in b)  # False
# print(a not in b)  # True   


# identity operators

print(a is b)  # False
print(a is not b)  # True   



# input('enter your name')

name = input('enter your name')
print("welcome", name )

num1 = int(input('enter first number'))
num2 = int(input('enter second number'))

sum= num1 + num2
print(sum)



