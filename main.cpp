#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

double binarySearch(int arr[], int x, int l, int r) {
    //- comeca
    auto start = steady_clock::now();
    while (l <= r) {
        
        int m = l + (r - l) / 2;
 
        if (arr[m] == x){
            // --> acha termina de contar
            cout << "\n\nO numero buscado existe" << endl;
            auto end = steady_clock::now();
            duration<double, std::micro> time = end - start;
            double tempo = time.count();
            return tempo;
        }
 
        if (arr[m] < x){
            l = m + 1;
        }

        else{
            r = m - 1;
        }
    }
    cout << "\n\nO numero buscado nao existe" << endl;

    auto end = steady_clock::now();
    duration<double, std::micro> time = end - start;
    double tempo = time.count();
    return tempo;
    //return -1;
}

int main(){

    cout << "Hello, world!" << endl;

    return 0;
}