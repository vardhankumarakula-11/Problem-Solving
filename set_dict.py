print('---------- Problem 1 : ----------')

s = {1,2,3}
s.add(4)
print(s)

print('---------- Problem 2 : ----------')

s = {1,2,3,4,5}
s.remove(4)
print(s)

print('---------- Problem 3 : ----------')

s1 = {1,2,3}
s2 = {4,5,6}
union1 = s1.union(s2)
union2 =  s1 | s2
print(union1)
print(union2)

print('---------- Problem 4 : ----------')

s1 = {1,2,3}
s2 = {2,3,4}
intersection1 = s1.intersection(s2)
intersection2 = s1 & s2
print(intersection1)
print(intersection2)

print('---------- Problem 5 : ----------')

s1 = {1,2,3}
s2 = {2,3,4}
diff1 = s1.difference(s2)
diff2 = s2 - s1
print(diff1)
print(diff2)

print('---------- Problem 6 : ----------')

s1 = {1,2}
s2 = {1,2,3}
issub1 = s1.issubset(s2)
issub2 = s2.issubset(s1)
print(issub1)
print(issub2)

print('---------- Problem 7 : ----------')

s = {1,2,3,4,5}
print(len(s))

print('---------- Problem 8 : ----------')

s = {1,2,3,4,5}
s.clear()
print("Cleared Set : ",s)

print('---------- Problem 9 : ----------')

s1 = {1,2,3}
s2 = {2,3,4}
symd1 = s1.symmetric_difference(s2)
symd2 = s2 ^ s1
print(symd1)
print(symd2)

print('---------- Problem 10 : ----------')

l = [1,2,2,3]
s = set(l)
print(s)

print('---------- Problem 11 : ----------')

l1 = ["a","b"]
l2 = [1,2]
d = dict(zip(l1,l2))
print(d)

print('---------- Problem 12 : ----------')

d = {"a" : 1}
d["a"]=2
print(d)

print('---------- Problem 13 : ----------')

d = {"a" : 1,
     "b" : 2
    }
d.pop("b")
print(d)

print('---------- Problem 14 : ----------')

d = {"a" : 1,
     "b" : 2
    }
if "a" in d:
    print(True)
else:
    print(False)

print('---------- Problem 15 : ----------')

d = {"a" : 1,
     "b" : 2
    }
for i,j in d.items():
    print(i,j)
    
print('---------- Problem 16 : ----------')

d = {"a" : 1,
     "b" : 2
    }
print("lenght of dict : ",len(d))

print('---------- Problem 17 : ----------')

d1 = {"a" : 1}
d2 = {"b" : 2}
d1.update(d2)
d2.update(d1)
print(d1)
print(d2)

print('---------- Problem 18 : ----------')

d1 = {"a" : 1}
print(d1.get("b",0))

print('---------- Problem 19 : ----------')

l = [1,2,2,3]
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

print('---------- Problem 20 : ----------')

d = {"a" : 1,
     "b" : 2
    }
res = {}
for i in d:
    keys = d[i]
    res[keys] = i
print(res)

print('---------- Problem 21 : ----------')

d = {"a" : 1,
     "b" : 5,
     "c" : 3,
     "d" : 2
    }
max = d["b"]
for i in d:
    if d[i]>max:
        max = d[i]
print(max)

print('---------- Problem 23 : ----------')

n = 1
m = 4
d = {}
for i in range(n,m):
    if i not in d:
        d[i] = i**2
print(d)

print('---------- Problem 24 : ----------')

d = {"a" : 10,
     "b" : 15,
     "c" : 8,
     "d" : 12
    }
condition  = 10
res = {}
for i in d:
    if d[i]>condition:
        res[i] = d[i]
print(res)

print('---------- Problem 25 : ----------')

d1 = { "a" : 1,
       "b" : 2
     }
d2 = {
    "a" : 3,
    "c" : 4
}

for i in d2:
    if i in d1:
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)

print('---------- Problem 26 : ----------')

st = "apple banana apple"
a = st.split()
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

print('---------- Problem 28 : ----------')

d1 = { "a" : 1,
       "c" : 2
     }
d2 = {
    "b" : 3,
    "c" : 4
}
for i in d1:
    if i in d2:
        print(i)

print('---------- Problem 30 : ----------')

d = {"a" : 1,
     "b" : 4,
     "c" : 2,
     "d" : 3
    }
val = 2
ed = {}
for i in d:
    if d[i]!=val:
        ed[i] = d[i]
print(ed)
