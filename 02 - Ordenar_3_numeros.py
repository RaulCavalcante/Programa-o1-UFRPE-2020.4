x=int(input())
y=int(input())
z=int(input())
if x > y :
    a = x
    x = y
    y = a
if y > z :
    a = y
    y = z
    z = a
print(x,y,z,sep="\n")
