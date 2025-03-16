import java.io.*;
import java.util.Random;

public class Main {

    public static void generareMatriceRandom(int n, int m, String filename) throws IOException {
        Random rand = new Random();
        BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
        writer.write(n + " " + m + "\n");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                writer.write(rand.nextInt(100) + " ");
            }
            writer.newLine();
        }
        writer.close();
    }

    public static int[][] citireMatrice(String filename) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filename));
        String[] dimensiuni = reader.readLine().split(" ");
        int n = Integer.parseInt(dimensiuni[0]);
        int m = Integer.parseInt(dimensiuni[1]);
        int[][] matrice = new int[n][m];
        for (int i = 0; i < n; i++) {
            String[] valori = reader.readLine().split(" ");
            for (int j = 0; j < m; j++) {
                matrice[i][j] = Integer.parseInt(valori[j]);
            }
        }
        reader.close();
        return matrice;
    }

    public static void scrieMatrice(int[][] matrice, String filename) throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter(filename));
        for (int[] row : matrice) {
            for (int value : row) {
                writer.write(value + " ");
            }
            writer.newLine();
        }
        writer.close();
    }

    public static int aplicareConvolutie(int[][] borderF, int[][] C, int i, int j) {
        int result = 0;
        int k = C.length / 2;
        for (int ki = -k; ki <= k; ki++) {
            for (int kj = -k; kj <= k; kj++) {
                result += borderF[i + k + ki][j + k + kj] * C[ki + k][kj + k];
            }
        }
        return result;
    }

    public static void convolutieSecventiala(int[][] F, int[][] C, int[][] V, int[][] borderF) {
        int n = F.length;
        int m = F[0].length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                V[i][j] = aplicareConvolutie(borderF, C, i, j);
            }
        }
    }

    public static void convolutieParalelaPeLinii(int[][] F, int[][] C, int[][] V, int[][] borderF, int p) throws InterruptedException {
        int n = F.length;
        int m = F[0].length;

        class ConvolutionThread extends Thread {
            private final int startRow;
            private final int endRow;

            public ConvolutionThread(int startRow, int endRow) {
                this.startRow = startRow;
                this.endRow = endRow;
            }

            @Override
            public void run() {
                for (int i = startRow; i < endRow; i++) {
                    for (int j = 0; j < m; j++) {
                        V[i][j] = aplicareConvolutie(borderF, C, i, j);
                    }
                }
            }
        }

        Thread[] threads = new Thread[p];
        for (int t = 0; t < p; t++) {
            int startRow = t * (n / p);
            int endRow = (t == p - 1) ? n : (t + 1) * (n / p);
            threads[t] = new ConvolutionThread(startRow, endRow);
            threads[t].start();
        }

        for (Thread thread : threads) {
            thread.join();
        }
    }

    public static void convolutieParalelaPeColoane(int[][] F, int[][] C, int[][] V, int[][] borderF, int p) throws InterruptedException {
        int n = F.length;
        int m = F[0].length;

        class ConvolutionThread extends Thread {
            private final int startCol;
            private final int endCol;

            public ConvolutionThread(int startCol, int endCol) {
                this.startCol = startCol;
                this.endCol = endCol;
            }

            @Override
            public void run() {
                for (int j = startCol; j < endCol; j++) {
                    for (int i = 0; i < n; i++) {
                        V[i][j] = aplicareConvolutie(borderF, C, i, j);
                    }
                }
            }
        }

        Thread[] threads = new Thread[p];
        for (int t = 0; t < p; t++) {
            int startCol = t * (m / p);
            int endCol = (t == p - 1) ? m : (t + 1) * (m / p);
            threads[t] = new ConvolutionThread(startCol, endCol);
            threads[t].start();
        }

        for (Thread thread : threads) {
            thread.join();
        }
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        String filename = "date.txt";
        int N = 10000, M = 10;
        int p = 8;

        // Generare matrice random
        generareMatriceRandom(N, M, filename);
        int[][] F = citireMatrice(filename);

        int[][] C = {
                {0, 1, 2, 1, 0},
                {1, 2, 4, 2, 1},
                {2, 4, 8, 4, 2},
                {1, 2, 4, 2, 1},
                {0, 1, 2, 1, 0}
        };

        int[][] borderF = new int[N + 4][M + 4];
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < M; y++) {
                borderF[x + 2][y + 2] = F[x][y];
            }
        }

        int[][] V = new int[N][M];

        // Convolutie secventiala
        long startTime = System.nanoTime();
        convolutieSecventiala(F, C, V, borderF);
        long endTime = System.nanoTime();
        System.out.println("Timp executie secventiala: " + (endTime - startTime) / 1e6 + " ms");
        scrieMatrice(V, "output_secv.txt");

//         Convolutie paralela pe linii
        V = new int[N][M];
        startTime = System.nanoTime();
        convolutieParalelaPeLinii(F, C, V, borderF, p);
        endTime = System.nanoTime();
        System.out.println("Timp executie paralela pe linii (p=" + p + "): " + (endTime - startTime) / 1e6 + " ms");
        scrieMatrice(V, "output_paralel_linii.txt");

        // Convolutie paralela pe coloane
        V = new int[N][M];
        startTime = System.nanoTime();
        convolutieParalelaPeColoane(F, C, V, borderF, p);
        endTime = System.nanoTime();
        System.out.println("Timp executie paralela pe coloane (p=" + p + "): " + (endTime - startTime) / 1e6 + " ms");
        scrieMatrice(V, "output_paralel_coloane.txt");
    }
}
