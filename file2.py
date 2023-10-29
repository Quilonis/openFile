
with open("test.txt","r",encoding="utf-8") as file:
    data=file.read()
print(data)

author=input("\n>>>>>>Хто автор?:\n")

with open("test.txt","a",encoding="utf-8") as file:
    file.write(f'\n{author}')
