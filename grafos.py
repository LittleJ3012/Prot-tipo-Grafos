#Observação importante: Este protótipo de Software foi desenvolvido primeiro no Google Collab, e depois realocado para o repositório GitHub.

import numpy as np
from google.colab import drive #Para fazer a conexão com os arquivos (ponte.txt, zachary.txt e exemplo.txt, que estão no meu Google Drive)

# Montando o Google Drive
drive.mount('/content/drive')

#Esta função lê o arquivo.txt (passado como parâmetro pelo usuário) e armazena o conteúdo do arquivo em uma matriz do tipo numpy.

def MatrizDeGrafos(inst): #O parâmetro é o nome do dataset(inst) 
    try:

        # Uso do condicional if para que o programa saiba o caminho de cada um dos três arquivos no Google Drive:
        if inst == "ponte":
           caminho_arquivo = "/content/drive/My Drive/ponte.txt"
        elif inst == "zachary":
           caminho_arquivo = "/content/drive/My Drive/zachary.txt"
        elif inst == "exemplo":
           caminho_arquivo = "/content/drive/My Drive/exemplo.txt"
        else:
           print("\nArquivo inválido.") #Imprime uma mensagem de validação caso o usuário digite um nome inválido.
           return None

        # Carregar a matriz diretamente do arquivo no caminho completo
        matriz = np.loadtxt(caminho_arquivo)

        if isinstance(matriz, np.ndarray):  # Verifica se é uma matriz numpy
            print("\nTipo da matriz:", type(matriz)) #Imprime o tipo da matriz
            print("\nMatriz:")
            print(matriz)

            qtd_linhas, qtd_colunas = matriz.shape #Uso da função shape do Python para obter as dimensões da matriz, que é um objeto Numpy Array.

            #Retornando as quantidades de linhas e colunas:
            print(f"\nQuantidade de linhas: {qtd_linhas}")
            print(f"\nQuantidade de colunas: {qtd_colunas}")
            
            #Salvando os resultados em um arquivo no Google Drive:
            with open(f"/content/drive/My Drive/resultado_{inst}.txt", "w") as saida_arquivo:
                saida_arquivo.write(f"{inst} {qtd_linhas} {qtd_colunas}\n")
            print(f"\nResultado salvo em: /content/drive/My Drive/resultado_{inst}.txt")

        else:
            print("O arquivo não gerou uma matriz numpy.")

    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}") #Mensagem de erro caso o programa não encontre o arquivo
        return None


#Código do input para o usuário e a chamada das funções:

nomeArquivo = input("\nDigite o nome do arquivo:")
MatrizDeGrafos(nomeArquivo) # Chamada da função com o arquivo de parâmetro
