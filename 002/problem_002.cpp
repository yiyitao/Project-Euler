#include <iostream>
#include <stdint.h>
#include <assert.h>
#include <math.h>

using namespace std;


uint64_t Fibonacci(int n)
{
    assert(n > 0);
    if(n <= 2)
    {
        return 2;
    }

    int _1=1;
    int _2=2;

    uint64_t sum=0;
    for(int i=3; i <= n; ++i)
    {
        sum = _1+_2;
        _1=_2;
        _2=sum;
    }

    return sum;
}

const double PHI=1.618033988749895;     // (1+sqrt(5))/2
const double PSI=-0.6180339887498949;   // (1-sqrt(5))/2

uint64_t Fibonacci2(int n)
{
    assert(n > 0);
    if(n <= 2)
    {
        return 1;
    }

    return ((pow(PHI, n) - pow(PSI,n))/sqrt(5) + 0.5f);
    return 0;
}

int main()
{
    uint64_t sum=0;
    uint64_t tmp=0;
    for(int i=2; true; i+=3)
    {
        tmp = Fibonacci(i);
        if(tmp >= 4000000)
        {
            break;
        }

        sum += tmp;
    }

    cout<<"result = "<<sum<<endl;
    return 0;
}
