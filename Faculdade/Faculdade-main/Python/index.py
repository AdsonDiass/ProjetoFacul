valor1 = 10
valor2 = 20

if valor1 > valor2:
    print ('o valor 1 e maior do que o valor2')
else:
    print('o valor2 é maior do que o valor1')    

# estrutura encadeada #

cor = 'verde'

if cor == 'verde':
    print('Acelerar')
elif cor == 'amarelo':
    print('Atenção')
else: 
    print('Parar')

# estruturas de decisoes

qtde_faltas = int(input("Digite a quantidade de faltas: "))
media_final = float(input("Digite a média final: "))

if qtde_faltas <= 5 and media_final >= 7:
    print("Aluno aprovado!")
else: 
    print("Aluno reprovado!")

# estrutura de repetição sempre tera uma decisão 

numero = 1 

while numero != 0:
    numero = int(input("Digite um numero: "))

    if numero % 2 == 0:
        print("Numero par!")
    else: 
        print("Numero impar!")


# for 

nome = "Guido"

for i, c in enumerate(nome):
    print(f"Posição = {i}, valor = {c}")


# controles de repetição

#range(5) #imprimi a quantidade que pedir 
#break # serve pra pular aquela condição ou aquele bloco de codigo 
#continue # pular pra proxima etapa, ignorando a interação do laço
 
 # função eval 

a = 2 
b = 1

equacao = input("Digite a formula geral da equação linear (a * x  + b ): ")
print(f"\nA Entrada do usuario {equacao} e do tipo {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equação para x {x} e {y} ")


