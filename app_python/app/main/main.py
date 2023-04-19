import requests
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
    print("4. Binery Search")
    print("5. Normal Search")
    print("6. Fill Array")
    print("0. Exit")
    print("==============================")
    opcao = int(input("Opção selecionada: "))
    return opcao
       
def Sort(vetor):

    response = requests.post('http://172.17.0.2:80/sort', json={'array': vetor})
    vetor = response.json().get('array_sort')
    tempo = response.json().get('tempo_execucao')
    return tempo

    
def insertion_sort(vetor):
    response = requests.post('http://172.17.0.2:80/insertionSort', json={'array': vetor})
    vetor = response.json().get('array_sort')
    tempo = response.json().get('tempo_execucao')
    return tempo
    
def quick_sort(vetor):
    response = requests.post('http://172.17.0.2:80/quickSort', json={'array': vetor})
    vetor = response.json().get('array_sort')
    tempo = response.json().get('tempo_execucao')
    return tempo

def binary_search(vetor,numero):
    response = requests.post('http://172.17.0.2:80/binarySearch', json={'array': vetor, 'number_search': numero})
    resposta = response.json().get('resposta')
    print(resposta + "\n")
    tempo = response.json().get('tempo_execucao')
    return tempo

def normal_search(vetor,numero):
    response = requests.post('http://172.17.0.2:80/normalSearch', json={'array': vetor, 'number_search': numero})
    resposta = response.json().get('resposta')
    print(resposta + "\n")
    tempo = response.json().get('tempo_execucao')
    return tempo

def fill_array(array,n):
    for i in range(n):
        array.append(random.randint(1, 2000000))
    return array


posicao_tabela = 0 

while True:
    print('**********************************')
    size = int(input("Digite o tamanho do array: "))

    array = []
    array = fill_array(array, size)
    #print(array)
   

    while True:
        opcao = Message()
        if(opcao==0):
            break
        
        match opcao:
            case 1:
                tempo = Sort(array)
                tabela = "\tPython Sort " + "\tTamanho: " + str(size) + "\tTempo: " + str(tempo)
                Lista.append(tabela)

            case 2:
                tempo = insertion_sort(array)
                tabela = "\tInsertion Sort " + "\tTamanho: " + str(size) + "\tTempo: " + str(tempo)
                Lista.append(tabela)   

            case 3:
                tempo = quick_sort(array)
                tabela = "\tQuick Sort " + "\tTamanho: " + str(size) + "\tTempo: " + str(tempo)
                Lista.append(tabela)
                
            case 4:
                print ("\n\n==========================\n")
                num_search = int(input("Qual numero deseja procurar?: "))
                tempo = binary_search(array, num_search)
                tabela = "\tBinary Search " + "\tTamanho: " + str(size) + "\tTempo: " + str(tempo)
                Lista.append(tabela)
            
            case 5:
                print ("\n\n==========================\n")
                num_search = int(input("Qual numero deseja procurar?: "))

                tempo = normal_search(array, num_search)
                tabela = "\tNormal Search " + "\tTamanho: " + str(size) + "\tTempo: " + str(tempo)
                Lista.append(tabela)
            
            case 6:
                array = fill_array(array,size)
                     
        print('\nTempo de execução: %.6f' %tempo)
        posicao_tabela += 1

    print('\n**********************************\n')
    opcao = int (input("\n--> 1. Desenha criar um novo array?\n--> 0. Sair\n\n-->"))
    if(opcao == 0):
        break

print('\n\n')

print(*Lista, sep = "\n")

print('\n\n')

        