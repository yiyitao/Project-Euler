#include<iostream>

using namespace std;

/*
 * Part1 (2k+1)^2
 * Part2 (2k)^2+1
 * Part3 (2k)^2+1-2k
 * Part4 (2k+1)^2-2k
 * Sum = 1+Sum(Part1) + Sum(Part2) + Sum(part3) + Sum(Part4) (0 < k <= 500)
*/

#define square(i) (i)*(i)

int main()
{
    int Sum = 1;
    for(int i = 1; i <= 500; ++i)
    {
        Sum += square(2*i+1);
        Sum += square(2*i)+1;
        Sum += square(2*i)+1 - 2*i;
        Sum += square(2*i+1) - 2*i;
    }

    cout<<"Sum = "<<Sum<<endl;

    return 0;
}
