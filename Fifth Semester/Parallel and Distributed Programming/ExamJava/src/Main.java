import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.time.Instant;
import java.util.Random;
import java.util.concurrent.*;
import java.util.concurrent.atomic.AtomicInteger;

class Request {
    int id;
    int resourceType;
    int status;  // 0 = waiting, 1 = processing, 2 = finished
    long timestamp;

    public Request(int id, int resourceType) {
        this.id = id;
        this.resourceType = resourceType;
        this.status = 0;
    }
}

class UserThread extends Thread {
    private final int count;
    private static final Random random = new Random();
    private static final int tu = 30; // interval intre cereri
    private static final BlockingQueue<Request> mainQueue = Main.mainQueue;
    private static final AtomicInteger waitingRequests = Main.waitingRequests;

    public UserThread(int count) {
        this.count = count;
    }

    @Override
    public void run() {
        int requestsMade = 0;
        while (Main.isRunning && requestsMade < count) {
            try {
                int resourceType = random.nextInt(3) + 1;
                Request request = new Request(requestsMade, resourceType);
                mainQueue.put(request);
                waitingRequests.incrementAndGet();
                requestsMade++;
                Thread.sleep(tu);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }
}

class LibrarianThread extends Thread {
    private static final BlockingQueue<Request> mainQueue = Main.mainQueue;
    private static final BlockingQueue<Request> cartiQueue = Main.cartiQueue;
    private static final BlockingQueue<Request> articoleQueue = Main.articoleQueue;
    private static final BlockingQueue<Request> revisteQueue = Main.revisteQueue;
    private static final AtomicInteger waitingRequests = Main.waitingRequests;
    private static final AtomicInteger processingRequests = Main.processingRequests;

    @Override
    public void run() {
        while (Main.isRunning || !mainQueue.isEmpty()) {
            try {
                Request request = mainQueue.poll(100, TimeUnit.MILLISECONDS);
                if (request != null) {
                    waitingRequests.decrementAndGet();
                    processingRequests.incrementAndGet();

                    switch (request.resourceType) {
                        case 1 -> cartiQueue.put(request);
                        case 2 -> articoleQueue.put(request);
                        case 3 -> revisteQueue.put(request);
                    }
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }
}

class DepartmentThread extends Thread {
    private final BlockingQueue<Request> queue;
    private final int type;
    private static final Random random = new Random();
    private static final int Xr = 150; // sleep pt accesarea cererii
    private static final AtomicInteger processingRequests = Main.processingRequests;
    private static final AtomicInteger finishedRequests = Main.finishedRequests;

    public DepartmentThread(BlockingQueue<Request> queue, int type) {
        this.queue = queue;
        this.type = type;
    }

    @Override
    public void run() {
        while (Main.isRunning || !queue.isEmpty()) {
            try {
                Request request = queue.poll(100, TimeUnit.MILLISECONDS);
                if (request != null) {
                    request.status = 1; // in procesare
                    Thread.sleep(Xr + random.nextInt(60)); // 120-180 ms pt simulare procesare cerere

                    request.status = 2; // finalizat
                    request.timestamp = Instant.now().toEpochMilli();

                    processingRequests.decrementAndGet();
                    finishedRequests.incrementAndGet();

                    // Scriere în fișier
                    Main.writeToFile(request);
                }
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                break;
            }
        }
    }
}

public class Main {
    private static final int U = 4; // thread-uri utilizatori
    private static final int Yu = 20; // cereri per utilizator
    private static final int R = 4; // bibliotecari
    private static final int Rm = 250; // interval de monitorizare
    private static final int Dt = 6000; // durata de rulare

    protected static final BlockingQueue<Request> mainQueue = new LinkedBlockingQueue<>();
    protected static final BlockingQueue<Request> cartiQueue = new LinkedBlockingQueue<>();
    protected static final BlockingQueue<Request> articoleQueue = new LinkedBlockingQueue<>();
    protected static final BlockingQueue<Request> revisteQueue = new LinkedBlockingQueue<>();

    protected static final AtomicInteger waitingRequests = new AtomicInteger(0);
    protected static final AtomicInteger processingRequests = new AtomicInteger(0);
    protected static final AtomicInteger finishedRequests = new AtomicInteger(0);

    protected static volatile boolean isRunning = true;

    public static void main(String[] args) throws InterruptedException {
        UserThread[] userThreads = new UserThread[U];
        for (int i = 0; i < U; i++) {
            userThreads[i] = new UserThread(Yu);
            userThreads[i].start();
        }

        LibrarianThread[] librarianThreads = new LibrarianThread[R];
        for (int i = 0; i < R; i++) {
            librarianThreads[i] = new LibrarianThread();
            librarianThreads[i].start();
        }

        // Creare si pornire thread-uri departamente
        DepartmentThread cartiThread = new DepartmentThread(cartiQueue, 1);
        DepartmentThread articoleThread = new DepartmentThread(articoleQueue, 2);
        DepartmentThread revisteThread = new DepartmentThread(revisteQueue, 3);

        cartiThread.start();
        articoleThread.start();
        revisteThread.start();

        // Pornire thread monitorizare
        Thread monitor = new Thread(Main::monitor);
        monitor.start();

        // Rularea sistemului pentru Dt milisecunde
        Thread.sleep(Dt);
        isRunning = false;

        for (UserThread userThread : userThreads) {
            userThread.join();
        }

        // Așteptare finalizare bibliotecari
        for (LibrarianThread librarianThread : librarianThreads) {
            librarianThread.join();
        }

        // Așteptare finalizare departamente
        cartiThread.join();
        articoleThread.join();
        revisteThread.join();

        // Oprire monitorizare
        monitor.interrupt();
    }

    protected static synchronized void writeToFile(Request request) {
        try (FileWriter fw = new FileWriter("output.txt", true);
             BufferedWriter bw = new BufferedWriter(fw);
             PrintWriter out = new PrintWriter(bw)) {
            out.printf("Request ID: %d, Type: %d, Status: %d, Timestamp: %d%n",
                    request.id, request.resourceType, request.status, request.timestamp);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void monitor() {
        while (isRunning) {
            try {
                System.out.printf("[MONITOR] Waiting: %d, Processing: %d, Finished: %d%n",
                        waitingRequests.get(), processingRequests.get(), finishedRequests.get());
                Thread.sleep(Rm);
            } catch (InterruptedException e) {
                break;
            }
        }
    }
}
