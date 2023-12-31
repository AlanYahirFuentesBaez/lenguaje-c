/*Librería para poder ingresar datos */
import java.util.Scanner;

public class hola {

    /**
     * @param args
     */
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int x,y,z;
        System.out.println("Este es un programa que suma 2 números cualesquiera");

        System.out.println("Ingresa un número x:");
        x=scanner.nextInt();

        System.out.println("Ingresa un número y:");
        y=scanner.nextInt();


        z=x-y;
        System.out.println("El resultado es:");
        System.out.println(z);     
        

        
        
    }
    
}
