class Student:
    def __init__(self,name):
        self.name = name 
        self.__math = 0
        self.__phy = 0
        self.__che = 0
        
    # def set_values(self,math,phy,che):
    #     if (math>=0 and math<=100) and (phy>=0 and phy<=100) and (che>=0 and che<=100):
    #         self.__math = math
    #         self.__phy = phy
    #         self.__che = che
    #     else:
    #         print("Invalide Marks")
            
    def set_math(self,math):
        if (math>=0 and math<=100):
            self.__math = math
        else:
            print("Invalide math Marks")
    
    def set_phy(self,phy):
        if (phy>=0 and phy<=100):
            self.__phy = phy
        else:
            print("Invalide phy Marks")
            
    def set_che(self,che):
        if (che>=0 and che<=100):
            self.__che = che
        else:
            print("Invalide che Marks")
            
        
    def get_val(self):
        print("------ Report Card ------")
        print("Stundent Name    : ",self.name)
        print("Maths marks      : ",self.__math)
        print("Phy Marks        : ",self.__phy)
        print("Chemistry Marks  : ",self.__che)
        print("Total marks      : ",self.__math+self.__phy+self.__che)
        print("AVG marks        : ",(self.__math+self.__phy+self.__che)/3)
        
obj1 = Student("Chanti")
obj1.set_math(71)
obj1.set_phy(11)
obj1.set_che(51)
obj1.get_val()