#include <iostream>
#include <stdint.h>
#include <vector>
#include <assert.h>

using namespace std;

bool isPalindromic(uint64_t n)
{
    vector<int> vb;
    do
    {
        vb.push_back(n%10);
    }while(n /= 10);

    for(int i=0, j=vb.size()-1; i < j ; ++i, --j)
    {
        if(vb[i] != vb[j])
        {
            return false;
        }
    }

    return true;
}


uint64_t MaxPalinmoic()
{
    for(int a=99; a > 0; --a)
    {
        for(int b=99; b > 0; --b)
        {
            // first bit is 8 or 9
            if((a*b)%10 < 8)
            {
                continue;
            }

            uint64_t number = (900+a)*(900+b);
            if(isPalindromic(number))
            {
                return number;
            }
        }
    }

    assert(0);  // impossible run to here
    return 0;
}

int main()
{
    cout<<"result = "<<MaxPalinmoic()<<endl;
    return 0;
}
