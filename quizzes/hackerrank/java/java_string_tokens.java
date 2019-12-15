// author: jinchoiseoul@gmail.com


import java.io.*;
import java.util.*;


public class java_string_tokens {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String orig = scan.nextLine().trim();
        // Write your code here.
        String[] tokens = orig.split("[ !,?._'@]+");
        int size = orig.isEmpty() ? 0 : tokens.length;
        
        System.out.println(size);
        for (String token : tokens) {
            System.out.println(token);
        }
        scan.close();
    }
}

