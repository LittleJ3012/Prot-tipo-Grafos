#Aluna: Julia Barcellos Paiva
#Matrícula: 2022010393
#Curso: Ciência da Computação

#Observação importante: Este protótipo de Software foi desenvolvido primeiro no Google Collab, e depois realocado para o repositório GitHub.

import numpy as np
from google.colab import drive #Para fazer a conexão com os arquivos (ponte.txt, zachary.txt e exemplo.txt, que estão no meu Google Drive)

# Montando o Google Drive
drive.mount('/content/drive')


#A primeira função lê o arquivo.txt (passado como parâmetro pelo usuário) e armazena o conteúdo do arquivo em uma matriz do tipo numpy. Ela também
#retorna a matriz e seu tipo.
def LendoOsDados(inst): #O parâmetro é o nome do dataset(inst) 
    try:

        # Definindo o caminho para o arquivo:
        caminho_arquivo = "/content/drive/My Drive/" + inst + '.txt'

        # Carregar a matriz diretamente do arquivo no caminho completo
        matriz = np.loadtxt(caminho_arquivo)

        if isinstance(matriz, np.ndarray):  # Verifica se é uma matriz numpy
           print("\nTipo da matriz:", type(matriz)) #Imprime o tipo da matriz
           print(f"\nMatriz:\n\n{matriz}\n")
           return matriz

        else:
            print("O arquivo não gerou uma matriz numpy.") #Mensagem de validação.

    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}") #Mensagem de erro caso o programa não encontre o arquivo
        return None


#A segunda função calcula a dimensão da matriz, retornando a quantidade de linhas e colunas.
def calculaDimensaoMatriz(matriz):
    qtd_linhas, qtd_colunas = matriz.shape #Uso da função shape do Python para obter as dimensões da matriz, que é um objeto Numpy Array.

    #Retornando as quantidades de linhas e colunas:
    return qtd_linhas, qtd_colunas

            
  #A terceira função salva os dados sobre as linhas e as colunas em um arquivo no Google Drive:
def salvaResultado(inst, qtd_linhas, qtd_colunas):
            with open(f"/content/drive/My Drive/resultado_{inst}.txt", "w") as saida_arquivo:
                saida_arquivo.write(f"{inst} {qtd_linhas} {qtd_colunas}\n") #Salvando o nome da instância e a dimensão da matriz
            print(f"\nResultado salvo em: resultado_{inst}.txt")

#Definição da main:
if __name__ == '__main__':

#Código do input para o usuário e a chamada das funções:
   inst = input("\nDigite o nome do arquivo:")
   matriz = LendoOsDados(inst) # Chamada da função que retorna a matriz e seu tipo

   if matriz is not None: #Valida a matriz
        qtd_linhas, qtd_colunas = calculaDimensaoMatriz(matriz)  # Obtém as dimensões
        print(f"\nDimensões da matriz: {qtd_linhas} linhas x {qtd_colunas} colunas")  # Imprime as dimensões na tela
        salvaResultado(inst, qtd_linhas, qtd_colunas)  # Chamada da função que salva as dimensões
 

