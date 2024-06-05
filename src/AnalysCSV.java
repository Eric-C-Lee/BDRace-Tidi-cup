import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.apache.commons.math3.stat.descriptive.DescriptiveStatistics;
import org.apache.commons.math3.stat.regression.SimpleRegression;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class AnalysCSV {
    public static void main(String[] args) {
        // 读取CSV文件
//        File file = new File("../sheet/od_by_tm.xlsx");
//        CSVFormat format = CSVFormat.DEFAULT.withHeader().withDelimiter(',');
//        List<CSVRecord> records = new ArrayList<>();
//        try (CSVParser parser = CSVParser.parse(file, format)) {
//            records = parser.getRecords();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }

        File file = new File("../sheet/od_by_tm.csv");
        List<CSVRecord> records = new ArrayList<>();
        try (Workbook workbook = WorkbookFactory.create(file)) {
            Sheet sheet = workbook.getSheetAt(0);
            DataFormatter dataFormatter = new DataFormatter();
            for (Row row : sheet) {
//                CSVRecord record = new CSVRecord();
                for (Cell cell : row) {
                    String value = dataFormatter.formatCellValue(cell);
                    String header = "Column" + cell.getColumnIndex();
                    record.put(header, value);
                }
                records.add(record);
            }
        } catch (IOException | InvalidFormatException e) {
            e.printStackTrace();
        }

        // 数据分析
        DescriptiveStatistics stats = new DescriptiveStatistics();
        SimpleRegression regression = new SimpleRegression();
        for (CSVRecord record : records) {
            double price = Double.parseDouble(record.get("产品价格"));
            double demand = Double.parseDouble(record.get("订单需求量"));
            stats.addValue(price);
            regression.addData(price, demand);
        }

        // 保存分析结果
        File resultFile = new File("../sheet/order_train0_result.xlsx");
        try (Workbook workbook = new XSSFWorkbook()) {
            Sheet sheet = workbook.createSheet("分析结果");
            Row row = sheet.createRow(0);
            Cell cell = row.createCell(0);
            cell.setCellValue("产品价格统计信息");
            row = sheet.createRow(1);
            cell = row.createCell(0);
            cell.setCellValue("最小值");
            cell = row.createCell(1);
            cell.setCellValue(stats.getMin());
            row = sheet.createRow(2);
            cell = row.createCell(0);
            cell.setCellValue("最大值");
            cell = row.createCell(1);
            cell.setCellValue(stats.getMax());
            row = sheet.createRow(3);
            cell = row.createCell(0);
            cell.setCellValue("平均值");
            cell = row.createCell(1);
            cell.setCellValue(stats.getMean());
            row = sheet.createRow(4);
            cell = row.createCell(0);
            cell.setCellValue("标准差");
            cell = row.createCell(1);
            cell.setCellValue(stats.getStandardDeviation());
            row = sheet.createRow(6);
            cell = row.createCell(0);
            cell.setCellValue("价格与需求量回归分析");
            row = sheet.createRow(7);
            cell = row.createCell(0);
            cell.setCellValue("斜率");
            cell = row.createCell(1);
            cell.setCellValue(regression.getSlope());
            row = sheet.createRow(8);
            cell = row.createCell(0);
            cell.setCellValue("截距");
            cell = row.createCell(1);
            cell.setCellValue(regression.getIntercept());
            row = sheet.createRow(9);
            cell = row.createCell(0);
            cell.setCellValue("相关系数");
            cell = row.createCell(1);
            cell.setCellValue(regression.getR());
            try (FileOutputStream outputStream = new FileOutputStream(resultFile)) {
                workbook.write(outputStream);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}



//import java.io.File;
//import java.io.IOException;
//import java.io.PrintWriter;
//import java.util.ArrayList;
//import java.util.List;
//import java.io.FileReader;
//
//import org.apache.commons.csv.CSVFormat;
//import org.apache.commons.csv.CSVParser;
//import org.apache.commons.csv.CSVRecord;
//import org.apache.commons.math3.stat.descriptive.DescriptiveStatistics;
//import org.apache.commons.math3.stat.regression.SimpleRegression;
//
//public class AnalysCSV{
//    public static void main(String[] args) {
//        // 读取CSV文件
////        File file = new File("../sheet/od_by_tm.csv");
////        CSVFormat format = CSVFormat.DEFAULT.withHeader().withDelimiter(',');
////        List<CSVRecord> records = new ArrayList<>();
////        try (CSVParser parser = CSVParser.parse(file, format)) {
////            records = parser.getRecords();
////        } catch (IOException e) {
////            e.printStackTrace();
////        }
//        File file = new File("../sheet/od_by_tm.xlsx");
//        CSVFormat format = CSVFormat.DEFAULT.withHeader().withDelimiter(',');
//        List<CSVRecord> records = new ArrayList<>();
//        try (CSVParser parser = CSVParser.parse(new FileReader(file), format)) {
//            records = parser.getRecords();
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//
//        // 数据分析
//        DescriptiveStatistics stats = new DescriptiveStatistics();
//        SimpleRegression regression = new SimpleRegression();
//        for (CSVRecord record : records) {
//            double price = Double.parseDouble(record.get("产品价格"));
//            double demand = Double.parseDouble(record.get("订单需求量"));
//            stats.addValue(price);
//            regression.addData(price, demand);
//        }
//
//        // 保存分析结果
//        File resultFile = new File("../sheet/order_train0_result.xlsx");
//        try (PrintWriter writer = new PrintWriter(resultFile)) {
//            writer.println("产品价格统计信息");
//            writer.println("最小值, " + stats.getMin());
//            writer.println("最大值, " + stats.getMax());
//            writer.println("平均值, " + stats.getMean());
//            writer.println("标准差, " + stats.getStandardDeviation());
//            writer.println();
//            writer.println("价格与需求量回归分析");
//            writer.println("斜率, " + regression.getSlope());
//            writer.println("截距, " + regression.getIntercept());
//            writer.println("相关系数, " + regression.getR());
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }
//}