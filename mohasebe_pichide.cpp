//https://quera.org/problemset/279//

#include <iostream>
#include <math.h>
using namespace std;

int main(){
    int n;
    int x;
    int y;
    int ans;
    int factorials[11] = {1,1,2,6, 24, 120, 720, 5040, 40320, 362880, 3628800};

    cin >> y >> x >> n;
    for (int i = 0; i <= n; i++) {
        ans += (factorials[n] / factorials[n - i] / factorials[i]) * pow(x, i) * pow(y, n - i);
    }
    cout << ans;
    return 0;
}