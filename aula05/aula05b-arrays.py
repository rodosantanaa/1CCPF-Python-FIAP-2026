lista_frutas = ["uva", "banana", "melancia"]

# lista_frutas[0] = "uva"
# lista_frutas[1] = "banana"
# lista_frutas[2] = "melancia"

print(lista_frutas[1])
print()

lista_frutas.append("pitaya")
print(lista_frutas[3])
print()

for i in range(len(lista_frutas)):
    print(lista_frutas[i])
print()

for fruta in lista_frutas:
    print(fruta)
