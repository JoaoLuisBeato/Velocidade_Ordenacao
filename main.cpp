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
}

int main(){

    return 0;
}