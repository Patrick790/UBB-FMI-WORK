import java.io.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.concurrent.locks.*;

class Participant {
    String id;
    int punctaj;
    String tara;

    public Participant(String id, int punctaj, String tara) {
        this.id = id;
        this.punctaj = punctaj;
        this.tara = tara;
    }

    public void adaugaPunctaj(int punctajAdaugat) {
        this.punctaj += punctajAdaugat;
    }

    @Override
    public String toString() {
        return id + ", " + punctaj + ", " + tara;
    }
}

class Node {
    Participant participant;
    Node next;
    final Lock lock = new ReentrantLock();

    public Node(Participant participant) {
        this.participant = participant;
    }
}

class ClasamentList {
    private final Node head;
    private final Node tail;

    public ClasamentList() {
        head = new Node(null);
        tail = new Node(null);
        head.next = tail;
    }

    public void insertOrUpdate(Participant participant, Set<String> fraudati) {
        Node prev = head;
        prev.lock.lock();
        Node current = head.next;

        try {
            while (current != tail) {
                current.lock.lock();
                try {
                    if (current.participant.id.equals(participant.id)) {
                        if (participant.punctaj == -1) {
                            fraudati.add(participant.id);
                            prev.next = current.next; // Remove node
                        } else {
                            current.participant.adaugaPunctaj(participant.punctaj);
                        }
                        return;
                    }
                } finally {
                    prev.lock.unlock();
                    prev = current;
                }
                current = current.next;
            }
            // Adauga nod nou
            if (!fraudati.contains(participant.id) && participant.punctaj != -1) {
                Node newNode = new Node(participant);
                prev.next = newNode;
                newNode.next = tail;
            }
        } finally {
            prev.lock.unlock();
        }
    }

    public List<Participant> toSortedList() {
        List<Participant> result = new ArrayList<>();
        Node current = head.next;
        while (current != tail) {
            result.add(current.participant);
            current = current.next;
        }
        result.sort((p1, p2) -> Integer.compare(p2.punctaj, p1.punctaj));
        return result;
    }

    public void printListToFile(String fileName) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName))) {
            for (Participant p : toSortedList()) {
                writer.write(p.toString());
                writer.newLine();
            }
        }
    }
}

class CoadaPartajata {
    private final Queue<String> coada = new LinkedList<>();
    private final int capacitate;
    private boolean terminat = false;

    private final Lock lock = new ReentrantLock();
    private final Condition coadaPlina = lock.newCondition();
    private final Condition coadaGoala = lock.newCondition();

    public CoadaPartajata(int capacitate) {
        this.capacitate = capacitate;
    }

    public void adauga(String inregistrare) throws InterruptedException {
        lock.lock();
        try {
            while (coada.size() == capacitate) {
                coadaPlina.await();
            }
            coada.add(inregistrare);
            coadaGoala.signalAll();
        } finally {
            lock.unlock();
        }
    }

    public String preia() throws InterruptedException {
        lock.lock();
        try {
            while (coada.isEmpty() && !terminat) {
                coadaGoala.await();
            }
            if (coada.isEmpty()) {
                return null;
            }
            String result = coada.poll();
            coadaPlina.signalAll();
            return result;
        } finally {
            lock.unlock();
        }
    }

    public void finalizeaza() {
        lock.lock();
        try {
            terminat = true;
            coadaGoala.signalAll();
        } finally {
            lock.unlock();
        }
    }
}
class ReaderTask implements Runnable {
    private final File fisier;
    private final CoadaPartajata coada;
    private final String tara;

    public ReaderTask(File fisier, CoadaPartajata coada, String tara) {
        this.fisier = fisier;
        this.coada = coada;
        this.tara = tara;
    }

    @Override
    public void run() {
        try (BufferedReader reader = new BufferedReader(new FileReader(fisier))) {
            String linie;
            while ((linie = reader.readLine()) != null) {
                coada.adauga(linie + "," + tara);
            }
        } catch (IOException | InterruptedException e) {
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
                String tara = parts[2].trim();

                clasament.insertOrUpdate(new Participant(id, punctaj, tara), fraudati);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

public class Main {
    private static final String INPUT_DIR = "C:\\Users\\ardel\\IdeaProjects\\PPD\\Lab5\\Lab5\\src\\data";
    private static final String OUTPUT_FILE = "Clasament.txt";

    public static void main(String[] args) throws InterruptedException, IOException {
        int numarProceseWorker = 4;
        int numarProceseReader = 2;
        int capacitateCoada = 50;

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

        CoadaPartajata coada = new CoadaPartajata(capacitateCoada);
        ClasamentList clasament = new ClasamentList();
        Set<String> fraudati = ConcurrentHashMap.newKeySet();

        ExecutorService readerPool = Executors.newFixedThreadPool(numarProceseReader);
        for (File fisier : fisiere) {
            String tara = fisier.getName().split("_")[0].replace("Rezultate", "");
            readerPool.submit(new ReaderTask(fisier, coada, tara));
        }

        readerPool.shutdown();

        List<Thread> workers = new ArrayList<>();
        for (int i = 0; i < numarProceseWorker; i++) {
            workers.add(new WorkerThread(coada, clasament, fraudati));
        }
        workers.forEach(Thread::start);

        readerPool.awaitTermination(Long.MAX_VALUE, TimeUnit.MILLISECONDS);
        coada.finalizeaza();

        for (Thread worker : workers) {
            worker.join();
        }

        clasament.printListToFile(OUTPUT_FILE);
        System.out.println("Clasamentul a fost generat cu succes in " + OUTPUT_FILE);

        long endTime = System.nanoTime();
        System.out.println("Timp de executie: " + (endTime - startTime) / 1e6 + " ms");
    }
}
