#include<iostream>
#include<string>
#include<string.h>
#include<assert.h>

using namespace std;

#define ARR_SIZE(x) (sizeof(x)/sizeof(x[0]))

struct basic
{
    const char *number;
    int length;
    basic(const char *n)
        :number(n)
    {
        length = strlen(number);
    }
};

static const basic basicNumbers[]=
{
    {""},
    {"one"},
    {"two"},
    {"three"},
    {"four"},
    {"five"},
    {"six"},
    {"seven"},
    {"eight"},
    {"nine"},
    {"ten"},
    {"eleven"},
    {"twelve"},
    {"thirteen"},
    {"fourteen"},
    {"fifteen"},
    {"sixteen"},
    {"seventeen"},
    {"eighteen"},
    {"nineteen"},
};


static const basic decialNumber[]=
{
    {""},
    {""},
    {"twenty"},
    {"thirty"},
    {"fotry"},
    {"fifty"},
    {"sixty"},
    {"seventy"},
    {"eighty"},
    {"ninety"}
};


static const basic lecimal[]=
{
    {"hundred"},
    {"thousand"}
};


string number2english(int number)
{
    if(number < 9999 && number >=1000)
    {
        int a = number/1000;
        int b = number%1000;
        string s;
        if(b/100 == 0) s = "and";
        return string(basicNumbers[a].number) + " " + string(lecimal[1].number) + " " + s + " " + number2english(number%1000);
    }
    
    if(number < 999 && number >= 100)
    {
        int a = number/100;
        if(number == 100) return string(basicNumbers[a].number) + " " + string(lecimal[0].number);
        return string(basicNumbers[a].number) + " " + string(lecimal[0].number) + " " + string("and") + " " + number2english(number%100);
    }

    if(number <= 99 && number >= 20)
    {
        int a = number/10;
        int b = number%10;
        if(b == 0) return string(decialNumber[a].number);
        return string(decialNumber[a].number) + "-" + string(basicNumbers[number%10].number);
    }

    return string(basicNumbers[number].number);
}

int calcDigitalLength(int number)
{
    if(number < 9999 && number >=1000)
    {
        int a = number/1000;
        int b = number%1000;
        int connectorLength = 0;
        if(b/100 == 0) connectorLength = 3;
        return basicNumbers[a].length + lecimal[1].length + connectorLength +  calcDigitalLength(number%1000);
    }
    
    if(number < 999 && number >= 100)
    {
        int a = number/100;
        if(number == 100) return basicNumbers[a].length + lecimal[0].length;
        return basicNumbers[a].length + lecimal[0].length + 3 +  calcDigitalLength(number%100);
    }

    if(number <= 99 && number >= 20)
    {
        int a = number/10;
        int b = number%10;
        if(b == 0) return decialNumber[a].length;
        return decialNumber[a].length + basicNumbers[number%10].length;
    }

    return basicNumbers[number].length;
}

int main()
{
    // int number = 8108;
    // cout<<number2english(number).c_str()<<endl;
    // cout<<calcDigitalLength(number)<<endl;
    

    int sum = 0;
    for(int i=1; i <= 1000; ++i)
    {
        sum += calcDigitalLength(i);
    }

    cout<<"result = "<<sum<<endl;
}

