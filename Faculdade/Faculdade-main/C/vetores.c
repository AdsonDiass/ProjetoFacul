int main(int argc,char** argv) {
    char nome[30];

    int i;

    printf("Digite o sobrenome do aluno ou aluna:\n");

    gets(nome);

    for (i = 0; nome[i]!= ' '; i++)
    {
        nome[i] = toupper(nome[i]);
        printf("\n\n Sobrenome convertido: %s\n\n",nome);

        getch();
 
    }
}