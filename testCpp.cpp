#include <bits/stcd++.h>
using namespace std;
long a,n;
long long LT(long a, long n) {
    long p = 1;
    for int (i = 1; i <= n; i++)
        p = a * p;
    return p;
}