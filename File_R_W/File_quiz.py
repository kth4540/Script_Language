import os
import shelve
def get_key(x):
    return x[1]


c={}

for fn in os.listdir('.'):
    c[fn]=os.path.getsize(fn)

result=sorted(c.items(),key=get_key)

print(result)


f=open('report.txt','w')

f.write('\n'.join(result))

f.close()




