def verificar_maioridade():
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")


def verificar_par_impar():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

def verificar_aprovacao():
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado.")

verificar_maioridade()
verificar_par_impar()
verificar_aprovacao()
