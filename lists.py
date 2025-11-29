# ......................... LISTS PROBLEMS ............................ #

#problem 1
l=[1,2,3,4]
l.append(5)
print(l)

#problem 2
l=[1,2,3,4]
l.remove(3)  #Value
l.pop(1)     # index
print(l)

#problem 3
l=[2,6,11,31,3]
print(max(l))

#problem 4
l=[2,6,11,31,3]
print(min(l))

#problem 5
l=[2,6,11,31,3]
print(sum(l))

#problem 6
l=[1,2,3,4,3,2,3,5,2,6,2]
print(l.count(2))

#problem 7
l=[1,2,3,4]
print(l[::-1])

# problem 8
l = [13, 254, 31, 4]
l.sort()
print(l)

# problem 9
l = [1, 2, 3, 4, 2, 1]
a = set(l)
print(list(a))

# problem 10
l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)

# problem 11
l1 = [1, 2, 3]
l2 = [2, 3, 4]
l3 = []
for i in l1:
    if i in l2:
        l3 += [i]
print(l3)

# problem 12
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evennums = []
for i in l:
    if i % 2 == 0:
        evennums += [i]
print(evennums)

# problem 13
l = [1,2,3,4,5,6,7,8,9]
oddnums = []
for i in l:
    if i % 2 != 0:
        oddnums += [i]
print(oddnums)

# problem 14
l = [1,2,1]
if l != l[::-1]:
    print("True")
else:
    print("False")

# problem 15
l = [0,1,2,-3,-4]
zc = 0
pc = 0
nc = 0
for i in l:
    if i == 0:
        zc += 1
    elif i > 0:
        pc += 1
    else:
        nc += 1
print("Zero Count : ", zc, "Positive Count : ", pc, "Negative Count : ", nc)

# problem 16
l=[1,3,4,5,0,2,6]
l.sort()
secondlargnum = l[len(l)-2:len(l)-1]
print(secondlargnum)
 
# problem 17
l=[1,3,4,5,0,2,6]
l.sort() 
secondsmallnum = l[1:2]
print(secondsmallnum)

# problem 18
l = [1,2,3]
c = l.copy()
print(c)
print(l)

# problem 19
l=[1,2,3,4,5,6,7,8,9]
count=0
for i in l:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i)

# Problem 20
l=[0,3,5,0,9,0]
replace=[]
for i in l:
    if i==0:
        replace.append(-1)
    else:
        replace.append(i)
print(replace)
  
# problem 21      
l=[3,3,3,3,3]  
c=[]
for i in l:
    if i not in c:
        c.append(i)
count=len(c)
if count==1:
    print("True")
else:
    print("False")

# Problem 22

l=[1,2,3,4,2,1,4,5]
val = {}
for i in l:
    if i in val:
        val[i]+=1
    else:
        val[i]=1
print(val)

# Problem 23
l=[[1,2,3],[4,5,6]]
a=[]
for i in l:
    a+=i
print(a)

# Probllem 24
l=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even nums : ",even)
print("Odd Nums : ",odd)

# Problem 25

lst = [1,2,3,4]
sum = 5
res = []
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==sum:
            res.append((lst[i],lst[j]))
print(res)

# Problem 26

l=[1,2,3,4,5,6,7]
for i in l:
    if i%2!=0:
        l.remove(i)
print(l)

# Problem 27

l=[1,2,3,4,5,6,7]
for i in l:
    if i%2==0:
        l.remove(i)
print(l)

# Problem 28

l= list(map(int,input("Enter a list : ").split()))
m=int(input("Enter num : "))
res = []
for i in l:
    res.append(m*i)
print(res)

# Problem 29

l=[1,2,9,5,6]
maxval = max(l)
minval = min(l)
res = maxval-minval
print(res)

# Problem 30

lst = []
if not lst :
    print(True)
else:
    print(False)

# problem 31

l=[1,2,3,4]
l.insert(2,6)
print(l)

# problem 32

l=[1,2,3,2]
num=2
for i in l:
    if i==num:
        l.remove(i)
print(l)

# Problem 33

l=[10,20,30]
a=l.index(30)
print(a)

# Problem 34

l=[2,3,4]
l1=[]
for i in l:
    l1.append(i**2)
print(l1)

# Problem 35

l=[-1,2,-3,4,-5,6]
for i in l:
    if i<0:
        l.remove(i)
print(l)

# Problem 36

l=[1,8,5,3]
gv=4
for i in l:
    if i<gv:
        l.remove(i)
print(l)

# Problem 37

l=[1,2,3,4,3,2]
res=[]
for i in l:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c>1 and i not in res:
        res.append(i)
print(res)

# Problem 38

lst = [1,2,3,4,5,6]
n = 3
for i in lst[:n]:
    lst.append(i)
    lst.remove(i)
print(lst)

# Problem 39

l=[1,2,3,4]
num=21
if num in l:
    print(True)
else:
    print(False)

# Problem 40

lst = [1, 2, 3, 4, 5, 6]
n = 0
m = 2
enp = []
while m <= len(lst):
    enp.append(lst[n:m])
    n += 2
    m += 2
print(enp)