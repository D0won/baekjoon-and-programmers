#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    cin.tie(0)->sync_with_stdio(0);
    string str = "";
    cin >> str;
    int slen = str.length();
    for(int i = 0; i < slen; i++){
        cout << str[i] << "\n";
    }
    return 0;
}