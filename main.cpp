#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;


int split(int vetor[], int low, int high){

    int pivot = vetor[high];
    int i = (low - 1);

    for(int j = low; j <= high - 1; j++){
        if(vetor[j] < pivot){
            i++;
            swap(vetor[i], vetor[j]);
        }
    } 

    swap(vetor[i + 1], vetor[high]);
    return (i + 1);
}

double quick_sort(int vetor[], int low, int high){

    auto start = steady_clock::now();

    if(low < high){

        int half = split(vetor, low, high);
        
        quick_sort(vetor, low, half - 1);
        quick_sort(vetor, half + 1, high);
        
    }

    auto end = steady_clock::now();
    duration<double, std::micro> time = end - start;
    
    double tempo = time.count();
    return tempo;
    
void print_time (double time){
    if(time >= 1000 && time < 1000000){
        //micro -> milli
        time = time/1000.0; // ->milli
        cout << "\n\nTempo percorrido: " << time << " milisegundos";
    }
    else if(time >= 1000000){
        //micro -> seconds
        time = time/1000000.0; //-> seconds
        cout << "\n\nTempo percorrido: " << time << " segundos";

    }
    else{
        cout << "\n\nTempo percorrido: " << time << " microsegundos";
    }
    
}

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