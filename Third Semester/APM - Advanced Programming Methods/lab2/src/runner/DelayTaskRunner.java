package runner;

public class DelayTaskRunner extends AbstractTaskRunner{
    public DelayTaskRunner(TaskRunner tr) {
        super(tr);
    }

    @Override
    public void executeOneTask(){
        try{
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        super.executeOneTask();// Execută task-ul după întârziere
    }

    @Override
    public void executeAll() {
        while (hasTask()) {
            executeOneTask();
        }
    }
}
