import json

with open(r'C:\Users\krist\OneDrive - Universitetet i Agder\Skrivebord\MOCK_DATA2.json', 'r') as file:
    data = json.load(file)

def find_person(identifikator):
    identifikator = str(identifikator) 
    for person in data:
        if str(person.get('id')) == identifikator or person.get('first_name') == identifikator or person.get('last_name') == identifikator:
            return person.get('group')
    return "Person not on the list"

# Eksempel på bruk
Darcy = find_person("Darcy")
print(Darcy) # Svaret blir 1 (Gruppe)

John = find_person("John")
print(John) # Person not on the list
