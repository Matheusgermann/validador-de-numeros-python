numeros = []

def adiciona_numero(n):
    if n <= 0:
        print("Selecione Um Número Inteiro Positivo")
    else:
        numeros.append(n)

def exibe_estatisticas():
    if numeros:
        crescente = sorted(numeros)
        print(f"A lista completa é {crescente}")
        print(f"A quantidade de números inseridos é {len(numeros)}")
        print(f"A soma total dos números é {sum(numeros)}")
        print(f"A média dos números é {sum(numeros) / len(numeros):.2f}")
        print(f"O maior número é {max(numeros)} e o menor é {min(numeros)}")
    else:
        print("A lista está vazia.")

def verifica_par_e_multiplo():
    if numeros:
        for numero in sorted(numeros):
            resultado = f"Número {numero}: "
            if numero % 2 == 0:
                resultado += "Par"
            else:
                resultado += "Ímpar"
            if numero % 3 == 0:
                resultado += ", múltiplo de 3"
            if numero % 5 == 0:
                resultado += ", múltiplo de 5"
            print(resultado)
    else:
        print("A lista está vazia.")

def contagem_regressiva():
    if numeros:
        ultimo_numero = numeros[-1]
        if ultimo_numero >= 0 and ultimo_numero % 2 == 0:
            while ultimo_numero >= 0:
                print(ultimo_numero)
                ultimo_numero -= 2
        else:
            print("Não é possível executar a contagem com este valor")
    else:
        print("Lista Vazia")

def menu():

    while True:

        print("\n====== MENU PRINCIPAL ======")
        print("[1] Adicionar número à lista")
        print("[2] Exibir estatísticas")
        print("[3] Verificar paridade e múltiplos")
        print("[4] Mostrar contagem regressiva do último número")
        print("[5] Sair")

        try:
            opcao = int(input("Escolha Uma Opção (1, 2, 3, 4 ou 5): "))

            if opcao == 1:
                try:
                    seleciona_numero = int(input("Digite um Número Inteiro Positivo para Adicionar à lista: "))
                    adiciona_numero(seleciona_numero)
                except ValueError:
                    print("Por favor, insira um número inteiro Positivo")
            
            if opcao == 2:
                exibe_estatisticas()
            
            if opcao == 3:
                verifica_par_e_multiplo()
            
            if opcao == 4:
                contagem_regressiva()

            if opcao == 5:
                print("Encerrando o programa... Até logo!")

                break

        except ValueError:
                print("Opção Inválida. Selecione 1, 2, 3, 4 ou 5")

menu()