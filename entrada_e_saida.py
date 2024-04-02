
def saudar_usuario():
    nome = input("Digite seu nome: ")
    print("Olá," ,nome,"! Seja bem-vindo(a)!")

def soma():
    num1 = (input("Digite o primeiro número: "))
    num2 = (input("Digite o segundo número: "))
    resultado_soma = num1 + num2
    print("A soma dos números é:", resultado_soma)

def multiplicacao():
    num1 = (input("Digite o primeiro número: "))
    num2 = (input("Digite o segundo número: "))
    resultado_multip = num1 * num2
    print("O produto dos números é:", resultado_multip)

def divisao_por_dois():
    num = (input("Digite um número: "))
    resultado_div2 = num / 2
    print("A divisão do número", num, "por dois é:", resultado_div2)

def calcular_imc():
    altura = (input("Digite sua altura em metros: "))
    peso = (input("Digite seu peso em quilogramas: "))
    imc = peso / (altura ** 2)
    print("O seu IMC é:", imc)

saudar_usuario()
soma()
multiplicacao()
divisao_por_dois()
calcular_imc()