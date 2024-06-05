import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadCSV {
    public static void main(String[] args) {
        String csvFile = "../sheet/order_train0.csv";
        String line = "";
        String csvSplitBy = ",";

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            while ((line = br.readLine()) != null) {
                String[] data = line.split(csvSplitBy);
                String orderDate = data[0];
                String salesRegionCode = data[1];
                String itemCode = data[2];
                String firstCateCode = data[3];
                String secondCateCode = data[4];
                String salesChanName = data[5];
                String itemPrice = data[6];
                String ordQty = data[7];
                System.out.println(orderDate + ", " + salesRegionCode + ", " + itemCode + ", " + firstCateCode + ", " + secondCateCode + ", " + salesChanName + ", " + itemPrice + ", " + ordQty);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}