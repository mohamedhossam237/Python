#List of Strings 
ls = ['Python', 'C++', 'JavaScript']

#List of Integers
li= [3,8,7,6,4]

#List of boolean 
lb = [True, False,True,True]

#Nested List
nl = [4,5,3,[1.3]]

#mixed list 
x = ['python','c++',2,5,7]

#print variable/s from the list by index
print(x[1]) 
print(x[0:2])
print(x[2:5])
print(x[-1])
#add
x.append(3)
x.insert(1, 'java')

#remove
x.pop() #remove last index
x.pop(3)
x.clear() #remove the list
del x #remove the list
