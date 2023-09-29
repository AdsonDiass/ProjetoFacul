import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

while True:
  tamanho_senha = 6  #Defina o tamanho da senha conforme necessário
  senha_aleatoria = gerar_senha(tamanho_senha)
  print("Senha aleatória:", senha_aleatoria)

  resposta = input("Deseja gerar outra senha? (SIM/NAO): ").strip().lower()
  if resposta != 's' and resposta != 'sim':
        print("Obrigado por usar o gerador de senha.")
        break

#string.ascii_letters: Isso é uma constante que contém todas as letras do alfabeto, tanto maiúsculas quanto minúsculas.
#string.digits: Isso é uma constante que contém os dígitos numéricos de 0 a 9.
#string.punctuation: Isso é uma constante que contém vários caracteres de pontuação, como !, @, #, $, etc.

#random.choice(caracteres): Isso usa a função random.choice para escolher aleatoriamente um caractere da sequência de caracteres definida em caracteres.
#for _ in range(tamanho): Isso cria um loop que escolhe tamanho caracteres aleatórios e os concatena juntos.
#''.join(...): Isso concatena os caracteres escolhidos em uma única string vazia (representada por '').