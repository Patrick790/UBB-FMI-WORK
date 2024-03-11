package domain;
import java.util.Arrays;

public class SortingTask extends Task{

    private final int[] arrayToSort;
    private final Sorter sorter;

    public SortingTask(String taskID, String descriere, int[] arrayToSort, Sorter sorter){
        super(taskID, descriere);
        this.arrayToSort = arrayToSort;
        this.sorter = sorter;
    }

    @Override
    public void run() {
        System.out.println("Running SortingTask...");
    }

    @Override
    public void execute() {
        System.out.println("Running SortingTask...");
        System.out.println("Sorting array using " + sorter.getSorterName() + " strategy:");
        sorter.sort(arrayToSort);
        System.out.println("Sorted array: " + Arrays.toString(arrayToSort));
    }


}
