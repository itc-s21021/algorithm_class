def euclid(x, y):
    if y == 0:
        return x
    else:
        return euclid(y, x%y)

print("a＞bとなる自然数を入力してください")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))
e = euclid(a, b)
f = euclid(c, d)
print("それらの数の最大公約数は", euclid(a, b))