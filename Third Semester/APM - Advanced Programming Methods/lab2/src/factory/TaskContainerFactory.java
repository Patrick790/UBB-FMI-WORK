package factory;

public class TaskContainerFactory implements Factory{

    private TaskContainerFactory() {
    }

    private static TaskContainerFactory instance;

    // Metoda statică pentru obținerea instanței Singleton
    public static TaskContainerFactory getInstance() {
        if (instance == null) {
            instance = new TaskContainerFactory();
        }
        return instance;
    }
    @Override
    public Container createContainer(Strategy strategy) {
        if(strategy == Strategy.LIFO){
            return new StackContainer();
        }
        else if(strategy == Strategy.FIFO)
            return new QueueContainer();
        else return null;
    }
}