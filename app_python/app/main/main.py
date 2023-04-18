import requests
import numpy as np

vetor = [4, 2, 1, 5, 3, 10, 44, 7, 13, 64, 99, 21, 45]


Lista = []
def Message():
    opcao = 0
    print("Digite a opcao:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Quick Sort")
    print("4. Binery Search")
    print("5. Normal Search")
    print("6. Fill Array")
    print("0. Exit")
    opcao = int (input("Opção selecionada: "))
    return opcao
       
def Sort(vetor):
    response = requests.post('http://172.17.0.3:80/Sort', json={'array': vetor})
    vetor = response.json().get('array_sort')
    tempo = response.json().get('tempo_execucao')
    return tempo

    
def insertion_sort(vetor):
    response = requests.post('http://172.17.0.3:80/insertionSort', json={'array': vetor})
    vetor = response.json().get('array_sort')
    tempo = response.json().get('tempo_execucao')
    return tempo
    
def quick_sort(vetor):
    response = requests.post('http://172.17.0.3:80/quickSort', json={'array': vetor})
    vetor = response.json().get('array_sort')
    tempo = response.json().get('tempo_execucao')
    return tempo

def binarySearch(vetor,numero):
    response = requests.post('http://172.17.0.3:80/quickSort', json={'array': vetor, 'number_search': numero})
    vetor = response.json().get('array_sort')
    tempo = response.json().get('tempo_execucao')
    return tempo

def normal_search(vetor,numero):
    response = requests.post('http://172.17.0.3:80/quickSort', json={'array': vetor, 'number_search': numero})
    vetor = response.json().get('array_sort')
    tempo = response.json().get('tempo_execucao')
    return tempo



def switch(opcao,array):
    if opcao == 1:
        tempo = Sort(array)
        tabela = np.array([('Bubble', size, tempo)],
        dtype=[('Sort', (np.str_, 10)), ('Size', np.int32), ('Tempo', np.float64)])
        Lista.append(tabela)
        
    if opcao == 2:
        tempo = insertion_sort(size, array)
        tabela = np.array([('Insertion Sort', size, tempo)],
        dtype=[('Sort', (np.str_, 10)), ('Size', np.int32), ('Tempo', np.float64)])
        Lista.append(tabela)
        
    if opcao == 3:
        tempo = quick_sort(size, array)
        tabela = np.array([('Quick Sort', size, tempo)],
        dtype=[('Sort', (np.str_, 10)), ('Size', np.int32), ('Tempo', np.float64)])
        Lista.append(tabela)
        

    if opcao == 4:
        print ("\n\n==========================\n")
        num_search = int(input("Qual numero deseja procurar?: "))

        tempo = binarySearch(array, num_search, 0, size-1)
        tabela = np.array([('Binary Search', size, tempo)],
        dtype=[('Sort', (np.str_, 10)), ('Size', np.int32), ('Tempo', np.float64)])
        Lista.append(tabela)
          
    if opcao == 5:
        print ("\n\n==========================\n")
        num_search = int(input("Qual numero deseja procurar?: "))

        tempo = normal_search(array, size, num_search)
        tabela = np.array([('Normal Search', size, tempo)],
        dtype=[('Sort', (np.str_, 10)), ('Size', np.int32), ('Tempo', np.float64)])
        Lista.append(tabela)
        
        
while True:
    size = input("Digite o tamanho do array: ")
    while True:
        opcao = Message()
        switch(opcao)
        if(opcao!=0):
            break
    opcao = int (input("1. Desenha criar um novo array?\n 0. Sair\n"))
    if(opcao == 0):
        break
        