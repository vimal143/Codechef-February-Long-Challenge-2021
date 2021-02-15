import java.util.Scanner;

public class HighestDivisor {
    public static void main(String[] args){
        int N;
        Scanner scanner=new Scanner(System.in);
        N=scanner.nextInt();
        for(int i=10;i>=1;i--){
            if(N%i==0){
                System.out.println(i);
                break;
            }
        }
    }
    
}
