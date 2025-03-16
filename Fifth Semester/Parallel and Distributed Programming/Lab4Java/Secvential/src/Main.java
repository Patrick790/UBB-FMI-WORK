import java.io.*;
import java.util.*;

class Participant implements Comparable<Participant> {
    String id;
    int punctaj;

    public Participant(String id, int punctaj) {
        this.id = id;
        this.punctaj = punctaj;
    }

    @Override
    public int compareTo(Participant other) {
        return Integer.compare(other.punctaj, this.punctaj);
    }

    @Override
    public String toString() {
        return id + " " + punctaj;
    }
}

public class Main {
    private static final String OUTPUT_FILE = "Clasament.txt";
    private static final String DATA_DIRECTORY = "C:\\Users\\ardel\\IdeaProjects\\PPD\\Lab4\\Secvential\\src\\data";

    public static void main(String[] args) throws IOException {
        long startTime = System.nanoTime();

        File dir = new File(DATA_DIRECTORY);
        File[] files = dir.listFiles((d, name) -> name.startsWith("RezultateC") && name.endsWith(".txt"));

        if (files == null || files.length == 0) {
            System.out.println("No files found in the directory.");
            return;
        }

        List<Participant> listaClasament = new LinkedList<>();
        Set<String> fraudati = new HashSet<>();

        for (File file : files) {
            try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
                String linie;

                while ((linie = reader.readLine()) != null) {
                    String[] parts = linie.split(",");
                    String id = parts[0].trim();
                    int punctaj = Integer.parseInt(parts[1].trim());

                    if (punctaj == -1) {
                        fraudati.add(id);
                        listaClasament.removeIf(p -> p.id.equals(id));
                        continue;
                    }

                    if (fraudati.contains(id)) continue; // Ignora concurentii care au fraudat

                    // Inserare ordonata sau actualizare punctaj
                    boolean gasit = false;
                    ListIterator<Participant> iterator = listaClasament.listIterator();
                    while (iterator.hasNext()) {
                        Participant p = iterator.next();
                        if (p.id.equals(id)) {
                            p.punctaj += punctaj;
                            gasit = true;

                            // Reordonare daca punctajul creste
                            iterator.remove();
                            adaugaOrdonat(listaClasament, p);
                            break;
                        }
                    }

                    if (!gasit) {
                        adaugaOrdonat(listaClasament, new Participant(id, punctaj));
                    }
                }
            }
        }

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(OUTPUT_FILE))) {
            for (Participant p : listaClasament) {
                writer.write(p.toString());
                writer.newLine();
            }
        }

        long endTime = System.nanoTime();
        System.out.printf("Timp de executie: %.2f ms%n", (endTime - startTime) / 1E6);
    }

    private static void adaugaOrdonat(List<Participant> lista, Participant nou) {
        ListIterator<Participant> iterator = lista.listIterator();
        while (iterator.hasNext()) {
            if (nou.compareTo(iterator.next()) < 0) {
                iterator.previous();
                iterator.add(nou);
                return;
            }
        }
        lista.add(nou);
    }
}
