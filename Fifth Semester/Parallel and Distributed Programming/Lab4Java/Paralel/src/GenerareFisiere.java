import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class GenerareFisiere {
    private static final Random random = new Random();

    public static void main(String[] args) throws IOException {
        int numarTari = 5;
        int probleme = 10;
        int minConcurenti = 80;
        int maxConcurenti = 100;
        double probabilitateNerezolvare = 0.1;
        double probabilitateFrauda = 0.02;

        // Create the "data" directory if it doesn't exist
        File dataDir = new File("data");
        if (!dataDir.exists()) {
            dataDir.mkdir();
        }

        for (int tara = 1; tara <= numarTari; tara++) {
            int numarConcurenti = minConcurenti + random.nextInt(maxConcurenti - minConcurenti + 1);
            for (int problema = 1; problema <= probleme; problema++) {
                String numeFisier = "src/data/RezultateC" + tara + "_P" + problema + ".txt";
                BufferedWriter writer = new BufferedWriter(new FileWriter(numeFisier));

                for (int concurent = 1; concurent <= numarConcurenti; concurent++) {
                    String id = "C" + tara + "_" + concurent;

                    // Determinăm dacă concurentul rezolvă problema
                    if (random.nextDouble() < probabilitateNerezolvare) {
                        continue; // Nu adăugăm linia dacă problema nu este rezolvată
                    }

                    // Determinăm dacă este fraudă
                    int punctaj;
                    if (random.nextDouble() < probabilitateFrauda) {
                        punctaj = -1; // Frauda
                    } else {
                        punctaj = 10 + random.nextInt(91); // Punctaj între 10 și 100
                    }

                    writer.write(id + ", " + punctaj);
                    writer.newLine();
                }
                writer.close();
            }
        }

        System.out.println("Fișiere generate cu succes!");
    }
}