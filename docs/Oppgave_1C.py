#######################################################################

def moon_weight(earth_weight: float) -> float:
    return earth_weight * (1/6)

earth_weight = 100  
print(moon_weight(earth_weight))

########################################################################

#funksjon for å gjøre tall til strings
def num_to_string(numbers):
    return ["pos" if num > 0 else "neg" if num < 0 else "zero" for num in numbers]

#eksempel
numbers = [5, -7, 0, 2, -11, 0.1]
resultat = num_to_string(numbers)
print(resultat)

#########################################################################

def has_string_five(strings):
    return any(len(s) == 5 for s in strings)   

# eksempel
strings = ["inforsmasjonssystemer", "lort", "pepsi", "katt", "snusboks"]
resultat1 = has_string_five(strings)
print(resultat1)

#########################################################################

def even_numbers(numbers):
    return [num for num in numbers if 10 <= num <= 20 and num % 2 == 0]

# eksempel
mockdata_tall = [7, 12, 14, 28, 9, 11, 13, 18]
resultat2 = even_numbers(mockdata_tall)
print(resultat2)

###########################################################################

def all_z_words(wordlist : list) -> list:
    """produce list of words from the input that contain z"""
    zlist = [] # start with an empty list
    for wd in wordlist:
        if "z" in wd:
            zlist = [wd] + zlist
    return(zlist)

# tester for all_z_words
print(all_z_words(['zimbabwe', 'pizza', 'alzheimers']))
print(all_z_words(['home', 'computer', 'table']))

# andre versjonen av funksjonen

def all_z_words2(wordlist : list) -> list:
    return list(filter(lambda wd: 'z' in wd, wordlist))

# tester andre funksjon
print(all_z_words2(['zimbabwe', 'pizzakutter', 'chorizo']))
print(all_z_words2(['egg', 'panne', 'mengde']))

####################################################################'
class Room:
    room: str
    seats: int

classrooms = {
    "room1": {"room": "room1", "seats": 30},
    "room2": {"room": "room2", "seats": 75},
    "room3": {"room": "room3", "seats": 28},
    "room4": {"room": "room4", "seats": 40},
    "room5": {"room": "room5", "seats": 100}
}

#funksjon for å finne antall seter
def num_of_seats(for_code: str, rooms: dict) -> int:
    '''Finne antall seter i et klasserom'''
    if for_code in rooms:
        return rooms[for_code]["seats"]
    return None

# eksempler
print(num_of_seats("room4", classrooms)) # Output: 40
print(num_of_seats("room1", classrooms)) # Output: 30

      
#funksjon for å legge til 10 seter til et rom
def increase_seats(for_code: str, rooms: dict) -> None:
    if for_code in rooms:
        rooms[for_code]["seats"] += 10

# eksempel på increase_seats
increase_seats("room1", classrooms)
print(classrooms["room1"]["seats"])


# finne alle klasserom med kapasitet for 50
above_50 = []

for room_code in classrooms:
    if classrooms[room_code]["seats"] > 50:
        above_50.append(classrooms[room_code])

print(above_50)