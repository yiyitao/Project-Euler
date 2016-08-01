#include <iostream>

using namespace std;

int sumtoN(const int n)
{
    return n*(n+1)/2;
}

int sumMultiples(const int limit, const int a)
{
    return sumtoN((limit -1)/a)*a;
}

int main()
{
    const int N=1000;
    cout<<"result = "<<(sumMultiples(N,3)+sumMultiples(N, 5)-sumMultiples(N, 15))<<endl;
    return 0;
}
