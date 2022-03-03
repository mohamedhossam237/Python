# name = input("Enter your name:")
# print("Hello " + name)


# import time

birthyear = int (input("Ente you birth year: "))
yearNow = time.localtime().tm_year
age = yearNow - birthyear
print(age)



