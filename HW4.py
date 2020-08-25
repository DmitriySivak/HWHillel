var_string = input('Enter your own string : ')
counting_vowels = 0

for i in var_string:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
            or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        counting_vowels = counting_vowels + 1

print('Total number of vowels = ', counting_vowels)