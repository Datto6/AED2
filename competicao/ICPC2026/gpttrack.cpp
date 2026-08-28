#include <iostream>
#include <string>
using namespace std;

string M, N;
int stars = 0;

string solve() {
    // Find a remaining *
    for (int i = 0; i < M.size(); i++) {
        if (M[i] == '*') {

            M[i] = '0';
            string ans = solve();

            if (ans != "")
                return ans;

            M[i] = '1';
            ans = solve();

            if (ans != "")
                return ans;

            M[i] = '*';

            return "";
        }
    }

    // No * left in M, so check N
    for (int i = 0; i < N.size(); i++) {
        if (N[i] == '*') {

            N[i] = '0';
            string ans = solve();

            if (ans != "")
                return ans;

            N[i] = '1';
            ans = solve();

            if (ans != "")
                return ans;

            N[i] = '*';

            return "";
        }
    }

    // No * left anywhere
    int divisor = 0;

    for (char c : N)
        divisor = divisor * 2 + (c - '0');

    int remainder = 0;

    for (char c : M)
        remainder = (remainder * 2 + (c - '0')) % divisor;

    if (remainder == 0)
        return M;

    return "";
}

int main() {
    cin >> M;
    cin >> N;

    for (char c : M)
        if (c == '*')
            stars++;

    for (char c : N)
        if (c == '*')
            stars++;

    string answer = solve();

    cout << answer << '\n';

    return 0;
}