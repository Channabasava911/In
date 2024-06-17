import java.util.*;
// public class arm
// {
//     public static void main(String args[])
//     {
//         Scanner sc=new Scanner(System.in);
//         int no=sc.nextInt();
//         int revno=no;
//         int l=no.length;
//         int power;
//         int rem=0,sum=0;
//         while(no!=0)
//         {
//             rem=no%10;
//             power=rem**l;
//             sum=sum+power;
//             no=no/10;

//         }
//         if(revno==no)
//         {
//             System.out.println("Armstrong");
//         }
//         else
//         {
//             System.out.println(" NOt an Armstrong");
//         }
//     }
// }

class armstrong
{
   
  public static void printpat(int row,int col)
  {
    for(int i=1;i<=row;i++)
    {
     for(int j=1;j<=col;j++)
     {
        if(i==1 || i==row || j==1 || j==col)
        {
        System.out.print("*");
        }
    }
    System.out.println();
    }
  }
  public static void main(String args[])
  {
    printpat(4,4);
  }

}


