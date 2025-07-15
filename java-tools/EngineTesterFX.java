import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.File;

public class EngineTesterFX extends Application {
    @Override
    public void start(Stage stage) {
        String enginePath = "/Users/Shared/WineEngines/WSCustomARM64.engine";
        File engine = new File(enginePath);
        String message = engine.exists() ? "✅ Engine bulundu." : "❌ Engine bulunamadı.";

        Label label = new Label(message);
        VBox vbox = new VBox(label);
        vbox.setSpacing(10);
        Scene scene = new Scene(vbox, 300, 100);

        stage.setTitle("Wine Engine Tester");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
