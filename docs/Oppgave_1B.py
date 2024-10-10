import json
import unittest
import dataclasses



with open(r'C:\Users\krist\OneDrive - Universitetet i Agder\Skrivebord\MOCK_DATA2.json', 'r') as file:
    data = json.load(file)



def find_person(identifier):
    identifier = str(identifier) 
    for person in data:
        if str(person.get('id')) == identifier or person.get('first_name') == identifier or person.get('last_name') == identifier:
            return person.get('group')
    return "Person not on the list"

# Eksempel på bruk
Darcy = find_person("Darcy")
print(Darcy) # Svaret blir 1 (Gruppe)

John = find_person("John")
print(John) # Person not on the list