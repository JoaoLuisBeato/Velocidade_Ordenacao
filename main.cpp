#include <iostream>
#include <chrono>

using namespace std;
using namespace std::chrono;


void fill_array(int size, int vetor[]){

    for(int i = 0; i < size; i++)
        vetor[i] = 20 + (rand() % 1999981);

double bubble_sort(int size, int vetor[]){

    auto start = steady_clock::now();

    for(int i = 0; i < size; i++)
        for(int j = 0; j < size - i; j++)
            if(vetor[j] > vetor[j + 1])
                swap(vetor[j], vetor[j + 1]);

    auto end = steady_clock::now();
    duration<double, std::micro> time = end - start;

    double tempo = time.count();
    return tempo;

}

double insertion_sort(int size, int vetor[]) {

    auto start = steady_clock::now();

    for (int i = 1; i < size; i++) {
        int escolhido = vetor[i];
        int j = i - 1;
        
        while ((j >= 0) && (vetor[j] > escolhido)) {
            vetor[j + 1] = vetor[j];
            j--;
        }
        vetor[j + 1] = escolhido;
    }

    auto end = steady_clock::now();
    duration<double, std::micro> time = end - start;
    
    double tempo = time.count();
    return tempo;
}

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
}
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
}
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

void print_array(int size, int vetor[]){
    for(int i = 0; i < size; i++){
        cout << vetor[i] << " ";
    }
}

int main(){
    
    int size, opcao, num_search;
    double tempo;

    cout << "Digite o tamanho do array: ";
    cin >> size;
    
    int* array = new int[size];
    for (int i=0; i<size; i++)
        array[i] = 0;
    
    do{
        opcao = Message();
        switch (opcao){
            case 1:
                tempo = bubble_sort(size, array);
                print_array(size, array);
                cout << "\n\nTempo micro: " << tempo << endl;
                print_time(tempo);
                break;

            case 2:
                tempo = insertion_sort(size, array);
                print_array(size, array);
                print_time(tempo);
                break;

            case 3:
                tempo = quick_sort(array, 0, size - 1);
                print_array(size, array);
                print_time(tempo);
                break;

            case 4: //Binary Search
                cout << "\n\n==========================\n";
                cout << "Qual numero deseja procurar?: ";
                cin >> num_search;
                tempo = binarySearch(array, num_search, 0, size-1);
                print_time(tempo);
                break;

            case 5: //Normal search
                cout << "\n\n==========================\n";
                cout << "Qual numero deseja procurar?: ";
                cin >> num_search;
                tempo = normal_search(array, size-1, num_search);
                print_time(tempo);
                break;
                
            case 6:
                fill_array(size, array);
                print_array(size, array);
                break;
                
            case 0:
                break;
                
            default:
                break;
        }
            
    }while(opcao != 0);
    return 0;
}