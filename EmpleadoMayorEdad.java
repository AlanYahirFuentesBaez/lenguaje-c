import java.util.Scanner;

public class EmpleadoMayorEdad {
    private String nombre;
    private String apellidoMaterno;
    private String apellidoPaterno;
    private double sueldoQuincenal;
    private int imss = 200;
    private double iva = 0.16;
    private double isr = 0.25;
    private double infonavit = 500;    
    private double sueldoTotal;

    // Constructor
    public EmpleadoMayorEdad(String nombre, String apellidoMaterno, String apellidoPaterno, double sueldoQuincenal) {
        this.nombre = nombre;
        this.apellidoMaterno = apellidoMaterno;
        this.apellidoPaterno = apellidoPaterno;
        this.sueldoQuincenal = sueldoQuincenal;
    }

    // Método para calcular el sueldo total
    public void calcularSueldoTotal() {
        double descuentos = imss + iva + (isr*sueldoQuincenal) + infonavit;
        double totalDescuentos = sueldoQuincenal - descuentos;
        sueldoTotal = sueldoQuincenal - totalDescuentos;
    }

    // Método para mostrar la información del empleado
    public void mostrarInfo() {
        System.out.println("Nombre: " + nombre);
        System.out.println("Apellido Materno: " + apellidoMaterno);
        System.out.println("Apellido Paterno: " + apellidoPaterno);
        System.out.println("IMSS: " + imss);
        System.out.println("IVA: " + iva);
        System.out.println("ISR: " + isr);
        System.out.println("Infonavit: " + infonavit);
        System.out.println("Sueldo Quincenal: $" + sueldoQuincenal);
        System.out.println("Sueldo Total: $" + sueldoTotal);
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresa la información del empleado:");
        System.out.print("Nombre: ");
        String nombre = scanner.nextLine();
        System.out.print("Apellido Materno: ");
        String apellidoMaterno = scanner.nextLine();
        System.out.print("Apellido Paterno: ");
        String apellidoPaterno = scanner.nextLine();
        System.out.print("Sueldo Quincenal: ");
        double sueldoQuincenal = scanner.nextDouble();

        EmpleadoMayorEdad empleado1 = new EmpleadoMayorEdad(nombre, apellidoMaterno, apellidoPaterno, sueldoQuincenal);
        empleado1.calcularSueldoTotal();

        System.out.println("\nInformación del empleado:");
        empleado1.mostrarInfo();
        

       

        Scanner scanner2 = new Scanner(System.in);

        System.out.println("Ingresa la información del empleado:");
        System.out.print("Nombre: ");
        String nombre2 = scanner2.nextLine();
        System.out.print("Apellido Materno: ");
        String apellidoMaterno2 = scanner2.nextLine();
        System.out.print("Apellido Paterno: ");
        String apellidoPaterno2 = scanner2.nextLine();
        System.out.print("Sueldo Quincenal: ");
        double sueldoQuincenal2 = scanner2.nextDouble();

        EmpleadoMayorEdad empleado2 = new EmpleadoMayorEdad(nombre2, apellidoMaterno2, apellidoPaterno2, sueldoQuincenal2);
        empleado2.calcularSueldoTotal();

        System.out.println("\nInformación del empleado:");
        empleado2.mostrarInfo();

        scanner.close();
        scanner2.close();
    }
}

