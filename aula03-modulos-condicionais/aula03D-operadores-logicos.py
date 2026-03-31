# logica E (and)

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)
print()

# logica OU (or)
logica_ou = False or False or True
print(logica_ou)
print()

# not (inversão)
negacao = not True
print(negacao)

if not verifica_login:
    print("acerta o login ai")
else:
    print("entra no programa")
print()

idade = 18
if idade == 16 and 17 or idade > 70:
    print("seu voto é opcional")
elif idade < 16:
    print("você não pode votar")
else:
    print("seu voto é obrigatório")
