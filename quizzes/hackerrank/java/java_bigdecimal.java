// author: jinchoiseoul@gmail.com


import java.math.BigDecimal;
import java.util.*;

class java_bigdecimal{

    public static void main(String []args){
        //Input
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        String []s=new String[n+2];
        for(int i=0;i<n;i++){
            s[i]=sc.next();
        }
      	sc.close();

        //Code
        Arrays.sort(s, 0, n, new Comparator<String>() {
           public int compare(String s1, String s2)  {
               BigDecimal b1 = new BigDecimal(s1);
               BigDecimal b2 = new BigDecimal(s2);
               return -b1.compareTo((b2));
           }
        });

        //Output
        for(int i=0;i<n;i++)
        {
            System.out.println(s[i]);
        }
    }

}
