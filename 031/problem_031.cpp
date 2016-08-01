#include <iostream>

using namespace std;


int main()
{
    int counter = 0;
    for(int _1=0; _1 <= 200; ++_1)
    {
        for(int _2=0; _2 <= 100; ++_2)
        {
            for(int _3=0; _3 <= 40; ++_3)
            {
                for(int _4=0; _4 <= 20; ++_4)
                {
                    for(int _5=0; _5 <= 10; ++_5)
                    {
                        for(int _6=0; _6 <= 4; ++_6)
                        {
                            for(int _7=0; _7 <= 2; ++_7)
                            {
                                if(_1 + 2*_2 + 5*_3 + 10*_4 + 20*_5 + 50*_6 + 100*_7 == 200)
                                {
                                    ++counter;
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    ++counter;
    cout<<counter<<endl;

    return 0;
}
