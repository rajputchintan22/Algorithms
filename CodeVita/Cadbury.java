import java.util.Scanner;

public class Main
{

    public static void main(String[] args)
    {
        int output = 0;
        Scanner sc=new Scanner(System.in);
        int p=sc.nextInt();
        int q=sc.nextInt();
        int r=sc.nextInt();
        int s=sc.nextInt();
        sc.close();
        for(int i = p;i<=q;i++)
        {
            for(int j=r;j<=s;j++)
            {
                int a=i;
                int b=j;
                int remain = 1;
                int x;
                while(remain != 0)
                {
                    if (a>=b)
                    {
                        x = (int)(a/b);
                        output+=x;
                        remain = a%b;
                        a=remain;
                    }
                    else
                    {
                        x = (int)(b/a);
                        output+=x;
                        remain = b%a;
                        b=remain;
                    }
                }
            }
        }
        System.out.println(""+output);
    }
}