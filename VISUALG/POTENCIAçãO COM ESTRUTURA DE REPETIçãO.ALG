algoritmo "Potenciação com Estrutura de Repetição"
var
    a, b, resultado, contador: inteiro
inicio
    escreva("Digite o valor de 'a': ")
    leia(a)

    escreva("Digite o valor de 'b': ")
    leia(b)

    resultado := 1
    contador := 1

    enquanto contador <= b faca
        resultado := resultado * a
        contador := contador + 1
    fimenquanto

    escreva("O resultado de ", a, " elevado a ", b, " é: ", resultado)
fimalgoritmo
