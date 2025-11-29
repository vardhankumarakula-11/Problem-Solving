print("------------ single Level inheritance : ---------------")

class A:
    def parent(self):
        print("Parent Class.")

class B(A):
    def child(self):
        print("Child Class.")
obj = A()
obj.parent()
print()
obj = B()
obj.parent()
obj.child()

print("------------ Multi Level inheritance : ---------------")

class A:
    def parent(self):
        print("This is Parent Method")
    
class B(A):
    def child(self):
        print("This is Child Method")
        
class C(B):
    def grandChild(self):
        print("This is Grand-Child Method")

obj = A()
obj.parent()
print()
obj = B()
obj.parent()
obj.child()
print()
obj = C()
obj.parent()
obj.child()
obj.grandChild()

print("------------ Multi inheritance : ---------------")

class A:
    def parent1(self):
        print("This is Parent1 Method")
    
class B:
    def parent2(self):
        print("This is parent2 Method")
        
class C(A,B):
    def grandChild(self):
        print("This is Grand-Child Method")
        
obj = A()
obj.parent1()
print()
obj = B()
obj.parent2()
print()
obj = C()
obj.parent1()
obj.parent2()
obj.grandChild()