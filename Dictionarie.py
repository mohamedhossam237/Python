dic = {
  "name": "Mohamed",
  "age": "22",
  "major": "CS"
}
print(dic)

print(dic["name"])

print(dic.get("name"))
print(dic.keys())


dic["name"] = "Ayda"

dic.update({"major": "CE"})
print(dic)

dic["country"] = "Egypt"

print(dic)

dic.update({"year of birth": "1999"})

print(dic)

dic.pop("year of birth")
print(dic)

dic.popitem()
team = {
  "t1" : {
   "name": "Mohamed",
  },
  "t2" : {
   "name": "Ayda",
  },
  "t3" : {
    "name" : "Doha",
  }
}

print(team["t1"].get('name'))

p1 = {
   "name": "python",
}
p2 = {
  "name" : "java",
}
p3 = {
  "name" : "c++",
}

myfamily = {
  "p1" : p1,
  "p2" : p2,
  "p3" : p3
}