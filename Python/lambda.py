people= [
    {"name":"Harry","house":"Gruffin"},
    {"name":"Cho","house":"Ravenclaw"},
    {"name":"Draco","house":"Slythrin"}
]
#Either by
#def f(person):
#    return person["name"]
#people.sort(key=f)
# OR
people.sort(key=lambda person: person["name"])

print(people)