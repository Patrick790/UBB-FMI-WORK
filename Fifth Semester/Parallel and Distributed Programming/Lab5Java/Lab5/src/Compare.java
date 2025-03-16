import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Objects;

public class Compare {
    private static final String INPUT_DIR = "C:\\Users\\ardel\\IdeaProjects\\PPD\\Lab5\\Lab5\\src\\data";
    private static final String OUTPUT_FILE_SEQ = "ClasamentSecvential.txt";
    private static final String OUTPUT_FILE_PAR = "Clasament.txt";

    public static void main(String[] args) throws InterruptedException, IOException {
        int runs = 10;
        double totalDurationSeq = 0;
        double totalDurationPar = 0;

        for (int i = 0; i < runs; i++) {
            // Measure time for sequential execution
            long startTimeSeq = System.nanoTime();
            Secvential.main(new String[]{});
            long endTimeSeq = System.nanoTime();
            totalDurationSeq += (endTimeSeq - startTimeSeq) / 1e6;

            // Measure time for parallel execution
            long startTimePar = System.nanoTime();
            Main.main(new String[]{});
            long endTimePar = System.nanoTime();
            totalDurationPar += (endTimePar - startTimePar) / 1e6;
        }

        double averageDurationSeq = totalDurationSeq / runs;
        double averageDurationPar = totalDurationPar / runs;

        System.out.println("Medie secvential: " + averageDurationSeq + " ms");
        System.out.println("Medie paralel: " + averageDurationPar + " ms");

        // Verify if the output files are identical
        boolean areFilesIdentical = compareFiles(OUTPUT_FILE_SEQ, OUTPUT_FILE_PAR);
        System.out.println("Fisierele sunt identice: " + areFilesIdentical);
    }

    private static boolean compareFiles(String file1, String file2) throws IOException {
        try (BufferedReader reader1 = new BufferedReader(new FileReader(file1));
             BufferedReader reader2 = new BufferedReader(new FileReader(file2))) {

            String line1, line2 = null;
            while ((line1 = reader1.readLine()) != null && (line2 = reader2.readLine()) != null) {
                if (!Objects.equals(line1, line2)) {
                    return false;
                }
            }
            return line1 == null && line2 == null;
        }
    }
}