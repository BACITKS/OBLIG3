
def my_str_len(s: str) -> int:
    if s == "":
        return 0
    return 1 + my_str_len(s[1:])

#eksempel på bruk
string = my_str_len("Ukraina")
print(string) # Output = 7

#####################################################################

def my_max(lst):
    if not lst:
        return None
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
            return max_value
        
my_list = [1, 20, 7, 12, 4]
print(my_max(my_list)) # Output = 7
