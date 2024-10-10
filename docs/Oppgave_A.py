def my_str_len(s: str) -> int:
    if s == "":
        return 0
    return 1 + my_str_len(s[1:])

#eksempel på bruk
string = my_str_len("Ukraina")
print(string)

#####################################################################

def my_max(lst: list) -> int:
    if len(lst) == 1:
        return lst[0]
    max_of_rest = my_max(lst[1:])
    return lst[0] if lst[0] > max_of_rest else max_of_rest

print(my_max([1, 2, 3, 4, 5])) # Output 5
