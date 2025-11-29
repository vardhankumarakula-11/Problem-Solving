print("1")
print("vardhan kumar")
marks=int(input("Enter Marks :  "))
if marks<=100:
    if marks>=91 and marks<=100:
        print("passed Grade : 'O' ",marks)
    elif marks<=90 and marks>=81:
        print("passed Grade : 'A+' ",marks)
    elif marks<=80 and marks>=71:
        print("passed Grade : 'A' ",marks)
    elif marks<=70 and marks>=61:
         print("passed Grade : 'B+' ",marks)
    elif marks<=60 and marks>=51:
         print("passed Grade : 'B' ",marks)
    elif marks<=50 and marks>=41:
        print("passed Grade : 'C+' ",marks)
    elif marks<=40 and marks>=35:
        print("passed Grade : 'C' ",marks)
    else:
        print("failed")
else:
    print("Enter Below 100...")


sec=int(input("Enter Minutes.."))
hs=sec//(3600)
a=sec-(hs*3600)
ms=a//60
ss=a-(ms*60)
print("Hours : ",hs)
print("Minutes : ",ms)
print("Seconds : ",ss)

def prime():
    c=0
    for i in range(1,a+1):
        if (a%i)==0:
            c+=1
    if c==2:
        return ('Prime')
    else:
        return ("Not a Prime")
a=int(input("Enter a num : "))
print(prime())

m=50
for p in range(1,m+1):
    c=0
    for i in range(1,p+1):
        if (p%i)==0:
            c+=1
    if c==2:
        print(p)

#Check Strong password or not 

a=input("Enter Your Password...")
if len(a)<8:
    print("char must be more than 8 ")
else:
    l=0
    u=0
    d=0
    s=0
    for i in a:
        if i.islower():
            l+=1
        elif i.isupper():
            u+=1
        elif i.isdigit():
            d+=1
        else:
            s+=1
    if l>0 and u>0 and d>0 and s>0:
        print("stronge pass")
    else:
         print("not stronge pass")
         
#sum of two heighest values 

a=int(input("num : "))
b=int(input("num : "))
c=int(input("num : "))
if a>b and a>c:
    if b>c:
        print(a+b)
    else:
        print(a+c)
elif b>a and b>c:
    if a>c:
        print(b+a)
    else:
        print(b+c)
else:
    if a>b:
        print(c+a)
    else:
        print(c+b)

#problem solving 

r=7
unit=2
n=8
a=0
c=0
arr=[2,8,3,5,7,4,1,2]
for i in arr:
    a=a+i
    c+=1
    if (r*unit)<=a:
        break
print(c)

#problem solving i/p : aaabbb o/p : a3b3

s=input(" ")
d=dict.fromkeys(s,9)
for i in s:
    d[i]=s.count(i)
res=""
for i,j in d.items():
    res+=i+str(j)
print(res)

#Another Method

s="aabbccccddddd"
res=" "
for i in s:
    if i not in res:
        res+=i+str(s.count(i))
print(res)

#p

n=5
for i in range(0,n):
    print("  "*(n-(i))+"* "*i)
n=5
for i in range(n,0,-1):
    print("  "*(n-(i))+"* "*i)

#p    

n=5
for i in range(1,n):
    print("* "*i)
for i in range(n,0,-1):
    print("* "*i)

#ATM Program...
def depo():
    a=int(input("Enter amount : "))
    if (0<a):
        print((str(a)+" Is Credited."))
        return a
    else:
        print("Please Enter Valid Amount")
        return 0
def withdraw(amount):
    a=int(input("Enter Withdraw Amount : "))
    if (a<amount):
        print(str(a)+" Is Debited.")
        return a
    else:
        print("insufficiant Balance.")
        return 0
def checkbalance(amount):
    return (str(amount)+" Is Your Current Balance.")
i=1
while (i<4):
    pin=1234
    amount=0
    p=int(input("Enter Your Pin Here : "))
    if (pin==p):
        while True:
            print("1) Deposite")
            print("2) Withdraw")
            print("3) Check Balance")
            print("4) Exit")
            opt=int(input("Choose Only One Given Option : "))
            if (opt==1):
                amount+=depo()
            elif (opt==2):
                amount-=withdraw(amount)
            elif (opt==3):
                print(checkbalance(amount))
            elif (opt==4):
                print("Thanks For Visiting...")
                break
            else:
                print("Choose Valid Option")
    else:
        print("Please Enter Correct Pin")
    i+=1
print("Please Try Again After 24hr")




