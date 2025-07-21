package java_String;

// import java.lang.String.*;

public class StringTest { // ✅ Renamed class
    public static void main(String[] args) {
        letterFind();
        reverseString();
        vowelCount();
        extractNumbersFromString();
    }

    public static void letterFind() {
        String str = "rambo";     // ✅ Now uses java.lang.String correctly
        char check = 'm';

        if (str.indexOf(check) != -1) {
            System.out.println(check + " is present in " + str);
        } else {
            System.out.println(check + " is not present");
        }
    }

    public static void reverseString() {
        String name = "Rambo";
        String rev = "";

        for(int i=name.length() - 1;i>=0;i--){
            rev = rev + name.charAt(i);
        } 
        System.out.println("reverse number: " + rev);
    }

    public static void vowelCount() {
        String str = "Programming";
        int count = 0;

        for(char c : str.toLowerCase().toCharArray()){
            if ("aeiou".indexOf(c) != -1) {
                count++;
            }
        }
        System.out.println("Vowel count: "+ count);
    }

    public static void extractNumbersFromString() {
        //String sentense = "Scored 10000runs and 345wickets";
        // String[] numbers = sentense.replaceAll("^0-9", " ".trim().split(" "));

        // for(String num : numbers) {
        //     System.out.println(num);
        // }

        String sentence = "Scored 10000runs and 345wickets";

        // ✅ replace non-digits with space, split on space
        String[] numbers = sentence.replaceAll("[^0-9]+", " ").trim().split(" ");

        for (String num : numbers) {
            System.out.println(num);
        }

    }
}
