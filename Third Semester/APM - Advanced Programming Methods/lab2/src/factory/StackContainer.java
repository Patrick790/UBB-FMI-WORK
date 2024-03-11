package factory;

import domain.Task;
import factory.Container;

import java.util.ArrayList;
import java.util.List;

public class StackContainer extends AbstractContainer {

//    private final List<Task> list;
//
//    public StackContainer(){
//        list = new ArrayList<>();
//    }
//    @Override
//    public Task remove() {
//        //TODO test if the list is empty
//        return list.remove(list.size() - 1);
//    }
//
//    @Override
//    public void add(Task task) {
//        list.add(task);
//    }
//
//    @Override
//    public int size() {
//        return list.size();
//    }
//
//    @Override
//    public boolean isEmpty() {
//        return list.isEmpty();
//
//    }
    public StackContainer(ArrayList<Task> tasks){
        this.tasks = tasks;
    }
    public StackContainer(){}

    @Override
    public Task remove(){
        if(isEmpty())
            return null;
        Task removedTask = tasks.get(tasks.size() - 1);
        tasks.remove(tasks.size() - 1);
        return removedTask;
    }
}

