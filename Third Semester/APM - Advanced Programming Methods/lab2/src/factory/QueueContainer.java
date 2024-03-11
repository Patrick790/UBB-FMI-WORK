package factory;

import domain.Task;
import factory.Container;

import java.util.ArrayList;

public class QueueContainer extends AbstractContainer {
    public QueueContainer(ArrayList<Task> tasks){
        this.tasks = tasks;
    }

    public QueueContainer(){
    }

    @Override
    public Task remove(){
        if(isEmpty())
            return null;
        Task removedTask = tasks.get(0);
        tasks.remove(0);
        return removedTask;
    }

}

