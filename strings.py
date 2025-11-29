# ......................... STRINGS PROBLEMS ............................ #

#problem 1

def removespaces(a):
    a=' '
    b=""
    for i in name:
        if i not in a:
            b+=i
    return b
name=input("Enter a name : ")
print(removespaces(name))

# problem 2

def rev(x):
    a=name[::-1]
    return a
name=input("Enter a name : ")
print(rev(name))

#problem 3

def rmvspcrev(y):
    a=" "
    b=''
    for i in name:
        if i not in a:
            b+=i
    c=b[::-1]
    return c
name=input("Enter a name : ")
print(rmvspcrev(name))

#problem 4
text=input("Enter a text : ")
wp=""
for i in text:
    if i!=" ":
        wp=i+wp
print(wp)

print()
    
#problem 5

text=input("Enter a text : ")
i=0
res=""
while (i<len(text)):
    if i==0:
        res+=text[i].upper()
    elif text[i]=="_":
        res+=text[i+1].upper()
        i+=1
    else:
        res+=text[i]
    i+=1
print(res)

print()

#problrm 6

var=input("Enter a Camel Case : ")
a=""
for i in var:
    if i.isupper():
        a+="_"+i.lower()
    else:
        a+=i
print("Snake Case : ",a)

# Both cases

text=input("Enter a text : ") #myVarName
i=0
res=""
while (i<len(text)):
    if text[i].isupper():
        res+="_"+text[i].lower()
        i+=1
    else:
        res+=text[i]
        i+=1
print(res)

print()

#problem 7 

var = input("Enter a Camel Case : ")
a=var[0:1].upper()
for i in var[1:len(var)]:
    a+=i
print("Pascal Case : ",a)
    
print()

#problem 8

var = input("Enter a Pascal Case : ")
a=var[0:1].lower()
for i in var[1:len(var)]:
    a+=i
print("Camel Case : ",a)

print()

#problem 9

text=input("Enter a text : ")
res=text[0].lower()
for i in text[1:len(text)]:
    if i.isupper():
        res+="_"+i.lower()
    else:
        res+=i
print(res)

print()
# Problem 10 

text=input("Enter a Text : ")
res=""
i=0
while i<len(text):
    if text[i]==" ":
        res+=text[i+1].upper()
        i+=1
    else:
        res+=text[i]
    i+=1
print(res)

# Problem 11

text=input("Enter a Text : ")
res=""
i=0
while len(text)>i:
    if text[i]==" ":
        res+="_"
    else:
        res+=text[i]
    i+=1
print(res)

# Problem 12 


text=input("Enter a Text : ")
res=text[0].upper()
i=1
while len(text)>i:
    if text[i]==" ":
        res+=text[i+1].upper()
        i+=1
    else:
        res+=text[i]
    i+=1
print(res)

#problem 13

text=input("Enter a text : ")
res=""
for i in text:
    if i.isupper():
        res+=i.lower()
    else:
        res+=i.upper()
print(res)

# problem 14

text=input("Enter a text : ")
b=""
for i in text:
    if i.isdigit():
        b+=i
print(b)

# Problem 15

text=input("Enter a Text : ")
uc=""
lc=""
num=""
sc=""
for i in text:
    if i.isupper():
        uc+=i
    elif i.islower():
        lc+=i
    elif i.isdigit():
        num+=i
    else:
        sc+=i
print("UpperCases : ",uc)
print("LowerCase : ",lc)
print("Digits : ",num)
print("Special Char : ",sc)

# Problem 16

text=input("Enter a Text : ")
uc=0
lc=0
num=0
sc=0
for i in text:
    if i.isupper():
        uc+=1
    elif i.islower():
        lc+=1
    elif i.isdigit():
        num+=1
    else:
        sc+=1
print("UpperCases : ",uc)
print("LowerCase : ",lc)
print("Digits : ",num)
print("Special Char : ",sc)

# problem 17

pas=input("Enter Your Password : ")
if len(pas)>=8:
    uc=0
    lc=0
    num=0
    sp=0
    for i in pas:
        if i.isupper():
            uc+=1
        elif i.islower():
            lc+=1
        elif i.isdigit():
            num+=1
        else:
            sp+=1
    if uc>0 and lc>0 and num>0 and sp>0:
        print("Strong Password")
else:
    print("PassWord Must Be 8 or Above Chars")
            
# Problem 18

text=input("Enter a Text : ")
a=""
for i in text:
    if i not in a:
        a+=i
print(a)

#probmlem 19

name=input("Enter a text : ")
rmvdup=""
dup=""
for i in name:
    if i not in rmvdup:
        rmvdup+=i
    else:
        dup+=i
print(dup)

# Problem 20

let = input("Enter letters :")
nxt=""
for i in let:
    nxt += chr(ord(i)+1)
print(nxt)