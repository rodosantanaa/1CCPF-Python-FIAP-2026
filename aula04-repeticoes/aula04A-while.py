cp = 0

# while cp<3:
#     print(f"produto {cp}")
#     cp += 1
# print()

#filtrando um número específico e limitando o comando
while cp < 10:
    cp += 1
    if cp == 3:
        continue
    print(f"produto {cp}")
    if cp == 7:
        break
print()

#while decrescente 4 até 1

i = 4
while i > 0:
    print(i)
    i -= 1
print()

#recebe número e imprime todos os números de 1 até n
n = int(input("digite um número n:"))
cont = 1
while cont <= n:
    print(cont)
    cont += 1
print()
