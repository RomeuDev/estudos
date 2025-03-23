print("""
      Olá! A classificação dessa calculadora é 
      realizada a partir da tabela fornecida pela 
      Organização Mundial da Saúde (OMS):

+-------------------+-------------------+
|       IMC         |    Diagnóstico    |
+-------------------+-------------------+
| menor que 18,5    | baixo peso        |
| entre 18,5 e 24,9 | intervalo normal  |
| entre 25 e 29,9   | sobrepeso         |
| entre 30 e 34,9   | obesidade classe I|
+-------------------+-------------------+
      """)

def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

# Função para substituir vírgula por ponto e converter para float
def formatar_entrada(valor):
    return float(valor.replace(",", "."))

# Solicitar peso e altura
peso = input("Digite seu peso em kg: ")
altura = input("Digite sua altura em metros: ")

# Converter as entradas para float, substituindo vírgula por ponto
peso = formatar_entrada(peso)
altura = formatar_entrada(altura)

# Calcular e exibir o IMC
imc = calcular_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f}")