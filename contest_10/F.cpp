#pragma GCC optimize("O3", "unroll-loops")

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n = 1e7;
    vector<int> p(n);
    for (int i = 0; i < n; i++) p[i] = i;
    random_shuffle(p.begin(), p.end());
    for (int i = 0; i < n; i++) cout << p[i] << " ";
}
