#include <iostream>
#include <string>
#include <vector>
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

void readFile(const char *file, vector<int> &vi)
{
    assert(file != NULL);
    FILE *in = NULL;
    int file_size=0;
    char *buf = NULL;

    in = fopen(file, "r");

    if(in == NULL)
    {
        return;
    }

    fseek(in, 0, SEEK_END);
    file_size = ftell(in);
    fseek(in, 0, SEEK_SET);

    buf = (char *)malloc(file_size+1);
    assert(buf != NULL);
    memset(buf, 0, file_size+1);

    fread(buf, file_size, 1, in);

    fclose(in);


    string str(buf, buf+file_size);

    size_t last=0;
    size_t index=str.find_first_of(',',last);
    while(index != string::npos)
    {
        int value = atoi(str.substr(last, index-last).c_str());
        vi.push_back(value);
        last = index + 1;
        index = str.find_first_of(',', last);
    }

    if(index-last > 0)
    {
        int value = atoi(str.substr(last, index-last).c_str());
        vi.push_back(value);
    }

    free(buf);
}

int Decode(vector<int> V, const int *Q)
{
    int len = V.size();
    for(int i=0; i < len; ++i)
    {
        V[i] ^= Q[i%3];
        if(V[i] < 32 || V[i] > 126)
        {
            return 0;
        }
    }

    int sum=0;
    for(auto i:V)
    {
        sum += i;
    }

    char *buf = (char *)malloc(50);
    for(int i=0; i < 49; ++i)
    {
        buf[i] = (char)V[i];
    }
    buf[49]='\0';

    //cout<<char(Q[0])<<char(Q[1])<<char(Q[2])<<" ";
    cout<<buf<<endl;

    free(buf);
    return sum;
}

void FindAllResult(vector<int> vi)
{
    int Q[3]={0,0,0};
    int start = 'a';
    int end = 'z'+1;
    for(int i = start; i < end; ++i)
    {
        Q[0]=i;
        for(int j = start; j < end; ++j)
        {
            Q[1]=j;
            for(int k = start; k < end; ++k)
            {
                Q[2] = k;
                Decode(vi, &Q[0]);
            }
        }
    }
}

int main()
{
    vector<int> vi;
    readFile("cipher.txt",vi);

    // int Q[]={97,97,97};
    // cout<<Decode(vi, &Q[0])<<endl;
    FindAllResult(vi);
    cout<<endl;
    return 0;
}
