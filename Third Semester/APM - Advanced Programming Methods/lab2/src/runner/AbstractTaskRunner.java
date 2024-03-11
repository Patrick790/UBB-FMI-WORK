package runner;

import domain.Task;

public class AbstractTaskRunner implements TaskRunner{

    private final TaskRunner tr;

    public AbstractTaskRunner(TaskRunner tr){ this.tr = tr;}
    @Override
    public void executeOneTask() {
        tr.executeOneTask();
    }

    @Override
    public void executeAll() {
        while(hasTask()){
            executeOneTask();
        }
    }

    @Override
    public void addTask(Task t) {
        tr.addTask(t);
    }

    @Override
    public boolean hasTask() {
        return tr.hasTask();
    }
}
