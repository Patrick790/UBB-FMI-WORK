module com.example.motorcyclesclientserver {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;

    opens com.example.motorcyclesclientserver to javafx.fxml;
    exports com.example.motorcyclesclientserver;
}