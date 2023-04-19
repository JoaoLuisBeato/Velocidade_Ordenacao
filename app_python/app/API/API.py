from flask import Flask, jsonify, request 
import time

app = Flask(__name__)

#página incial da aplicação web que não tem nenhuma funcionalidade 
@app.route('/')
def homepage():
    return '<h1>Home Page<h1>'

#endereço /sort que realiza a ordenação do array com a biblioteca padrão do pyhton
#Recebe as requisições pelo método POST
@app.route('/sort', methods=['POST'])
def sort():
    #Biblioteca time marca o tempo que levar pra realizar
    # a ordenção do array, começa com o tempo inicial
    # subtrai o tempo final do tempo inicial

    tempo_inicial = time.time()

    #Recebe um JSON da aplicação, por onde é mandado o array a ser ordenaddo
    # e atribui a variavel vetor dando um get no JSON atráves da 'array'
    vetor = request.json.get('array')
    vetor.sort()


    tempo_final = time.time()
    tempo_de_execucao = tempo_final - tempo_inicial
    
    #Retorna para aplicação um JSON contendo o vetor ordenado
    #e tempo de excução da função
    return jsonify({'array_sort': vetor, 'tempo_execucao': tempo_de_execucao})


#endereço /quickSort que realiza a ordenação do array utilizando o algoritmo QuickSort 
#Recebe as requisições pelo método POST
@app.route('/quickSort', methods=['POST'])
def quickSort():
    #Biblioteca time marca o tempo que levar pra realizar
    # a ordenção do array, começa com o tempo inicial 
    # subtrai o tempo final do tempo inicial
    tempo_inicial = time.time()

    #Recebe um JSON da aplicação, por onde é mandado o array a ser ordenaddo
    # e atribui a variavel vetor dando um get no JSON atráves da 'array'
    vetor = request.json.get('array')

    #chama a função interna de ordenação do QuickSort
    quickSortHelper(vetor,0,len(vetor)-1)

    tempo_final = time.time()
    tempo_de_execucao = tempo_final - tempo_inicial

    #Retorna para aplicação um JSON contendo o vetor ordenado
    #e tempo de excução da função
    return jsonify({'array_sort': vetor, 'tempo_execucao': tempo_de_execucao})

#funcão auxiliar de ordenação - QuickSort
#==========================================#
def quickSortHelper(alist,first,last):
    if first<last:
       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark
#==========================================#

#endereço /insertionSort que realiza a ordenação do array utilizando o algoritmo InsertionSort 
#Recebe as requisições pelo método POST
@app.route('/insertionSort', methods=['POST'])
def pre_insertion_sort():
    #Biblioteca time marca o tempo que levar pra realizar
    # a ordenção do array, começa com o tempo inicial  
    # subtrai o tempo final do tempo inicial
    tempo_inicial = time.time()

    #Recebe um JSON da aplicação, por onde é mandado o array a ser ordenaddo
    # e atribui a variavel vetor dando um get no JSON atráves da 'array'
    vetor = request.json.get('array')

    #Chama a função interna de insertion Sort
    vetor = insertionSort(vetor)

    tempo_final = time.time()
    tempo_de_execucao = tempo_final - tempo_inicial
    #Retorna para aplicação um JSON contendo o vetor ordenado
    #e tempo de excução da função
    return jsonify({'array_sort': vetor, 'tempo_execucao': tempo_de_execucao})

#funcão auxiliar de ordenação - QuickSort
#==========================================#
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    return array
#==========================================#

#endereço /normalSearch que realiza a busca de um número no array utilizando busca sequencial
#Recebe as requisições pelo método POST
@app.route('/normalSearch', methods = ['POST'])
def normalSearch():
    #Biblioteca time marca o tempo que levar pra realizar
    # a ordenção do array, começa com o tempo inicial  
    # subtrai o tempo final do tempo inicial
    tempo_inicial = time.time()

    #Recebe um JSON da aplicação, por onde é mandado o array a ser ordenaddo
    # e atribui a variavel vetor dando um get no JSON atráves da 'array'
    vetor = request.json.get('array')

    #Recebe através desse JSON o número a ser procurado
    size = len(vetor)
    numsearch = request.json.get('number_search')

    check = 0

    for step in range(size):
        if (vetor[step] == numsearch):
            check = 1

    tempo_final = time.time()
    tempo_de_execucao = tempo_final - tempo_inicial

    #Retorna para aplicação um JSON a string se o numero foi encontrado
    #e tempo de excução da função
    if check == 1:
        return jsonify({'resposta': "O numero existe", 'tempo_execucao': tempo_de_execucao})

    else: 
        return jsonify({'resposta': "O numero nao existe", 'tempo_execucao': tempo_de_execucao})


#endereço /bianrySearch que realiza a busca de um número no array utilizando busca sequencial
#Recebe as requisições pelo método POST
@app.route('/binarySearch', methods = ['POST'])
def binarySearch():
    #Biblioteca time marca o tempo que levar pra realizar
    # a ordenção do array, começa com o tempo inicial  
    # subtrai o tempo final do tempo inicial
    tempo_inicial = time.time()

    #Recebe um JSON da aplicação, por onde é mandado o array a ser ordenado
    # e atribui a variavel vetor dando um get no JSON atráves da 'array'
    # recebe também o número que será buscado
    vetor = request.json.get('array')
    numsearch = request.json.get('number_search')   

    #Executa a função de busca binária do array
    #===================================================#
    low = 0
    high = len(vetor)
    
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if (vetor[mid] == numsearch):
            tempo_final = time.time()
            tempo_de_execucao = tempo_final - tempo_inicial
            return jsonify({'resposta': "O numero existe", 'tempo_execucao': tempo_de_execucao})

        if (vetor[mid] < numsearch):
            low = mid + 1

        else:
            high = mid - 1
    #===================================================#
    tempo_final = time.time()
    tempo_de_execucao = tempo_final - tempo_inicial

    #Retorna para aplicação um JSON a string se o numero foi encontrado
    #e tempo de excução da função
    return jsonify({'resposta': "O numero nao existe", 'tempo_execucao': tempo_de_execucao})


app.run(host='0.0.0.0', port=80)
#Parâmetros inicial para geração da aplicação Flask, determinando a porta e a rota