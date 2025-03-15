module com.example.bibliotecaiss {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.apache.logging.log4j;
    requires java.sql;

    opens com.example.bibliotecaiss to javafx.fxml;
    exports com.example.bibliotecaiss;

    exports com.example.bibliotecaiss.controller;
    exports com.example.bibliotecaiss.domain;

    opens com.example.bibliotecaiss.controller to javafx.fxml;
    opens com.example.bibliotecaiss.domain to javafx.fxml;
}