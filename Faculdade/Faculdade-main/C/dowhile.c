int main(int argc, char** argv) {
   int i;  

   do{
     printf("\n Digite um numero do sabor \n");

     printf("\t (1) ...flocos \n");
     printf("\t (2) ...Morango \n");
     printf("\t (3) ...Leite condensado \n");

     scanf("%d",&i);
   }while((i<1) || (i>3));

   switch (i)
   {
   case 1:
      printf("\t\t Vc escolheu flocos");
         break;
    case 2:
      printf("\t\t Vc escolheu Morango");
         break;
    case 3:
      printf("\t\t Vc escolheu Leite condensado");
         break;
   }
}