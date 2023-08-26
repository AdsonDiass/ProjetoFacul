
texto = "Aprendendo python na disciplina de linguagem de programação"

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: = {texto[0:6]}")


print (f"texto = {texto}")
print (f"Tamanho do texto = {len(texto)}\n")

palavras = texto.split()

print(f"palabras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")


# vai criar um objeto interavel (range)

numeros = list(range(0,21))
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)


# Tuplas n são mutaveis

# criando um dicionario 

dici_1 = {}
dici_1['nome'] = "João"
dici_1['idade'] = 30

# Algoritimos de busca

# Busca linear vai passar pela lista ou percorrer ate encontar o item especifico 

vogais = 'aeiou'
resultado = vogais.index('e')
print(resultado)

# Complexidade = a melhor forma e mais rapida de deixar o codigo limpo e usar menos recursos

# Busca binaria 

def executar_busca_binaria(lista,valor):
    minimo = 0 
    maximo = len(lista) - 1

    while minimo <= maximo:
        meio = (minimo + maximo) //2 

        if valor < lista [meio]:
            maximo = meio - 1 
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True
        return False # valor não encontrado 
    

# Algoritmos de Ordenação

lista = [10,4,1,15,-3]

lista_ordenada1 = sorted(lista)
lista_ordenada2 = lista.sort()

print('lista =',lista,'\n')

print('lista_ordenada1 = ',lista_ordenada1)
print('lista_ordenada2 = ',lista_ordenada2)

print('lista =',lista)

# mesma coisa que 

lista = [7,4]

if lista[0] > lista[1]:
    aux = lista[1] # ta quardando o valor 4 pra depois colocar ele na frente do 7
    lista[1] = lista[0]
    lista[0] = aux 

print(lista)

# Selection sort serve pra ordernar a lista, ela percorre a lista inteira procurando 
# o menor numero e colocando em ordem

def executar_selection_sort(lista):
    n = len(lista)
    for i in range(0,n):
        index_menor = i
        for j in range(i+1,n):
             if lista[j] < lista[index_menor]:
                 index_menor = j
             lista[i],lista[index_menor] = lista[index_menor], lista[i]
    return lista

lista = [10,9,5,8,11,3]
print(executar_selection_sort(lista))

#Bublble sort ordenção por bolha, verifica dois numeros e compara quem e maior e troca, ate o fim da lista

def executar_bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+ 1] = lista[j + 1], lista[j]
    return lista

lista = [10,9,5,8,11,-1,3]
executar_bubble_sort(lista)

#Merge Sort(ordenação por junção) sai dividindo em varias listas



