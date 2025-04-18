def concatenar_dados():
    dado1 = input("Digite o primeiro dado: ")
    dado2 = input("Digite o segundo dado: ")
    resultado = dado1 + " " + dado2
    print("Resultado da concatenação:", resultado)


def repetir_texto():
    texto = input("Digite uma palavra ou frase: ")
    vezes = int(input("Digite quantas vezes deseja repetir: "))
    resultado = texto * vezes
    print("Texto repetido:")
    print(resultado)


def operacoes_matematicas():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    divisao = numero1 / numero2 if numero2 != 0 else "Divisão por zero!"

    print("Soma:", soma)
    print("Subtração:", subtracao)
    print("Multiplicação:", multiplicacao)
    print("Divisão:", divisao)


def verificar_par_ou_impar():
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")


def calcular_media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    print(f"A média das notas é: {media:.2f}")


def verificar_palindromo():
    palavra = input("Digite uma palavra: ")
    if palavra == palavra[::-1]:
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo.")


def menu():
    while True:
        print("\n=== MENU DE DESAFIOS PYTHON ===")
        print("1 - Concatenar Dados")
        print("2 - Repetir Texto")
        print("3 - Operações Matemáticas")
        print("4 - Verificar Par ou Ímpar")
        print("5 - Calcular Média de Notas")
        print("6 - Verificar Palíndromo")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            concatenar_dados()
        elif opcao == "2":
            repetir_texto()
        elif opcao == "3":
            operacoes_matematicas()
        elif opcao == "4":
            verificar_par_ou_impar()
        elif opcao == "5":
            calcular_media()
        elif opcao == "6":
            verificar_palindromo()
        elif opcao == "0":
            print("Saindo... 👋")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Iniciar o programa
menu()
