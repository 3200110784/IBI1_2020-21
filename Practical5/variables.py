a=010302
b=190784
c=100321
d=abs(c-a)
e=abs(b-a)
if d<e:
  print("e is bigger")
elif d>e:
  print("d is bigger")
else:
  print("they are same")
x=True
y=False
z=x and not y or not x and y
w=(x!=y)
print(z)
print(w)
if w == z:
 print("w=z")
elif w != z:
 print("wrong!")
exit()

