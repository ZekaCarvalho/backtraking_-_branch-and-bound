from util import *

'''
Função com interface para resolução do problema N-Rainhas, esta função inicializa o
tabuleiro e chama uma função auxiliar que será chamada recursivamente.
Retorna False, caso não haja uma solução possível.
'''
def rainhas(n):
    #Cria e popula com 0 um tabuleiro NxN
    tabuleiro = [[0 for i in range(n)] for j in range(n)]

    return rainhas_aux(tabuleiro, n, 0, 0)    


'''
Função auxiliar para resolução do problema N-Rainhas
'''
def rainhas_aux(tabuleiro, n, k, contador):
    
    #CHECAR SE HÁ SOLUÇÃO. Nesse caso, como as rainhas são posicionadas iterativamente em cada coluna, 
    #se o tamanho da solução for igual ao número de colunas temos que uma solução foi encontrada.
    if (k >= n):
        # PROCESSAR SOLUCAO. Incrementar o contador.
        imprimeTabuleiro(tabuleiro)
        return contador + 1
    
    #COMPUTAR S, o conjunto de candidatos para expandir o subproblema
    for i in range(n):
        #expandir solução
        if posicaoSegura(tabuleiro, n, i, k):
            tabuleiro[i][k] = 8     
            #atualizar o contador, caso uma solução tenha sido encontrada
            contador = rainhas_aux(tabuleiro, n, k + 1, contador)
            #caso contrário, descarta o movimento. Ou seja, backtrack.
            tabuleiro[i][k] = 0    
    return contador




print("Foram encontradas {} solucoes.".format(rainhas(4)))
