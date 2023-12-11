pal = input('Ingrese una palabra:')

dic = {}

for letra in pal:
    if letra in dic:
        dic[letra] = dic[letra] + 1
    else:
        dic[letra] = 1

print(dic)