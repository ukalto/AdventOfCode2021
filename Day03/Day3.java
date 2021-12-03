import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;

public class Day5 {
    static List<String> input = new ArrayList<>();

    private static List<String> loadArray() {
        try {
            return input = Files.readAllLines(new File("Inputs/Day5.txt").toPath(), Charset.defaultCharset());
        } catch (IOException e) {
            e.printStackTrace();
        }
        return null;
    }

    private static boolean checkZeroBiggerOne(List<String> list, int pos) {
        int countZero = 0;
        int countOne = 0;
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).charAt(pos) == '0')
                countZero++;
            else
                countOne++;
        }
        return countZero > countOne;
    }

    private static String getOxygen(List<String> list) {
        int pos = 0;
        while (list.size() > 1 && pos < list.get(0).length()) {
            List<String> newList = new ArrayList<>();
            if (!checkZeroBiggerOne(list, pos)) {
                for (int i = 0; i < list.size(); i++) {
                    if (list.get(i).charAt(pos) == '1')
                        newList.add(list.get(i));
                }
            } else {
                for (int i = 0; i < list.size(); i++) {
                    if (list.get(i).charAt(pos) == '0')
                        newList.add(list.get(i));
                }
            }
            list = newList;
            pos++;
        }
        return list.get(0);
    }

    private static String getC02(List<String> list) {
        int pos = 0;
        while (list.size() > 1 && pos < list.get(0).length()) {
            List<String> newList = new ArrayList<>();
            if (checkZeroBiggerOne(list, pos)) {
                for (int i = 0; i < list.size(); i++) {
                    if (list.get(i).charAt(pos) == '1')
                        newList.add(list.get(i));
                }
            } else {
                for (int i = 0; i < list.size(); i++) {
                    if (list.get(i).charAt(pos) == '0')
                        newList.add(list.get(i));
                }
            }
            list = newList;
            pos++;
        }
        return list.get(0);
    }

    public static void main(String[] args) {
        loadArray();
        List<String> list1 = new ArrayList<>(input);
        List<String> list2 = new ArrayList<>(input);
        String oxygen = getOxygen(list1);
        String co2 = getC02(list2);
        System.out.println(Integer.parseInt(oxygen, 2) * Integer.parseInt(co2, 2));
    }
}