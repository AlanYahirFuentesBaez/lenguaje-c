/*Librería para poder ingresar datos */
import java.util.Scanner;
 /**
esta la clase principal
  */
public class hola {

    /**
     * @param args
     */

    /**
     este es el cuerpo principal
     */
     public static void main(String[] args) {
    /**
    instancia para poder ingresar datos mediante la terminal
     */
        Scanner scanner = new Scanner(System.in);
    /**
    declaracion de las variables
     */
        int x,y,z;
    /**
    mensaje al usuario
     */
        System.out.println("Este es un programa que suma 2 números cualesquiera");
    /**
    es el numero que se va a introducir con la letra
     */
        System.out.println("Ingresa un número x:");
        x=scanner.nextInt();

        System.out.println("Ingresa un número y:");
        y=scanner.nextInt();
    /**
    es el resultado de la operacion del programa 
     */

        z=x-y;
    /**
    imprime el resultado de el programa
     */
        System.out.println("El resultado es:");
        System.out.println(z);     
    /**
    fin de el programa 
    */  
   
        
        
    }
    
}
