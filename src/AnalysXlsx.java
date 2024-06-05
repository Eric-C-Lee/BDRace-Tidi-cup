import java.io.File;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

public class AnalysXlsx {
    public static void main(String[] args) {
        String filePath = "../sheet/od_by_tm.xlsx";
        String sheetName = "Sheet1";

        // 读取 Excel 文件
        List<Map<String, Object>> dataList = readExcel(filePath, sheetName);

        // 数据分析
        double[] prices = new double[dataList.size()];
        double[] demands = new double[dataList.size()];
        for (int i = 0; i < dataList.size(); i++) {
            Map<String, Object> data = dataList.get(i);
            double price = (double) data.get("产品价格");
            double demand = (double) data.get("订单需求量");
            prices[i] = price;
            demands[i] = demand;
        }
        double minPrice = getMin(prices);
        double maxPrice = getMax(prices);
        double avgPrice = getAverage(prices);
        double stdDevPrice = getStdDev(prices);
        Map<String, Double> regressionResult = linearRegression(prices, demands);
        double slope = regressionResult.get("slope");
        double intercept = regressionResult.get("intercept");
        double correlationCoefficient = correlation(prices, demands);

        // 输出结果
        System.out.println("产品价格统计信息：");
        System.out.println("最小值：" + minPrice);
        System.out.println("最大值：" + maxPrice);
        System.out.println("平均值：" + avgPrice);
        System.out.println("标准差：" + stdDevPrice);
        System.out.println("价格与需求量回归分析结果：");
        System.out.println("斜率：" + slope);
        System.out.println("截距：" + intercept);
        System.out.println("相关系数：" + correlationCoefficient);
    }

    /**
     * 读取 Excel 文件
     */
    private static List<Map<String, Object>> readExcel(String filePath, String sheetName) {
        List<Map<String, Object>> dataList = new ArrayList<>();

        try (Workbook workbook = new XSSFWorkbook(new FileInputStream(new File(filePath)))) {
            Sheet sheet = workbook.getSheet(sheetName);
            Row headerRow = sheet.getRow(0);

            for (int i = 1; i <= sheet.getLastRowNum(); i++) {
                Row row = sheet.getRow(i);
                Map<String, Object> data = new HashMap<>();

                for (int j = 0; j < headerRow.getLastCellNum(); j++) {
                    Cell cell = row.getCell(j);
                    String columnName = headerRow.getCell(j).getStringCellValue();

                    switch (cell.getCellType()) {
                        case STRING:
                            data.put(columnName, cell.getStringCellValue());
                            break;
                        case NUMERIC:
                            data.put(columnName, cell.getNumericCellValue());
                            break;
                        case BOOLEAN:
                            data.put(columnName, cell.getBooleanCellValue());
                            break;
                        default:
                            data.put(columnName, null);
                            break;
                    }
                }

                dataList.add(data);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return dataList;
    }

    /**
     * 获取数组的最小值
     */
    private static double getMin(double[] array) {
        double min = Double.MAX_VALUE;

        for (double value : array) {
            if (value < min) {
                min = value;
            }
        }

        return min;
    }

    /**
     * 获取数组的最大值
     */
    private static double getMax(double[] array) {
        double max = Double.MIN_VALUE;

        for (double value : array) {
            if (value > max) {
                max = value;
            }
        }

        return max;
    }

    /**
     * 获取数组的平均值
     */
    private static double getAverage(double[] array) {
        double sum = 0.0;

        for (double value : array) {
            sum += value;
        }

        return sum / array.length;
    }

    /**
     * 获取数组的标准差
     */
    private static double getStdDev(double[] array) {
        double average = getAverage(array);
        double sum = 0.0;

        for (double value : array) {
            sum += Math.pow(value - average, 2);
        }

        return Math.sqrt(sum / (array.length - 1));
    }

    /**
     * 计算线性回归（最小二乘法）
     */
    private static Map<String, Double> linearRegression(double[] x, double[] y) {
        double sumX = 0.0;
        double sumY = 0.0;
        double sumXY = 0.0;
        double sumXX = 0.0;
        int n = x.length;

        for (int i = 0; i < n; i++) {
            sumX += x[i];
            sumY += y[i];
            sumXY += x[i] * y[i];
            sumXX += x[i] * x[i];
        }

        double slope = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
        double intercept = (sumY - slope * sumX) / n;

        Map<String, Double> result = new HashMap<>();
        result.put("slope", slope);
        result.put("intercept", intercept);
        return result;
    }

    /**
     * 计算相关系数
     */
    private static double correlation(double[] x, double[] y) {
        double sumXY = 0.0;
        double sumX = 0.0;
        double sumY = 0.0;
        double sumXX = 0.0;
        double sumYY = 0.0;
        int n = x.length;

        for (int i = 0; i < n; i++) {
            sumX += x[i];
            sumY += y[i];
            sumXX += x[i] * x[i];
            sumYY += y[i] * y[i];
            sumXY += x[i] * y[i];
        }

        double numerator = n * sumXY - sumX * sumY;
        double denominator = Math.sqrt((n * sumXX - sumX * sumX) * (n * sumYY - sumY * sumY));
        return numerator / denominator;
    }
}
