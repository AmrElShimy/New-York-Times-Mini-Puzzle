import java.nio.file.Files;
import java.time.LocalDate;
import java.util.ArrayList;
import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;

public class getData {
    LocalDate date = LocalDate.now(); // Create a date object
    String date1 = " " + date.getDayOfMonth() + "." + date.getMonthValue() + "." + date.getYear();
    File fileName = new File(
            "D:\\Users\\amr-e\\Desktop\\PL\\PL__Project\\Puzzles\\" + "Puzzle-" + date.getMonthValue() + "-" + date.getDayOfMonth() + ".txt");
    File clueFileName = new File("D:\\Users\\amr-e\\Desktop\\PL\\PL__Project\\Processing Files\\" + "outputFile" + ".txt");

    String line = null;

    public getData() {
    }

    public ArrayList<String> readText() {
        ArrayList<String> acrossHints = new ArrayList<String>();
        ArrayList<String> downHints = new ArrayList<String>();
        ArrayList<String> blocks = new ArrayList<String>();
        try {
            // FileReader reads text files in the default encoding.
            FileReader fileReader = new FileReader(fileName);

            // Always wrap FileReader in BufferedReader.
            BufferedReader bufferedReader = new BufferedReader(fileReader);

            while((line = bufferedReader.readLine()) != null) {
                if (line.charAt(0)== 'A'){
                    String strOut= line.substring(8, line.length());
                    strOut = strOut.substring(0,1) + "." + strOut.substring(1);
                    acrossHints.add(strOut);
                }
                else if (line.charAt(0)== 'D') {
                    String strOut= line.substring(6, line.length());
                    strOut = strOut.substring(0,1) + "." + strOut.substring(1);
                    downHints.add(strOut);
                }
                else {
                    String strOut= line.substring(4, line.length());
                    strOut = strOut.substring(0,1) + "." + strOut.substring(1);
                    blocks.add(strOut);
                }
            }


            bufferedReader.close();
            acrossHints.addAll(downHints);
            acrossHints.addAll(blocks);
            // System.out.println(acrossHints);
            return acrossHints;
        }
        catch(FileNotFoundException ex) {
            System.out.println("Unable to open file '" + fileName + "'");
            return null;
        }
        catch(IOException ex) {
            System.out.println("Error reading file '"+ fileName + "'");
            return null;
        }
    }


    public ArrayList<String> readHints() {
        ArrayList<String> newHints = new ArrayList<String>();
        //ArrayList<String> downHints1 = new ArrayList<String>();
        try {
            String text = new String(Files.readAllBytes(Paths.get(String.valueOf(clueFileName))));
            //System.out.println(text);
            for(int i = 0; i < 5; i++)
            {
                text = text.substring(text.indexOf(i + ". "));
                int incrementIndex = i + 1;
                String acrossNew = text.substring(text.indexOf(":") + 1, text.indexOf("" + incrementIndex));
                newHints.add(" " + acrossNew);
                //System.out.println(acrossNew);
                //System.out.println("-----------------------------------------------------");
            }
            for(int i = 5; i < 9; i++)
            {
                text = text.substring(text.indexOf(i + ". "));
                int incrementIndex = i + 1;
                String downNew = text.substring(text.indexOf(":") + 1, text.indexOf("" + incrementIndex));
                newHints.add(" " + downNew);
                //System.out.println(downNew);
                // System.out.println("-----------------------------------------------------");
            }
            text = text.substring(text.indexOf(9 + ". "));
            String downNew = text.substring(text.indexOf(":") + 1);
            newHints.add(" " + downNew);
            //FileReader fileReader1 = new FileReader(clueFileName);
            //BufferedReader bufferedReader1 = new BufferedReader(fileReader1);
            //System.out.println(bufferedReader1.readLine() != null);

//         while((line = bufferedReader1.readLine()) != null) {
//             if (line.charAt(0)<5){
//             	String strOut1= Character.toString(line.charAt(0))+ Character.toString(line.charAt(3))+Character.toString(line.charAt(4)) +Character.toString(line.charAt(7)) +" "+ line.substring(9, line.length());
//             	acrossHints1.add(strOut1);
//
//             }
//             else{
//                 String strOut1= Character.toString(line.charAt(0))+ Character.toString(line.charAt(3))+Character.toString(line.charAt(4)) +Character.toString(line.charAt(7)) +" "+ line.substring(9, line.length());
//                 downHints1.add(strOut1);
//             	//System.out.println( strOut1);
//             }
//
//             }


            //bufferedReader1.close();
            //  acrossHints1.addAll(downHints1);
            return newHints;
        }
        catch (NullPointerException | IOException ex)
        {
            System.out.println("Null Pointer");
            return null;
        }
//         catch(FileNotFoundException ex) {
//             System.out.println("Unable to open file '" + fileName + "'");
//             return null;
//         }
//         catch(IOException ex) {
//             System.out.println("Error reading file '"+ fileName + "'");
//             return null;
    }
}



