
import domain.*;
import factory.Container;
import factory.Factory;
import factory.Strategy;
import factory.TaskContainerFactory;
import runner.DelayTaskRunner;
import runner.PrinterTaskRunner;
import runner.StrategyTaskRunner;
import runner.TaskRunner;

import java.time.LocalDateTime;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        MessageTask t1 = new MessageTask("2020", "Ana", "Mesaj5", "Ioana1", "Andrei1", LocalDateTime.now());
        MessageTask t2 = new MessageTask("2021", "Ana2", "Mesaj1", "Ioana2", "Andrei3", LocalDateTime.now());
        MessageTask t3 = new MessageTask("2022", "Ana3", "Mesaj2", "Ioana3", "Andrei2", LocalDateTime.now());
        MessageTask t4 = new MessageTask("2023", "Ana4", "Mesaj3", "Ioana4", "Andrei4", LocalDateTime.now());
        MessageTask t5 = new MessageTask("2024", "Ana5", "Mesaj4", "Ioana5", "Andrei5", LocalDateTime.now());


        TaskRunner runner = new PrinterTaskRunner(new StrategyTaskRunner(Strategy.FIFO));
        runner.addTask(t1);
        runner.addTask(t2);
        runner.addTask(t3);
        runner.addTask(t4);
        runner.addTask(t5);

        runner.executeAll();

        int[] arrayToSort = {5, 2, 9, 1, 5, 6};

        Sorter bubbleSorter = new BubbleSorter();
        SortingTask bubbleSortTask = new SortingTask("1234", "BubbleSort Array", arrayToSort, bubbleSorter);
        bubbleSortTask.execute();

        Sorter quickSorter = new QuickSorter();
        SortingTask quickSortTask = new SortingTask("5678", "QuickSort Array", arrayToSort, quickSorter);
        quickSortTask.execute();

        MessageTask[] messageTasks = {t1, t2, t3, t4, t5};
        if (args.length < 1) {
            System.out.println("Trebuie specificată o strategie (LIFO sau FIFO) în linia de comandă.");
            return;
        }

        Strategy strategy = Strategy.valueOf(args[0]);

        // Creează runner-ul de task-uri folosind StrategyTaskRunner
        TaskRunner strategyRunner = new StrategyTaskRunner(strategy);

        // Adauga task-urile în runner-ul de strategie
        for(MessageTask messageTask : messageTasks){
            strategyRunner.addTask(messageTask);
        }

        strategyRunner.executeAll();

        // Creează un decorator DelayTaskRunner cu o întârziere de 3 secunde
        TaskRunner delayRunner = new DelayTaskRunner(strategyRunner);

        // Executa task-urile cu DelayTaskRunner
        delayRunner.executeAll();

        // Creează un decorator PrinterTaskRunner
        TaskRunner printerRunner = new PrinterTaskRunner(delayRunner);

        // Executa task-urile cu PrinterTaskRunner
        for(MessageTask task : messageTasks){
            printerRunner.executeOneTask();
        }
    }
}