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

    public void adaugaPunctaj(int punctajAdaugat) {
        this.punctaj += punctajAdaugat;
    }

    @Override
    public String toString() {
        return id + " " + punctaj;
    }
}

class Node {
    Participant participant;
    Node next;

    public Node(Participant participant) {
        this.participant = participant;
        this.next = null;
    }
}

class ClasamentList {
    private Node head;

    public ClasamentList() {
        head = null;
    }

    public synchronized void insertOrUpdate(Participant participant) {
        Node current = head;
        Node prev = null;
        while (current != null) {
            if (current.participant.id.equals(participant.id)) {
                current.participant.adaugaPunctaj(participant.punctaj);
                if (prev != null) {
                    prev.next = current.next;
                } else {
                    head = current.next;
                }
                insertOrdered(current.participant);
                return;
            }
            prev = current;
            current = current.next;
        }
        insertOrdered(participant);
    }

    private synchronized void insertOrdered(Participant participant) {
        Node newNode = new Node(participant);
        if (head == null || head.participant.punctaj < participant.punctaj) {
            newNode.next = head;
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null && current.next.participant.punctaj >= participant.punctaj) {
                current = current.next;
            }
            newNode.next = current.next;
            current.next = newNode;
        }
    }

    public void printListToFile(String fileName) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            Node current = head;
            while (current != null) {
                writer.write(current.participant.toString());
                writer.newLine();
                current = current.next;
            }
        }
    }
}

class CoadaPartajata {
    private final Queue<String> coada = new LinkedList<>();
    private boolean terminat = false;

    public synchronized void adauga(String inregistrare) throws InterruptedException {
        coada.add(inregistrare);
        notifyAll();
    }

    public synchronized String preia() throws InterruptedException {
        while (coada.isEmpty() && !terminat) {
            wait();
        }
        if (coada.isEmpty()) return null;
        return coada.poll();
    }

    public synchronized void finalizeaza() {
        terminat = true;
        notifyAll();
    }
}

class ReaderThread extends Thread {
    private final List<File> fisiere;
    private final CoadaPartajata coada;

    public ReaderThread(List<File> fisiere, CoadaPartajata coada) {
        this.fisiere = fisiere;
        this.coada = coada;
    }

    @Override
    public void run() {
        try {
            for (File fisier : fisiere) {
                try (BufferedReader reader = new BufferedReader(new FileReader(fisier))) {
                    String linie;
                    while ((linie = reader.readLine()) != null) {
                        coada.adauga(linie);
                    }
                } catch (IOException | InterruptedException e) {
                    e.printStackTrace();
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

class WorkerThread extends Thread {
    private final CoadaPartajata coada;
    private final ClasamentList clasament;
    private final Set<String> fraudati;

    public WorkerThread(CoadaPartajata coada, ClasamentList clasament, Set<String> fraudati) {
        this.coada = coada;
        this.clasament = clasament;
        this.fraudati = fraudati;
    }

    @Override
    public void run() {
        try {
            String linie;
            while ((linie = coada.preia()) != null) {
                String[] parts = linie.split(",");
                String id = parts[0].trim();
                int punctaj = Integer.parseInt(parts[1].trim());

                synchronized (clasament) {
                    if (punctaj == -1) {
                        fraudati.add(id);
                        continue;
                    }

                    if (fraudati.contains(id)) continue;

                    clasament.insertOrUpdate(new Participant(id, punctaj));
                }
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class Main {
    private static final String INPUT_DIR = "C:\\Users\\ardel\\IdeaProjects\\PPD\\Lab4\\Paralel\\src\\data";
    private static final String OUTPUT_FILE = "Clasament.txt";

    public static void main(String[] args) throws InterruptedException, IOException {
        long startTime = System.nanoTime();

        int numarProceseWorker = Integer.parseInt(args[0]);
        int numarProceseReader = Integer.parseInt(args[1]);

        // Crearea fisierelor si configurarea cozii
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

        CoadaPartajata coada = new CoadaPartajata();
        ClasamentList clasament = new ClasamentList();
        Set<String> fraudati = new HashSet<>();

        List<List<File>> fileGroups = new ArrayList<>();
        int groupSize = fisiere.length / numarProceseReader;
        for (int i = 0; i < numarProceseReader; i++) {
            List<File> group = new ArrayList<>();
            for (int j = i * groupSize; j < (i + 1) * groupSize && j < fisiere.length; j++) {
                group.add(fisiere[j]);
            }
            fileGroups.add(group);
        }

        // Pornire threaduri Reader
        List<Thread> readerThreads = new ArrayList<>();
        for (int i = 0; i < numarProceseReader; i++) {
            readerThreads.add(new ReaderThread(fileGroups.get(i), coada));
        }

        for (Thread reader : readerThreads) {
            reader.start();
        }

        // Pornire threaduri Worker
        List<Thread> workers = new ArrayList<>();
        for (int i = 0; i < numarProceseWorker; i++) {
            workers.add(new WorkerThread(coada, clasament, fraudati));
        }
        workers.forEach(Thread::start);

        // Așteptare finalizare Readers
        for (Thread reader : readerThreads) {
            reader.join();
        }

        coada.finalizeaza();

        // Așteptare finalizare Workers
        for (Thread worker : workers) {
            worker.join();
        }

        // Scrierea clasamentului final
        clasament.printListToFile(OUTPUT_FILE);
        System.out.println("Clasamentul a fost generat cu succes in " + OUTPUT_FILE);
        long endTime = System.nanoTime();

        System.out.println("Timpul de executie: " + (double)(endTime - startTime) / 1E6 + " ms");
    }
}
