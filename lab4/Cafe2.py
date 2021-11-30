class compaigne():
    def __init__(self,position=""):
        self.position=position
    def info(self):
        print(self.position)
positions=["Администратор","Служащий","Рабочий"]
persons=[]
b=int(input('''Кого вы хотите добавить в компанию? - 
    0.Админ
    1.Служащий
    2.Рабочий 
    - '''))
person_x=compaigne(positions[b])
persons.append(person_x.position)
print(persons)
def PogFriend():
    print("Кто получит премию в этом месяце? - ")
    print(persons)
    x=int(input("введите индекс обьекта - "))
    persons[x]=persons[x]+" получил премию"
    print(persons[x])
PogFriend()

person_x.info()