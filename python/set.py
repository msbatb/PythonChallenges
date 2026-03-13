#l=[10,20,30,"csd"]
#s=set(l)
#s={10,10.5,"csd"}
#print(s)
#s.add(30)
#mutable is unhassable and tuple/immutable is hassable
#in set unhassable type element can add
#l=[15,20,30]
#s.add(l)
#print(s)

#iterable means we can apply loop or for non-iterable we can not apply loop
# s={10,10.5,"csd"}
# l=[10,10.5,"csd1"]
# s.update(l)
# print(s)

# s1={10,10.5,"csd"}
# s2={10,20,30.6}
# s3=s1.union(s2)
# s3=s1 | s2
# print(s1)
# print(s2)
# print(s3)

s1={10,10.5,"csd",20}
s2={10,20,30.6}
s3=s1.intersection(s2)
# s3=s1 & s2
s4=s2.difference(s1)
# s4=s2-s1
s5=s1.symmetric_difference(s2)
# s5=s2^s1
print(s3)
print(s4)
print(s5)

#u=input("enter: ")
#v={"a","e","i","o","u"}
#s=set(u)
#print(s)
#r=v.intersection(s)
#print(r)

#l=[10,20,10,30,20,30,10]
#s=set(l)
#print(s)

