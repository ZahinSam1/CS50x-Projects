people  =[
    {"name": "Abid", "house": "nouga"},
    {"name": "zahin", "house": "Bogura"},
    {"name": "Luffy", "house": "OnePieces"}
]



people.sort(key=lambda person: person["name"])

print(people)