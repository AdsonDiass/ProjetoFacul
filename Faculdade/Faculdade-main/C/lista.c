#include <stdio.h>
#include <stdlib.h>


struct Node {
    int dado;
    struct Node * next;
};

void insere_inicio(struct Node** inicio_ref,int new_dado) {
    struct Node* new_node = (struct node*) malloc(sizeof(struct Node));

    new_node->dado= new_dado;
    new_node->next= (*inicio_ref);

    (*inicio_ref) = new_node;
};

//andar pela lista 

void printList(struct Node* node) {
    while(node != NULL) {
        printf("%d", node ->dado);
        node = node ->next;
    }
}

int main() {
    struct Node* inicio = NULL;

    insere_fim(&inicio,6);
    insere_inicio(&inicio,7);
    insere_inicio(&inicio,1);
    insere_fim(&inicio,4);

    printf("\n Lista Criada: ");
    printList(inicio);
    
    return 0;
}

void insere_fim(struct Node** inicio_ref, int new_dado) {
    struct Node* new_node = (struct node*) malloc(sizeof(struct Node));

    struct Node* ultimo = inicio_ref;
    new_node->dado = new_dado;
    new_node->next = NULL;

    if(*inicio_ref == NULL) {
        *inicio_ref=new_node;
        return;
    }

    while(ultimo->next !=NULL) {
        ultimo= ultimo->next;
        ultimo->next = new_node;
        return;
    }
}