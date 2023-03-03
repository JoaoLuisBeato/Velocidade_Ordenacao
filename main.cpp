#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

int Message(){
    int opcao = 0;
    cout << "\n\n==========================\n";
    cout << "Digite a opcao" << endl;
    cout << "1. Bubble Sort " << endl;
    cout << "2. Insertion Sort " << endl;
    cout << "3. Quick Sort " << endl;
    cout << "4. Binery Search" << endl;
    cout << "5. Normal Search" << endl;
    cout << "6. Fill Array" << endl;
    cout << "0. Exit" << endl;
    cout << " --> ";
    cin >> opcao;
    cout << "==========================\n";
    return opcao;
}

int main(){

    cout << "Hello, world!" << endl;

    return 0;
}