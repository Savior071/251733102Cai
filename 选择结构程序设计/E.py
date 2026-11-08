n = input()
X,Y = map(int,n.split())
if Y % X == 0:
    Z = X + Y
else:
    Z = Y - X
print(Z)