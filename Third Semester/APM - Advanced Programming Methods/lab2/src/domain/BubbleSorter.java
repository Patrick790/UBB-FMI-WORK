package domain;

public class BubbleSorter implements Sorter{
    @Override
    public void sort(int[] array) {
        int n = array.length;
        boolean swapped;
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    // Schimbăm elementele dacă ele nu sunt în ordinea corectă
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                    swapped = true;
                }
            }
            // Dacă nu s-a făcut nicio schimbare într-o trecere, atunci vectorul este deja sortat.
            if (!swapped) {
                break;
            }
        }
    }

    @Override
    public String getSorterName() {
        return "BubbleSort";
    }
}
