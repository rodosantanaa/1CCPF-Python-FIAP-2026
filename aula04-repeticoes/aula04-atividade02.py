#verificar notas
def verificar_nota(nota):
    while nota < 0 or nota > 10:
        print("nota deve estar entre 0 e 10")
        nota = float(input("digite a nota novamente:"))
    return nota

notaA = float(input("digite a primeira nota: "))
notaA = verificar_nota(notaA)

notaB = float(input("digite a segunda nota: "))
notaB = verificar_nota(notaB)

media = (notaA + notaB) / 2
print(media)
