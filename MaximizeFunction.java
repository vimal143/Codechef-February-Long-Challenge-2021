import java.util.Arrays;
import java.util.Scanner;

public class MaximizeFunction {
    public static void main(String[] args){
        int tc;
        Scanner scanner=new Scanner(System.in);
        tc=scanner.nextInt();
        while(tc>0){
            int N;
            
            N=scanner.nextInt();
            int [] A=new int[N];
            for(int i=0;i<N;i++){
                A[i]=scanner.nextInt();
            }
            Arrays.sort(A);
            int max=A[N-1];
            int min=A[0];
            int secMin=A[1];
            int ans=Math.abs(min-secMin)+Math.abs(secMin-max)+Math.abs(max-min);
            System.out.println(ans);   
            tc--;
        }
    }
    
}
