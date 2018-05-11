x = [2,3,4]
#i is a element
for i in x:
    print(i, end = ' ')
print()
#i is a position
#range(0, len(x), 1)  =  range(len(x))
for i in range(len(x)):
    print(x[i], end=' ')
print()
#idx : value
for idx, i in enumerate(x):
    print(idx+1,i,sep=':')   #sep裡面 (編號:是什麼)
print()

#append增加一個element
x.append(5)
print(x)
#z is a new list, and then copy all element in x,y.
#and assign the reference to variable z
y = [1,43,5,4]
z=x+y
print(x,y,z,sep ='\n')
#z is x ，z只記住x的位置，所以改動z會改動x
z = x
z[0]=99
print(x,z,sep='\n')
#把一個list放入一個list裡面
x.append(y)
print(x)

x[2:3] = [43,65,87]
print(x)