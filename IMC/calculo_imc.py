def calcular_imc(peso, altura):
    try:
        peso = float(peso)
        altura = float(altura)
        if altura > 0 and peso > 0:
            imc = peso / (altura ** 2)
            return imc
        else:
            return "Valores inválidos. Peso e altura devem ser maiores que zero."
    except ValueError:
        return "Valores inválidos. Certifique-se de inserir números válidos para peso e altura."

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Acima do peso"
    else:
        return "Obeso"

peso = input("Digite o seu peso em Kg: ")
altura = input("Digite a sua altura em metros: ")

resultado_imc = calcular_imc(peso, altura)

if isinstance(resultado_imc, float):
    classificacao = classificar_imc(resultado_imc)
    print(f"Seu IMC é: {resultado_imc:.2f}")
    print(f"Classificação: {classificacao}")
else:
    print(resultado_imc)
