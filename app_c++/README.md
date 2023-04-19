# Velocidade_Ordenacao

- Projeto organizado pelo:
André Luís Bianchini Filho,
João Luís Beato Cardoso,
Mateus José Whitaker Filipe,
Rafael Rodrigues Sato,
Yuka Sakai.
-
    Terceira Tarefa - Velocidade para ordenação e busca!



## Como excutar o código

A execução do código tem como pré-requisito o software Docker. A partir dele, deve-se baixar a pasta do projeto e descompacta-la. Após isso, abra o Terminal ou PowerShell e navegue até onde está a pasta do projeto.
Agora dentro do terminal digite os seguintes comandos:

    -> docker build . -t nome_escolhido:<versão> (recomendável 1.0)
        Ex: docker build . -t ordenacao:1.1
        
    -> docker run --rm -it nome_escolhido:<versão>
        Ex: docker run --rm -it ordenacao:1.1




## Sobre o projeto


Tendo como objetivo a potencialização e estímulo do uso de uma ferramenta de controle de versões e entregas (github ou gitlab), realizamos um projeto em equipe que consiste na construção de um código que *ordena um vetor de números, busca e calcula o seu tempo de execução para comparação*.

Primeiramente, o software requisita ao usuário um números entre 10.000 e 1.000.000, que determinará o temanho do vetor, na qual gerará uma sequência contendo números inteiros aleatórios na faixa de 20 e 2.000.000.

Após essa etapa, tem-se ao usuário a escolha das seguintes opções

* 1 Bubble Sort
* 2 Insertion Sort
* 3 Quick Sort
* 4 Binery Search
* 5 Normal Search
* 6 Fill Array
* 0 Inserir um array novo

Sendo a opção 1, 2 e 3 algoritmos de ordenação de números inteiros, 4 e 5 algoritmos de busca (na qual a primeira necessita do vetor ordenado e a segunda não), um algaritmo de preenchimento na 6 e o 0 para uma opção de inserir um array novo.

Ao escolher alguma opção de ordenação, os dados de tamanho do array, tipo de ordenação e o tempo de execução ficará salvo em uma string, que será printada como uma tabela, na qual cabe no máximo 20 tentativas de ordenação de arrays e, caso ultrapasse, a nova informação sobrescreverá a ultima para evitar uma sobrecarga. Portanto, caso não queira perder a vigézima informação, é preferível que tire o print da tabela e reinicie o programa (ou limpe a tabela) antes de rodar um array novo para ordenação.

Dessa forma, ao final de cada busca ou ordenação, é exibida ao terminal em unidades o tamanho do array, tipo de ordenação e o tempo que levou para terminar a execução em segundos, milisegundos e microssegundos.
Ao final da execução do programa, é listada uma tabela no termina com os tempos de execução de cada algoritmo
para cada vetor utilizado.
