# arquivo =  open('teste.txt','w') #subreescreve o arquivo
# arquivo1 =  open('teste1.txt','a') #manten e escreve nova linha o arquivo
# arquivo.write('Minha primeiro escrita')
# arquivo.close()

def escrever_arquivo(texto):
    diretorio = 'C:/Users/renato/PycharmProjects/teste.txt'
    #arquivo = open('teste.txt', 'w')  # subreescreve o arquivo diretorio que esta rodando
    arquivo = open(diretorio, 'w')  # subreescreve o arquivo
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste1.txt', 'a') #manten e escreve nova linha o arquivo
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo,'c:/') # mantem mo nome
    shutil.copy(nome_arquivo, 'c:/.novoNome.tetx')  # troca o nome

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo,'c:/')

if __name__ == '__main__':
    #escrever_arquivo("Primeira linha \n")
    atualizar_arquivo("Segunda linha \n")

