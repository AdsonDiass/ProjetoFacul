int main() {
    float nota1;
    float nota2;
    float media;

    printf("insira nota1: ");
    scanf("%f", &nota1);

    printf("Insira nota 2: ");
    scanf("%f", &nota2);

    media = (nota1 + nota2) / 2;

    printf("media = %f", media);


}

// %c = permite a escrita de apenas um caractere
// %d escrita de numeros inteiros decimais
// %e realiza-se escrita de numeros em notação cientifica
// %f e feota a escrota de numeros reais 
// %s efetua-se a escrita de uma serie de caracteres