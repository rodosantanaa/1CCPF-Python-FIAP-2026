# função com parâmetro sem retorno
def boas_vindas(nome):
    print(f"olá {nome}! seja bem-vindo!")

nome_digitado = input("digite seu nome: ")
# ou definir o nome antes --> boas_vindas("nome")
boas_vindas(nome_digitado)
print()

# função com parâmetro com retorno
def soma(num_A, num_B):
    soma = num_A + num_B
    return soma
print(soma(4, 3))
