package runner;

import java.time.LocalDateTime;

public class PrinterTaskRunner extends AbstractTaskRunner{
    public PrinterTaskRunner(TaskRunner tr) {
        super(tr);
    }

    @Override
    public void executeOneTask() {
        super.executeOneTask();
        System.out.println("Task executat cu succes la ora " + LocalDateTime.now());
    }

    @Override
    public void executeAll() {
        while (hasTask()) {
            executeOneTask();
        }
    }
}
