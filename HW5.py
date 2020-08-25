def func(var_a, var_b):
    if type(var_a) is str or type(var_b) is str:
        return 'str'
    if var_a > var_b:
        return '>'
    if var_a == var_b:
        return '='
    if var_a < var_b:
        return '<'
print(func(5,'2'))
print(func(6,5))
print(func(5,5))
print(func(5,6))