class Rocket:
    def __init__(self, color=str, weight=str):
        self.weight = weight
        self.color = color
        self.color = input("введите цвет корпуса ракеты - ")
        self.weight = input("Введите вес ракеты - ")
class Airplane:
    def __init__(self, length=int):
        self.length= length
        self.Length=input("введите длину корпуса самолёта - ")
class JetPlane(Rocket,Airplane):
    def __init__(self,speed=int,length=int,color=str, weight=str):
        super(JetPlane,self).__init__(length)
        Airplane.__init__(self, color)
        self.speed= speed
        self.speed=input("введите скорость нового реактивного самолёта - ")
    def GetInfo(self):
        print("Новосозданный реактивный самолёт имеет " +self.color+ " цвет и длину корпуса " + self.length + " м. Имеет максимальную скорость " +self.speed+ " километров в час и вес" +self.weight ")
JetPlane.GetInfo()
