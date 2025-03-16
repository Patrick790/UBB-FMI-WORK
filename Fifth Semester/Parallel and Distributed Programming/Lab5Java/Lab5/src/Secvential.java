import java.io.*;
import java.util.*;

class Clasament {
    private final Map<String, Participant> participanti = new HashMap<>();
    private final Set<String> fraudati = new HashSet<>();

    public void adaugaSauActualizeazaParticipant(Participant participant) {
        if (participant.punctaj == -1) {
            fraudati.add(participant.id);
            participanti.remove(participant.id);
        } else if (!fraudati.contains(participant.id)) {
            participanti.merge(participant.id, participant, (exist, nou) -> {
                exist.adaugaPunctaj(nou.punctaj);
                return exist;
            });
        }
    }

    public List<Participant> getClasament() {
        List<Participant> lista = new ArrayList<>(participanti.values());
        lista.sort((p1, p2) -> Integer.compare(p2.punctaj, p1.punctaj));
        return lista;
    }

    public void scrieClasamentInFisier(String fileName) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            for (Participant p : getClasament()) {
                writer.write(p.toString());
                writer.newLine();
            }
        }
    }
}

public class Secvential {
    private static final String INPUT_DIR = "C:\\Users\\ardel\\IdeaProjects\\PPD\\Lab5\\Lab5\\src\\data";
    private static final String OUTPUT_FILE = "ClasamentSecvential.txt";

    public static void main(String[] args) {
        File director = new File(INPUT_DIR);
        if (!director.exists() || !director.isDirectory()) {
            System.out.println("Directorul specificat nu exista sau nu este valid!");
            return;
        }

        File[] fisiere = director.listFiles((dir, name) -> name.endsWith(".txt"));
        if (fisiere == null || fisiere.length == 0) {
            System.out.println("Nu exista fisiere .txt in directorul specificat!");
            return;
        }

        long startTime = System.nanoTime();

        Clasament clasament = new Clasament();

        for (File fisier : fisiere) {
            String tara = fisier.getName().split("_")[0].replace("Rezultate", "");
            try (BufferedReader reader = new BufferedReader(new FileReader(fisier))) {
                String linie;
                while ((linie = reader.readLine()) != null) {
                    String[] parts = linie.split(",");
                    String id = parts[0].trim();
                    int punctaj = Integer.parseInt(parts[1].trim());

                    clasament.adaugaSauActualizeazaParticipant(new Participant(id, punctaj, tara));
                }
            } catch (IOException e) {
                System.err.println("Eroare la citirea fisierului " + fisier.getName());
                e.printStackTrace();
            }
        }

        try {
            clasament.scrieClasamentInFisier(OUTPUT_FILE);
            System.out.println("Clasamentul a fost generat cu succes in " + OUTPUT_FILE);
        } catch (IOException e) {
            System.err.println("Eroare la scrierea fisierului de output.");
            e.printStackTrace();
        }

        long endTime = System.nanoTime();
        System.out.println("Timp de executie: " + (endTime - startTime) / 1e6 + " ms");
    }
}