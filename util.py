'''
Função de apoio para checar se há¡ rainhas atacando na posição em questão
Dado que o algoritmo popula o tabuleiro a partir da esquerda, será
necessário avaliar se há ataques pelo lado esquerdo
'''
def posicaoSegura(tabuleiro, n, linha, coluna):
 
    # Checa se há rainhas atacando pelo lado esquerdo na linha em questão
    for i in range(coluna):
        if tabuleiro[linha][i] == 8: return False
 
    # Checa se há rainhas atacando pela diagonal superior esquerda
    for i,j in zip(range(linha,-1,-1), range(coluna,-1,-1)):
        if tabuleiro[i][j] == 8: return False
 
    # Checa se há rainhas atacando pela diagonal inferior esquerda
    for i,j in zip(range(linha, n, 1), range(coluna, -1, -1)):
        if tabuleiro[i][j] == 8: return False
        
    return True
    
# Função de apoio para imprimir tabuleiro
def imprimeTabuleiro(tabuleiro):
    print('\n'.join([''.join(['{:2}'.format(item) for item in linha]) for linha in tabuleiro]), '\n')    
