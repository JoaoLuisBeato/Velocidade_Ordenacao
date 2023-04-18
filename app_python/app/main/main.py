import requests

vetor = [4, 2, 1, 5, 3, 10, 44, 7, 13, 64, 99, 21, 45]
print(vetor)
numero  = 44
response = requests.post('http://172.17.0.3:80/normalSearch', json={'array': vetor, 'number_search': numero})

#vetor = response.json().get('array_sort')
resposta = response.json().get('resposta')
tempo = response.json().get('tempo_execucao')

print(vetor)
print('Tempo de execução: %.4f' %tempo)
print(resposta)