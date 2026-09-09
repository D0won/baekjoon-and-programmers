#include<bits/stdc++.h>
using namespace std;

int main(void)
{
    cin.tie(0)->sync_with_stdio(0);
    int n = 0;
    cin >> n;
    if(n % 2 == 0){
        cout << n << " is even";
    }
    else{
        cout << n << " is odd";
    }
    return 0;
}