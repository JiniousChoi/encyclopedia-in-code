// author: jinchoiseoul@gmail.com

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class java_end_of_file {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int lineNo = 1;
        while (scan.hasNext()) {
            System.out.println(lineNo + " " + scan.nextLine());
            lineNo ++;
        }
    }
}
