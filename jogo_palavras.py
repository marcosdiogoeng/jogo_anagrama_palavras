import random as rd #importa a biblioteca Random
# Marcos Diogo
n = rd.randrange(0, 5) #Cria o numero para sortear as palavras dentro do arquivo txt

with open('arquivo.txt', 'r') as arquivo: #Abre o arquivo txt como leitura
    palavra = arquivo.readlines() # lê as linhas do arquivo
    palavra = palavra[n] # armazena a palavra sorteada pelo numero n

def func_remove(x): # funcao para tratar a palavra sorteada para comparação
    palavra_sort = list(x)
    palavra_sort.remove('\n')
    return ', '.join(palavra_sort).replace(', ', '')

def normalizar_palavra(y:str) -> str: # funcao para embaralhar a palavra sorteada
    embaralha = rd.sample(y, len(y))
    embaralha.remove('\n')
    return ', '.join(embaralha).replace(', ', '')

teste = func_remove(palavra) # recebe a palavra para comparação
contador = 0 # contador para numero de tentativas
print('Vamos jogar Anagrama!!!')
mostrador = normalizar_palavra(palavra) 
# armazena a palavra para mostrar no console ja embaralhada

while True: #Loop para o jogo
    print(f'\nQual é a palavra: {mostrador}')
    resultado = input('\nDigite a sua resposta: ')
    contador += 1 # incrementa o contador para cada tentativa
    if resultado == teste: # compara o resultado digitado com a palavra sorteada
        print('\nParabens, voce acertou!!!')
        break # sai do jogo
    elif contador >= 5: # se o numero de tentativas for 5, gamer over
        print('\nGamer Over!!! \nNumero de tentativas excedidas!')
    else: # quando o usuario erra a palavra
        print('\nVoce errou!!!')