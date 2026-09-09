#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    cin.tie(0)->sync_with_stdio(0);
    string str = "";
    cin >> str;
    int slen = str.length();
    for(int i = 0; i < slen; i++){
        if(str[i] >= 65 && str[i] <= 90){
            str[i] = str[i] + 32;
        }
        else{
            str[i] = str[i] - 32;
        }
    }
    cout << str;
    return 0;
}