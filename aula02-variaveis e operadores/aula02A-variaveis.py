print("ola mundo")
print(7 + 4)
print("7 + 4")
print("7" + "4") #concatenação de strigs

'''
comentario
de varias
linhas
'''

#variaveis
nome = "rodrigo"
idade = 18 #int
peso = 81.6 #float
print(nome, idade, peso)
print(f"ooiiii, {nome}!")

#input -- simula formulario no cmd
nome = input("digite seu nome:")
idade = int(input("digite sua idade:"))
peso = float(input("digite seu peso:"))
print(nome, idade, peso)

#desafio 1
nome = input("digite seu nome:")
print(f"olá! {nome}! Seja bem vindo")

#desafio 2
dia = input("dia do seu nascimento:")
mes = input("mes do seu nascimento:")
ano = input("ano do seu nascimento:")
print("o seu aniversario é no dia:", dia, mes, ano)

#desafio 3
n1 = input("digite um numero:")
n2 = input("digite outro numero:")
print("a soma dos numeros é:", int(n1) + int(n2))
