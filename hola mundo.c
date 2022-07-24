#include<stdio.h>
#include<stdlib.h>
int main()
{
    int num;
    char nombre[20],edad[3],curp[20];
    printf("Ingresar el número de personas a registrar:/n");
    scanf("%d/n",&num);

    while(num>0){
        num=num-1;
        scanf("/nIngresa el nombre: %s ",&nombre[20]);
        scanf("/nIngresa la edad: %s ",&edad[3]);
        scanf("/nIngresa el curp: %s ",&nombre[20]);

        printf("%s",nombre);
        printf("%s",edad);
        printf("%s",curp);
        print('Ingresa la siguiente persona/n/n');
    }
    

}