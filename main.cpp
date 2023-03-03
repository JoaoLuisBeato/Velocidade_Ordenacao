#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;

double normal_search(int vetor[], int size, int num_search){ 
    
    int check = 0;
    auto start = steady_clock::now();
        
        for(int i = 0; i < size; i++){
            if(vetor[i] == num_search){
                check = 1;
            }
        }

        if(check == 1){
            cout << "\n\nO numero buscado existe" << endl;
        }else{
            cout << "\n\nO numero buscado nao existe" << endl;
        }
        //cout << "\n\n==========================\n";
    
    auto end = steady_clock::now();
    duration<double, std::micro> time = end - start;
    double tempo = time.count();
    return tempo;
}

int main(){

    cout << "Hello, world!" << endl;

    return 0;
}