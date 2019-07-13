using System;

public class myClass{
	static public void Main (){
		int p = Convert.ToInt32(Console.ReadLine());
		int q = Convert.ToInt32(Console.ReadLine());
		int r = Convert.ToInt32(Console.ReadLine());
		int s = Convert.ToInt32(Console.ReadLine());
		int output=0;
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
        Console.Write(output);
	}
}