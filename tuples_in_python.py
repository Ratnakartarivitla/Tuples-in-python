#tuple
#crreating tuple

x=(1,2,3,'hi',3.2)
print(type(x))
print(x)

#indexing in tuples:
print(x[1])
#slicing
print(x[4:1:-1])
#repetition
print(x*2)
#concat
t1 = (1,2,3)
t2=(4,5,6)
print(t1+t2)
#membership
print(2 in t1)
#iteration
for i in x:
  print(i)
#arthematic operations
print(max(t1),min(t1),sum(t1),len(t1))