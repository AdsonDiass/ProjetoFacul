# atributos são os dados ou caracteristica do objetos
# metados são onde poondem interagir e se comunicarem com outros objetos
# herança permite que uma classe herde os atributos e metados de outra classe
# encapsulamento e o ato de combina os atributos e metados, torna certo privados ou ocultação de informação
# Poliformismo "muitas formas", subclasse , podendo diferenciar cada um de uma forma.

#Classe

class PrimeiraClasse: 
    def imprimir_mensagem(self,nome):
        print(f"Olá{nome}, seja bem vindo")
        objeto1 = PrimeiraClasse()
        objeto1.imprimir_mensagem('João')

#Construtor da classe

class Televisao:
    def __init__(self): #construtor
        self.volume = 10
    def aumentar_volume(self):
        self.volume += 1
    def diminuir_volume(self):
        self.volume -= 1
tv = Televisao()
print("Volume ao ligar a tv = ", tv.volume)
tv.aumentar_volume()
print("Volume atual = ", tv.volume)

# public private protected 
# tem como fazer a importação de módulo com o import

import requests #fazendo uma requisão WEB

info = requests.get('https://api.github.com/events')
info.headers

# Banco de dados não relacionais e relacionais

#DDL faz parte do grupo de criar,deletar e modificar o banco de dados
#DML faz parte do grupo onde as instruções e dado ao banco, inserir , atualização e excluir algum dado
#DCL faz parte do grupo de segurança do banco de dados

# Criando um banco 

import sqlite3
conn = sqlite3.connect('aulaDB.db')
print(type(conn))

ddl_create = """""
aqui dentro fica os comandos pra criar,inserir e fazer varias coisas no banco de dados
"""""

#sempre tem que estabelecer a conexão com um banco, criar um cursor e executar o comando
#gravar a operação e fechar o cursor e a conexão





 


