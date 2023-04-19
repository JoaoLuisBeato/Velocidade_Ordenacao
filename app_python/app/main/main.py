import requests                 ##  Bibliotecas para chamada da api e randomizaçao do vetor
import random


Lista = []
tabela = []

def Message():
    opcao = 0
    print("===============================")
    print("Digite a opcao:")
    print("1. Python Sort")
    print("2. Insertion Sort")
    print("3. Quick Sort")
    print("4. Binery Search")                       ##  Funçao chamada para print do menu, feita na propria
    print("5. Normal Search")                       ##  main, ja que a API foi utilizada para desenvolver os sistemas
    print("6. Fill Array")                          ##  de ordenação
    print("0. Exit")
    print("==============================")
    opcao = int(input("Opção selecionada: "))
    return opcao
       
def Sort(vetor):

    response = requests.post('http://172.17.0.2:80/sort', json={'array': vetor})        ##  Referencia para API utilizar o /sort com o @app.route
    vetor = response.json().get('array_sort')                                           ##  Resposta do vetor que veio da API
    tempo = response.json().get('tempo_execucao')                                       ##  Tempo de execucao do Sort da API
    return tempo

    
def insertion_sort(vetor):
    response = requests.post('http://172.17.0.2:80/insertionSort', json={'array': vetor})       ##  Referencia para API utilizar o /insertionSort com o @app.route
    vetor = response.json().get('array_sort')                                                   ##  Resposta do vetor ordenado que veio da API
    tempo = response.json().get('tempo_execucao')                                               ##  Tempo de execucao do Insertion Sort da API
    return tempo
    
def quick_sort(vetor):
    response = requests.post('http://172.17.0.2:80/quickSort', json={'array': vetor})           ##  Referencia para API utilizar o /quickSort com o @app.route
    vetor = response.json().get('array_sort')                                                   ##  Resposta do vetor ordenado que veio da API
    tempo = response.json().get('tempo_execucao')                                               ##  Tempo de execucao do Quick Sort da API
    return tempo

def binary_search(vetor,numero):
    response = requests.post('http://172.17.0.2:80/binarySearch', json={'array': vetor, 'number_search': numero})           ##  Referencia para API utilizar o /binarySearch com o @app.route        
    resposta = response.json().get('resposta')                                                                              ##  Resposta da API se caso o número foi encontrado ou não
    print(resposta + "\n")                                                                                                  ##  Print da resposta ^^^^^^
    tempo = response.json().get('tempo_execucao')                                                                           ##  Tempo de execucao do Binary Search da API
    return tempo

def normal_search(vetor,numero):
    response = requests.post('http://172.17.0.2:80/normalSearch', json={'array': vetor, 'number_search': numero})           ##  Referencia para API utilizar o /normalSearch com o @app.route
    resposta = response.json().get('resposta')                                                                              ##  Resposta da API se caso o número foi encontrado ou não
    print(resposta + "\n")                                                                                                  ##  Print da resposta ^^^^^^
    tempo = response.json().get('tempo_execucao')                                                                           ##  Tempo de execucao do Normal Search da API  
    return tempo

def fill_array(array,n):                                                                                                    ##   Função para encher o array com numeros aleatórios de 1 a 2000000
    for i in range(n):          
        array.append(random.randint(1, 2000000))                                                                            ##   Gera numero aleatório pela biblioteca random e insere no array                                                                            
    return array


posicao_tabela = 0 

while True:
    print('**********************************')
    size = int(input("Digite o tamanho do array: "))                                                                        ##  size armazena o tamanho do array, utilizado no fill_array()

    array = []                                                                                                              ##  Criação do array principal
    array = fill_array(array, size)                                                                                         ##  Chamada do fill_array()
    #print(array)
   

    while True:
        opcao = Message()                                                                                                   ##  Chamada da função message() para printar o menu
        if(opcao==0):                                                                                                       
            break
        
        match opcao:                                                                                                        ##  Match-Case == Switch Case para ver qual API será chamada
            case 1:
                tempo = Sort(array)                                                                                         ##  Caso 1: Chamada do Sort nativo do Python
                tabela = "\tPython Sort " + "\tTamanho: " + str(size) + "\tTempo: " + str(tempo)                            ##  Print do tipo de sort, size do array e tempo levado pelo sort na API
                Lista.append(tabela)                                                                                        ##  Atribuição dos resultados da execução para uma lista/relatório de chamadas

            case 2:
                tempo = insertion_sort(array)                                                                               ##  Caso 2: Chamada da funçao que faz o pedido do Insertion Sort na API
                tabela = "\tInsertion Sort " + "\tTamanho: " + str(size) + "\tTempo: " + str(tempo)                         ##  Print do tipo de sort, size do array e tempo levado pelo sort na API
                Lista.append(tabela)                                                                                        ##  Atribuição dos resultados da execução para uma lista/relatório de chamadas  

            case 3:
                tempo = quick_sort(array)                                                                                   ##  Caso 3: Chamada da funçao que faz o pedido do Quick Sort na API
                tabela = "\tQuick Sort " + "\tTamanho: " + str(size) + "\tTempo: " + str(tempo)                             ##  Print do tipo de sort, size do array e tempo levado pelo sort na API
                Lista.append(tabela)                                                                                        ##  Atribuição dos resultados da execução para uma lista/relatório de chamadas
                
            case 4:
                print ("\n\n==========================\n")
                num_search = int(input("Qual numero deseja procurar?: "))                                                   ##  Input do número a ser buscado
                tempo = binary_search(array, num_search)                                                                    ##  Caso 4: Chamada da funçao que faz o pedido do Binary Search na API
                tabela = "\tBinary Search " + "\tTamanho: " + str(size) + "\tTempo: " + str(tempo)                          ##  Print do tipo de sort, size do array e tempo levado pelo sort na API
                Lista.append(tabela)                                                                                        ##  Atribuição dos resultados da execução para uma lista/relatório de chamadas
            
            case 5:
                print ("\n\n==========================\n")
                num_search = int(input("Qual numero deseja procurar?: "))                                                   ##  Input do número a ser buscado
                tempo = normal_search(array, num_search)                                                                    ##  Caso 5: Chamada da funçao que faz o pedido do Normal Search na API
                tabela = "\tNormal Search " + "\tTamanho: " + str(size) + "\tTempo: " + str(tempo)                          ##  Print do tipo de sort, size do array e tempo levado pelo sort na API
                Lista.append(tabela)                                                                                        ##  Atribuição dos resultados da execução para uma lista/relatório de chamadas
            
            case 6:
                array = fill_array(array,size)                                                                              ##  Caso 6: Preenchimento de valores aleatórios do array conforme o size dado
                     
        print('\nTempo de execução: %.6f' %tempo)                                                                           ##  Print do tempo de execução da API atual selecionada
        posicao_tabela += 1

    print('\n**********************************\n')
    opcao = int (input("\n--> 1. Desenha criar um novo array?\n--> 0. Sair\n\n-->"))                                        ##  Input caso queira continuar no programa ou não
    if(opcao == 0):
        break

print('\n\n')

print(*Lista, sep = "\n")                                                                                                   ##  Print da tabela/lista/relatório de todos os sorts feitos na sessão

print('\n\n')

        