with open("test.txt","w",encoding="utf-8") as file:
    file.write('\nHello worlds')
a=0
names=['Nick',"Walter","Saul"]
numbers=["23423423423",'4214214124214','1241242141241']

with open("test.txt","w",encoding="utf-8") as file:
    for name in names:
        file.write(f'\n{name} {numbers[a]}')
        a+=1
    a=0