abc = 'abcdefghijklmnopqrstuvwxyz'
list_abc = []
for i in range(len(abc)):
    add = abc[i]
    list_abc.append(add)
num = 2
for i in range(8):
    list_abc.pop(num)
    num += 2
print(list_abc)