escolha_usuario = int(input())

match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("entrar do programa")
    case _:
        print("erro!")