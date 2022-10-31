pets = []

pet = {
    'animal type': 'cat',
    'name': 'Bubbles',
    'owner': 'Ayesha',
    'weight': 15,
    'eats': 'tuna',
}
pets.append(pet)

pet = {
    'animal type': 'Rabbit',
    'name': 'chonky',
    'owner': 'Sameer',
    'weight': 5,
    'eats': 'Carrots',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'Tommy',
    'owner': 'Alyan',
    'weight': 9,
    'eats': 'Bones',
}
pets.append(pet)

for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))