import json

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
print(Darcy) # Svaret blir 1

John = find_person("John")
print(John) # Person not on the list

def my_str_len(s: str) -> int:
    if s == "":
        return 0
    return 1 + my_str_len(s[1:])


def my_max(lst: list) -> int:
    if len(lst) == 1:
        return lst[0]
    max_of_rest = my_max(lst[1:])
    return lst[0] if lst[0] > max_of_rest else max_of_rest


def moon_weight(earth_weight: float) -> float:
    return earth_weight * (1/6)

earth_weight = 100  
print(moon_weight(earth_weight))

#funksjon for å gjøre tall til strings
def num_to_string(numbers):
    return ["pos" if num > 0 else "neg" if num < 0 else "zero" for num in numbers]

#eksempel
numbers = [5, -7, 0, 2, -11, 0.1]
resultat = num_to_string(numbers)
print(resultat)


def has_string_five(strings):
    return any(len(s) == 5 for s in strings)   

# eksempel
strings = ["inforsmasjonssystemer", "lort", "pepsi", "katt", "snusboks"]
resultat1 = has_string_five(strings)
print(resultat1)


def even_numbers(numbers):
    return [num for num in numbers if 10 <= num <= 20 and num % 2 == 0]

# eksempel
mockdata_tall = [7, 12, 14, 28, 9, 11, 13, 18]
resultat2 = even_numbers(mockdata_tall)
print(resultat2)


