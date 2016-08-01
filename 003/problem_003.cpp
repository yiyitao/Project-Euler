#include <iostream>
#include <math.h>
#include <assert.h>
#include <stdint.h>

using namespace std;

bool isPrime(int n)
{
    assert(n > 0);

    int s = sqrt(n);

    for(int i=s; i > 1; --i)
    {
        if(n%i == 0)
        {
            return false;
        }
    }

    return true;
}

int MaxPrimeFactor(uint64_t n)
{
    assert(n > 0);
    int s = sqrt(n);

    for(int i=s; i > 1; --i)
    {
        if(n%i == 0 && isPrime(i))
        {
            return i;
        }
    }

    return 1;
}

int main()
{
    cout<<"result = "<<MaxPrimeFactor(600851475143)<<endl;
    return 0;
}
