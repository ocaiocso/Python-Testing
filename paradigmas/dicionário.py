def menu():
    print("1- Adicionar Evento")
    print("2- Remover Evento")
    print("3- Consultar evento")
    print("0- Sair")


op = menu()
eventos = {}

while op != 0:
    op = int(input("Digite uma opcao:"))
    if op == 1:
        data = input("Informe o dia-mês: ")
        valor= input("Etnre com  valor: ")
        eventos[data] = float(valor)
    elif op == 2:
        data= input("Data a ser exluída dia-mes")
        if data in eventos:
            del eventos[data]
        else:
            print(data+ "Não encontrado!")
    elif op == 3:
        print(list(eventos.values()))
    else:
        print("Opção invalida")

print(eventos)

