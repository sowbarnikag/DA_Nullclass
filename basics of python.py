print("hello world")
print(34*5)
print(232+343)
#this is a comment
a=['apple','orange']
print(a)
b=[1,2,3,4,4,5,5,6,66,6]
print(b)
t=["hi","hello","how are you"]
print(t)
a=2
if a==0:
    print(1)
else:
    print(0)
i=1
while i<5:
    print(i)
    i=i+1
vegetable=["carrot","cabbage","onion"]
for x in vegetable:
    print(x)
def myfunc(x):
     if x%2==0:
        print(2)
     else:
        print("aaashhh")
myfunc(2)
import numpy as np
a=np.array([1,2,3,4,5,6])
print(a)
print(a[3])
print(a[-1])
b=np.array([12,33,55,7,32,22,])
print(b[1:4])
print(b[:4])
c=b.copy()
print(c)
d=b.view()
print(d)
a=np.array([1,3,4,5,6,7,8,9,10,11,12,13])
b=a.reshape(4,3)
print(b)
c=np.array([13,14,15])
d=np.concatenate([a,c])
print(d)
cf=np.array_split(d,2)
print(cf)
cd=np.where(d==4)
print(cd)
cc=np.where(d%2==0)
print(cc)
c=np.array([3,4,2,10,5])
d=np.sort(c)
print(d)
c=np.array(['apple','orange','banana','mango'])
d=np.sort(c)
print(d)
ss=np.random.randint(100)
print(ss)
ww=np.random.rand(10)
print(ww)
zz=np.zeros(5)
print(zz)
aa=np.ones(2)
print(aa)    
