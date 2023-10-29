class Pupils():
    def __init__(self,name,surname,mark):
        self.name=name
        self.mark=mark
        self.surname=surname

def find_average(pupils):
    average=0
    for pupil in pupils:
        average+=pupil.mark
    average/=len(pupils)
    print(average)


pupils = list()
with open("tst.txt","r",encoding="utf-8") as file:
    data=file.readlines()
    for d in data:
        print(d)
        p=d.split(" ")
        pupil=Pupils(p[0],p[1],int(p[2]))
        pupils.append(pupil)
find_average(pupils)

