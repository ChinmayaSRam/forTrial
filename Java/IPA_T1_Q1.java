import java.util.*;

public class IPA_T1_Q1{
    public static void main(String[] args)
    {
        int i, sum=0, count=0, a[] = new int [5];
        try (Scanner ip = new Scanner (System.in)) 
        {
            for (i=0; i<5; i++)
            {
                a[i] = ip.nextInt();
            }
            
            int loL = ip.nextInt();
            int upL = ip.nextInt();

            for(i=0; i<5; i++)
            {
                if(a[i]>loL && a[i]<upL)
                {
                    sum += a[i];
                    count++;
                }
            }
        }
        System.out.println(sum/count);
    }
}