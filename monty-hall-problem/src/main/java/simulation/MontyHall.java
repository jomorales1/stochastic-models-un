package simulation;

import java.util.Random;
import java.util.Scanner;

public class MontyHall {
    // Variables que almacenan el número de victorias cambiando
    // y sin cambiar de puerta
    private static int wins_changing = 0;
    private static int wins_not_changing = 0;

    // Método que representa las diferentes rondas
    private static void simulate() {
        Random random = new Random();
        int win_door = random.nextInt(3);
        int selection = random.nextInt(3);
        if (selection == win_door) {
            wins_not_changing++;
        } else {
            wins_changing++;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingrese el número de simulaciones: ");
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            simulate();
        }
        double wc_percent = (double) wins_changing / n;
        double wnc_percent = (double) wins_not_changing / n;
        System.out.println("Porcentaje de victorias cambiando: " + wc_percent);
        System.out.println("Porcentaje de victorias sin cambiar: " + wnc_percent);
    }
}
