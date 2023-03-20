#include <iostream>
#include <chrono>
#include <random>
#include <string.h>

using namespace std;
using namespace std::chrono;

// Modulo com os principais atributos para completar a tabela.

typedef struct modulo {
   char sort[20];
   int size;
   double tempo_execucao;
}modulo;

// a funçao bubble_sort ela é um dos metodos de ordenaçao, sua principal funçao é o swap, a complexidade dele é n ao quadrado.

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

// o insertion_sort é o segundo metodo de oredenaçao do programa, ele funciona fazendo comparaçoes com o anterior para ordenar o array, 
//tambem tem a complexidade de n ao quadrado.

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

// funçao complementar do quick_sort ela divide o vetor ao meio.

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

// funcao quick_sort é a terceira ordenaçao, ele usa a funçao split para escolher o pivot e a esquerda dele estao os numeros menor que
// o pivot e a direita estao os maiores, fazendo isso ate o arry estar ordenado, sua complexidade é log(n).

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

// a funçao normal_search é a primeira busca do programa, ela é uma busca linear, anda o array inteiro ate achar o numero desejado, 
//a complexidade é n.

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
    auto end = steady_clock::now();
    duration<double, std::micro> time = end - start;
    double tempo = time.count();
    return tempo;
}

// a funçao binarySearch é a segunda busca do programa e a mais efeciente, ela realiza busca por divisoes sucessivas do array,
//a complexidade é Log (n).

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

// funçao que retorna o print do menu do programa.

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

// funçao que imprimi o array com todos os numeros random.

void print_array(int size, int vetor[]){

    cout << "\n\n" << endl;

    for(int i = 0; i < size; i++){
        cout << vetor[i] << " ";
    }
    cout << "\n" << endl;
}

// funçao que imprimi o tempo que demorou a execuçao, dependendo do tempo ele imprimi em milisegundos, segundos ou microsegundo.

void print_time (double time){
    if(time >= 1000 && time < 1000000){
        //micro -> milli
        time = time/1000.0; // ->milli
        cout << "|\tTempo percorrido: " << time << " milisegundos\t|";
    }
    else if(time >= 1000000){
        //micro -> seconds
        time = time/1000000.0; //-> seconds
        cout << "|\tTempo percorrido: " << time << " segundos\t|";

    }
    else{
        cout << "|\tTempo percorrido: " << time << " microsegundos\t|";
    }
}

// funçao que cria os numeros random dependendo do tamanho que o usuario pedir.

void fill_array(int size, int vetor[]){

    random_device random;
    default_random_engine engine {random()};
    uniform_int_distribution<> dist{20, 2000001};


    for(int i = 0; i < size; i++)
        vetor[i] = dist(engine);
}

// imprimi a tabela de acordo com as funçoes executadas.

void printar_tabela(modulo sorts[20], int size){
    for(int i = 0; i < size; i++){
       cout << "|\tSort: " << sorts[i].sort << "\t|\tSize: " << sorts[i].size << "\t";
       print_time(sorts[i].tempo_execucao);
       cout << endl;
    }
}

int main(){

    int size, opcao, num_search, posicao = 0, Max_print = 100000;
    double tempo;
    modulo tabela[20];

    do{
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
                    tabela[posicao].size = size;
                    strcpy(tabela[posicao].sort, "Bubble Sort");
                    tabela[posicao].tempo_execucao = tempo;
                    if(size <= Max_print)
                        print_array(size, array);

                    print_time(tempo);

                    if(posicao<20)
                        posicao++;
                    break;

                case 2:
                    tempo = insertion_sort(size, array);
                    tabela[posicao].size = size;
                    strcpy(tabela[posicao].sort, "Insertion Sort");
                    tabela[posicao].tempo_execucao = tempo;
                    if(size <= Max_print)
                        print_array(size, array);
                    print_time(tempo);
                    if(posicao<20)
                        posicao++;
                    break;

                case 3:
                    tempo = quick_sort(array, 0, size - 1);
                    tabela[posicao].size = size;
                    strcpy(tabela[posicao].sort, "Quick Sort");
                    tabela[posicao].tempo_execucao = tempo;
                    if(size <= Max_print)
                        print_array(size, array);
                    print_time(tempo);
                    if(posicao<20)
                        posicao++;
                    break;

                case 4: //Binary Search
                    cout << "\n\n==========================\n";
                    cout << "Qual numero deseja procurar?: ";
                    cin >> num_search;
                    tempo = binarySearch(array, num_search, 0, size-1);
                    tabela[posicao].size = size;
                    strcpy(tabela[posicao].sort, "Binary Search");
                    tabela[posicao].tempo_execucao = tempo;
                    print_time(tempo);
                    if(posicao<20)
                        posicao++;
                    break;

                case 5: //Normal search
                    cout << "\n\n==========================\n";
                    cout << "Qual numero deseja procurar?: ";
                    cin >> num_search;
                    tempo = normal_search(array, size, num_search);
                    tabela[posicao].size = size;
                    strcpy(tabela[posicao].sort, "Norma Search");
                    tabela[posicao].tempo_execucao = tempo;
                    print_time(tempo);
                    if(posicao<20)
                        posicao++;
                    break;

                case 6:
                    fill_array(size, array);
                    if(size <= Max_print)
                        print_array(size, array);

                    break;

                default:
                    break;
            }

        }while(opcao != 0);

        delete[] array;
        cout << "\n 1. Deseja criar um novo array" << endl;
        cout << " 0. Encerrar programa" <<endl;
        cout << "--> ";
        cin >> opcao;
        cout << "\n\n";

    }while(opcao == 1);
    cout << "=========================================================================================================\n";
    printar_tabela(tabela,posicao);
    cout << "=========================================================================================================\n";
    return 0;
}
