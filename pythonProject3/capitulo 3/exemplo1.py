def soma (numero1, numero2):
    return numero1 + numero2

def subtracao (numer1, numero2):
    return numero1 - numero2

def multiplicacao (numer1, numero2):
    return numero1 * numero2

def divisao (numero1, numero2):
    return numero1 / numero2

numero1 = int(input("digite um numero inteiro!"))
numero2 = int(input("digite outro numero inteiro!"))

resultadoSoma = soma(numero1, numero2)
resultadoSubtracao = subtracao(numero1, numero2) #chamada da funcao
resultadoMultiplicacao = multiplicacao(numero1, numero2)
resultadoDivisao = divisao(numero1, numero2)

print("o resultado da função  é", resultadoSoma)
print("o resultado da função subtração é", resultadoSubtracao)
print("o resultado da função multiplicação é", resultadoMultiplicacao)
print("o resultado da função divisão é", resultadoDivisao)