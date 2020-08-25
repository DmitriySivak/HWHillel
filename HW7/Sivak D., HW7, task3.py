def square(a):
    if a.isdigit():
            a = float(a)
            p = a * 4
            s = a ** 2
            d = a ** 2 + a ** 2
            diag = d ** .5
            result = [p, s, diag]
    else:
            print("Error")
            result = [0, 0, 0]
    return result

print("Side square = ")
a = input()
res = square(a)
print("\n", res[0], "- Perimeter", "\n", res[1], "- Area", "\n", res[2], "- Diagonal")