package runner;

import domain.Task;
import factory.Container;
import factory.Factory;
import factory.Strategy;
import factory.TaskContainerFactory;

public class StrategyTaskRunner implements TaskRunner{
    private final Container container;
    public StrategyTaskRunner(Strategy strategy){
//        Factory factory = new TaskContainerFactory();
//        container = factory.createContainer(strategy);
        container = TaskContainerFactory.getInstance().createContainer(strategy);
    }

    @Override
    public void executeAll(){
        while(hasTask()) {
            container.remove().run();
        }

    }

    @Override
    public void addTask(Task t) { container.add(t);}

    @Override
    public boolean hasTask() {
        return false;
    }

    @Override
    public void executeOneTask(){
        if(hasTask()){
            container.remove().run();
        }
    }

}