#l=[10,20,30,"csd",10.5]
#print(l)
#print(l[3:2])
#print(l[3:2:-1])
#print(l[-2:-3])
#print(l[-2:-3:-1])
#print(l[1:2:-1])
#print(l[1:2])
#print(l[::])
#print(l[:4])
#print(l[::-1])

#task by teacher
#l=[10,20,30,"csd,10.5"]
#p=0
#r=len(l)
#for ele in l:
#    print(f"element {ele} parsent at {p} and {p-r} index")
#    p=p+1

#while p<=r-1:
#    print(f"element {l[p]} parsent at {p} and {p-r} index")
#    p=p+1

#index()
#def my_index(list,ele):
#    index=0
#    for e in list:
#        if e==ele:
#            return index
#        index=index+1
#
#l=[10,20,"csd",20,20]
#print(my_index(l,20))

#insert()
#l.append(50)
#print(l)
#insert add element where we want 1 is position, 60 is element
#l.insert(1,60)
#print(l)
#if we put any index but that index not available in list then element print at end of list
#l.insert(10,"csd1")
#print(l)
#l.insert(-10,"csd2")
#print(l)

#extend() & remove() & pop()
#joined=["abc","abc1","pqr","xyz"]
#demo=["xyz1","pqr1","xyz3","abc1"]
#print(joined)
#joined.extend(demo)
#print(joined)
#demo.remove("xyz3")
#print(demo)
#demo.pop()
#print(demo)

#reverse() & sort()
#l=[5,10,6,3,6]
#s=["csd","bsd","cpt","csa"]
#l.reverse()
##print(l)
#l.sort()
#print(l)
#s.sort()
#print(s)
#l.sort(reverse=True)
#print(l)

#alising & cloning with copy and silcing
#l=[5,10,8,4,3]
#print(l)
#l1=l.copy()
#l1=l[::]
#l1=l[1:4]
#print(l1)
#print(l is l1)
#l[1]=100
#print(l)
#print(l1)

#mathmatical
#l=[5,10,8,4,3]
#l1=[1,2,6,7,11]
#l2=l+l1
#l3=l*3
#print(l2)
#print(l3)

#comparison of list
#l=[5,10,8,4,3]
#l1=[5,8,110,4,3]
#l2=[5,10,8,4,3]
#print(l==l1)
#print(l==l2)
#print(l1==l2)
#print(l is l1)
#print(l is l2)
#print(l>l1)
#print(l<l1)

#membership operators
#l=[5,"csd",8,4,3]
#print(8 in l)
#print(8 not in l)
#print(18 in l)
#print(18 not in l)

#user=input("enter word: ")
#v=["a","e","i","o","u"]
#l=[]
#for ele in user:
#    if ele in v:
#        if ele not in l:
#            l.append(ele)
#print(l)

#nested list
#l=[10,[20.30],40]
#stu=[["abc",1,45],["abc1",2,56]]
#print(stu[0])
#print(stu[0][2])

#list comprehension
#l1=[i for i in range(1,51)]
#print(l1)

#Task
#l=[]
#for i in range(8):
#    l.append(2**i)
#print(l)
#
#l2=[2**i for i in range(8)]
#print(l2)

#l1=[i**2+1 for i in range(9)]
#print(l1)

#l=[10,20,30,40,50]
#l1=[40,50,20]
#l2=[]
#for i in l:
#    if i not in l1:
#        l2.append(i)
#print(l2)

#l2=[i for i in l if i not in l1]
#print(l2)