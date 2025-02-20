# WAP to ask the user to enter names of thier 3 favourite movies and store them in the list
movies = []
mov1 = input('enter 1st movie')
mov2 = input('enter 2nd movie')
mov3 = input('enter 3rd movie')

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

print(type(movies))


#WAP to count the number of students with th "A" grade in the following tuple?

studentGrade = ["C","D","A","A","B","B","A"]
print(studentGrade.count("A"))


# store the above values in the list and sort it from a to d?

studentGrade.sort()
print(studentGrade)
