from flask import Flask, jsonify, request 
import time

app = Flask(__name__)

@app.route('/')
def homepage():
    return '<h1>Home Page<h1>'

@app.route('/sort', methods=['POST'])
def sort():
    tempo_inicial = time.time()
    vetor = request.json.get('array')
    vetor.sort()


    tempo_final = time.time()
    tempo_de_execucao = tempo_final - tempo_inicial
    
    return jsonify({'array_sort': vetor, 'tempo_execucao': tempo_de_execucao})


@app.route('/quickSort', methods=['POST'])
def quickSort():
   
    vetor = request.json.get('array')
    tempo_inicial = time.time()
    quickSortHelper(vetor,0,len(vetor)-1)

    tempo_final = time.time()
    tempo_de_execucao = tempo_final - tempo_inicial


    return jsonify({'array_sort': vetor, 'tempo_execucao': tempo_de_execucao})

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

@app.route('/insertionSort', methods=['POST'])
def pre_insertion_sort():
    tempo_inicial = time.time()

    vetor = request.json.get('array')
    vetor = insertionSort(vetor)

    tempo_final = time.time()
    tempo_de_execucao = tempo_final - tempo_inicial
    return jsonify({'array_sort': vetor, 'tempo_execucao': tempo_de_execucao})

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

@app.route('/normalSearch', methods = ['POST'])

def normalSearch():

    tempo_inicial = time.time()
    vetor = request.json.get('array')
    size = len(vetor)
    numsearch = request.json.get('number_search')

    check = 0

    for step in range(size):
        if (vetor[step] == numsearch):
            check = 1

    tempo_final = time.time()
    tempo_de_execucao = tempo_final - tempo_inicial

    if check == 1:
        return jsonify({'resposta': "O numero existe", 'tempo_execucao': tempo_de_execucao})

    else: 
        return jsonify({'resposta': "O numero nao existe", 'tempo_execucao': tempo_de_execucao})


@app.route('/binarySearch', methods = ['POST'])

def binarySearch():

    array = request.json.get('array')
    numsearch = request.json.get('number_search')   
    low = 0
    high = len(array)
    tempo_inicial = time.time()
    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == numsearch:
            tempo_final = time.time()
            tempo_de_execucao = tempo_final - tempo_inicial
            return jsonify({'resposta': "O numero existe", 'tempo_execucao': tempo_de_execucao})

        elif array[mid] < numsearch:
            low = mid + 1

        else:
            high = mid - 1

    tempo_final = time.time()
    tempo_de_execucao = tempo_final - tempo_inicial
    return jsonify({'resposta': "O numero nao existe", 'tempo_execucao': tempo_de_execucao})

app.run(host='0.0.0.0', port=80)