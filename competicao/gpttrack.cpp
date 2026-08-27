#include <iostream>
#include <string>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using namespace boost::multiprecision;

cpp_int back(const string& M,const string& N,int i,int j,cpp_int poti,cpp_int potj,
    cpp_int numi,cpp_int numj) {
    // Base case
    if (i < 0 && j < 0) {
        if (numj != 0 && numi % numj == 0) {
            return numi;
        }
        return -1;
    }
    // Both M[i] and N[j] are '*'
    if (i >= 0 && j >= 0 && M[i] == '*' && N[j] == '*') {

        // M = 0, N = 0
        long long sol = back(M, N,i - 1, j - 1,poti * 2, potj * 2,numi, numj);
        if (sol != -1)
            return sol;
        // M = 1, N = 0
        sol = back(M, N,i - 1, j - 1,poti * 2, potj * 2,numi + poti, numj);
        if (sol != -1)
            return sol;
        // M = 0, N = 1
        sol = back(
            M, N,
            i - 1, j - 1,
            poti * 2, potj * 2,
            numi, numj + potj
        );
        if (sol != -1)
            return sol;

        // M = 1, N = 1
        return back(M, N,i - 1, j - 1,poti * 2, potj * 2,numi + poti,numj + potj);
    }

    // Only M[i] is '*'
    if (i >= 0 && M[i] == '*') {
        // M = 0
        long long sol = back(M, N,i - 1, j,poti * 2, potj,numi, numj);
        if (sol != -1){
            return sol;
        }


        // M = 1
        return back(M, N,i - 1, j,poti * 2, potj,numi + poti, numj);
    }

    // Only N[j] is '*'
    if (j >= 0 && N[j] == '*') {
        // N = 0
        long long sol = back(M, N,i, j - 1,poti, potj * 2,numi, numj);

        if (sol != -1){
            return sol;
        }
        // N = 1
        return back(M, N,i, j - 1, poti, potj * 2, numi, numj + potj);
    }

    // Neither is '*'
    if (i >= 0 && j >= 0) {

        int bitM = M[i] - '0';
        int bitN = N[j] - '0';

        return back(M, N,i - 1, j - 1,poti * 2, potj * 2,numi + bitM * poti,numj + bitN * potj);
    }

    // Only M remains
    if (i >= 0) {
        int bitM = M[i] - '0';
        return back(M, N,i - 1, j,poti * 2, potj,numi + bitM * poti,numj);
    }

    // Only N remains
    if (j >= 0) {
        int bitN = N[j] - '0';
        return back(M, N,i, j - 1,poti, potj * 2,numi,numj + bitN * potj);
    }

    return -1;
}


string binario(long long num) {
    if (num == 0)
        return "0";
    if (num == -1)
        return "-1";

    string resultado = "";

    while (num > 0) {
        int bit = num % 2;
        num /= 2;
        resultado = char('0' + bit) + resultado;
    }

    return resultado;
}


int main() {
    string M, N;

    cin >> M;
    cin >> N;

    cpp_int saida = back(M,N,M.length() - 1,N.length() - 1,1,1,0,0);

    string resultado = binario(saida);

    // Add leading zeros
    while (resultado.length() < M.length()) {
        resultado = "0" + resultado;
    }

    cout << resultado << endl;

    return 0;
}