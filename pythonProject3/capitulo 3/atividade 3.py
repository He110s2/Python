def calculaDiametro(raio):
    return 2 * raio

def calculaCircunferencia(pi, raio):
    return pi * raio * 2

def calculaArea(pi, raio):
    return pi * (raio ** 2)
raio = float(input("insira um numero do raio"))
pi = 3.14159

diametro = calculaDiametro(raio)
circunferencia = calculaCircunferencia(pi, raio)
area = calculaArea(raio, raio)

print("area: ", area)
print("diametro: ", diametro)
print("circunferencia: ", circunferencia)