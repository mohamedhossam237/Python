#tuple of strings 
ts =("python", "c++", "java")

#tuple of integers 
ti = (4,2,6,9)

#tuple of boolean
tb = (True,True,False,True)

#mixed Tuple
t = ("python", "c++",5,4,3)

#Access tuble
print (t[1])
print (t[1:3])

#add 
t.append(8)


#update tuple for remove we have to do the same 
l = list(t)
l[1]="java"
t = tuple(l)

print(t)

#Unpacking a Tuple

(x,y,z) = ts

print(x)
print(y)
print(z)

#Join Two Tuples

tj = ts + ti

print(tj)

#Multiply Tuples

tm = ti*2

print(tm)