import java.io.*;
/********************************************************************************
 *     Author:Eric,2023
 *
 *     本项目仅用于参加第十一届“泰迪杯”数据挖掘挑战赛，不得用于商业行为。
 *     在比赛结束后，该项目所有源码将开源，使用者可以按照GPL标准下用于参考、学习和分发。
 *     需要注意的是，使用者也应将自己做出的变动进行开源，并注明该源码出自和作者。
 *
 *     学府大道19号
 ********************************************************************************
 *     This project is only used for participating in the 11th "泰迪杯(tipdm.org)" data mining challenge and is not
 *     allowed to be used for commercial purposes.
 *
 *     After the competition, all source code of this project will be open-sourced and users can use it for reference,
 *     learning, and distribution under the GPL standard.
 *
 *     It should be noted that users should also open-source their own modifications and indicate that the source
 *     code comes from and the author.
 *
 *     *发现脱敏数据*
 ********************************************************************************/
public class SelfIntroduction {
    public static void main(String[] args) throws Exception {
        String fileName = "../src/SelfIntroduction.java";
        File inputFile = new File(fileName);

        BufferedReader reader = new BufferedReader(new FileReader(inputFile));

        String line;
        int lineNumber = 1;
        while ((line = reader.readLine()) != null) {
            if (line.trim().startsWith("//")) {
                System.out.println("Line " + lineNumber + ": " + line);
            } else if (line.contains("/*")) {
                while (!line.contains("*/")) {
                    System.out.println("Line " + lineNumber + ": " + line);
                    line = reader.readLine();
                    lineNumber++;
                }
                System.out.println("Line " + lineNumber + ": " + line);
            } else if (line.contains("*") && !line.contains("*/")) {
                System.out.println("Line " + lineNumber + ": " + line.trim());
            }

            lineNumber++;
        }

        reader.close();
    }
}






