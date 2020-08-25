low_number = int(input('Введите нижний порог чисел:'))
upp_number = int(input('Введите верхний порог чисел:'))
n = int(input("Введите делитель:"))
for i in range(low_number, upp_number + 1):
    if(i % n == 0):
print(i)