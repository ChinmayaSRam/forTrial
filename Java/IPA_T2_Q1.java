import java.util.*;

public class IPA_T2_Q1 {
    public static void main(String[] args)
    {
    try (Scanner ip = new Scanner (System. in)) {
        int n = ip.nextInt();
        int sum=0;
        while (n!=0)
        {
        sum += n%10;
        n = n/10;
        }
        if (sum%3==0)
        System.out.println( "TRUE");
        else
        System.out.println("FALSE");
    }
    }
}
