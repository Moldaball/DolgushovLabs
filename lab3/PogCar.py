#4.	Измените п.3 так, как если бы функция была членом класса  Car.
class Car:
    def Pog(self,long,width):
        if long==width:
            return "Error"
        else:
            return "Ok"
x=3
y=1
m=Car()
print(m.Pog(x,y))