def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (em metros): "))
imc = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")