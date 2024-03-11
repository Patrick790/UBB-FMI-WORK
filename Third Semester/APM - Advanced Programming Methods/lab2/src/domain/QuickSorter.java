package domain;

public class QuickSorter implements Sorter{
    @Override
    public void sort(int[] array){
        quickSort(array, 0, array.length - 1);
    }

    @Override
    public String getSorterName(){
        return "QuickSort";
    }

    private void quickSort(int[] array, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(array, low, high);
            quickSort(array, low, pivotIndex - 1); // Sortați sub-array-ul stânga al pivotului
            quickSort(array, pivotIndex + 1, high); // Sortați sub-array-ul dreapta al pivotului
        }
    }


    private int partition(int[] array, int low, int high) {
        int pivot = array[high];
        int i = low; // Inițializăm indexul i la low
        for (int j = low; j < high; j++) {
            if (array[j] < pivot) {
                int aux = array[i];
                array[i] = array[j];
                array[j] = aux;
                i++;
            }
        }
        int aux = array[i];
        array[i] = array[high];
        array[high] = aux;
        return i;
    }

}
