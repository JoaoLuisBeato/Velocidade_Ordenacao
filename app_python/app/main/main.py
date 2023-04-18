import requests

vetor = [4, 2, 1, 5, 3, 10, 44, 7, 13, 64, 99, 21, 45]
print(vetor)
response = requests.post('http://172.17.0.3:80/sort', json={'array': vetor})

vetor = response.json().get('array_sort')
tempo = response.json().get('tempo_execucao')

print(vetor)
print('Tempo de execução: %.4f' %tempo)