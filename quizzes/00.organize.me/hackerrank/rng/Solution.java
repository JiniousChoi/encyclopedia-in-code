import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static int seed_start = 500000000;
    public static int seed_stop =  1501504420;
    
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        int tc = stdin.nextInt();
        while (tc-- > 0) {
            solve(stdin);
        }
        stdin.close();
    }
    
    public static void solve(Scanner stdin) {
        int[] values = new int[10];
        for(int i=0; i<10; i++) {
            values[i] = stdin.nextInt();
        }
        boolean solved = false;
        for(int seed = seed_start; seed <= seed_stop; seed++) {
            Random rng = new Random(seed);
            boolean failed = false;
            for(int j=0; j<10; j++) {
                if(values[j] != rng.nextInt(1000)) {
                    failed = true;
                    break;
                }
            }
            if(!failed) {
                solved = true;
                //for(int k=0; k<10; k++) {
                //    System.out.print(rng.nextInt(1000));
                //    System.out.print(" ");
                //}
                //System.out.println();
                System.out.println("seed: " + seed);
                break;
            }
        }
        if (!solved)
            System.out.println("Failed to solve");
    }
}
