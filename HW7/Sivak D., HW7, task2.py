from collections import Counter

def converter(string, delimiter):
    return Counter(string.split(delimiter))

my_str = 'journey, money, house, journey, travel, sea, summer, sea'
delimiter = ', '
print(converter(my_str, delimiter))