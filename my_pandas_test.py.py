import numpy as np
import pandas as pd
dict1={
    "name":['rohan','seema','mahes','sharan'],
    "marks":[3,46,576,23],
    "city":['delhi','calcuta','tamilnadi','srilanka']
}
df=pd.DataFrame(dict1)
print(df)
df.index=[1,2,3,4]
print(df)
ser=pd.Series(np.random.rand(20))
print(ser)
q=type(ser)
print(q)
newdf=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
print(newdf)
ab=newdf.head(3)
print(ab)
sc=newdf.tail(3)
print(sc)
nn=newdf.sort_index(axis=0)
print(nn)
zz=newdf.drop(0,axis=1)
print(zz)
newdf.dropna(inplace=True)