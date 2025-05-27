#1: O que acontece se tentarmos escrever (write()) em um arquivo aberto apenas para leitura ("r")?
#Resposta: Se tentarmos escrever em um arquivo aberto apenas para leitura, vai da erro.
    #Prática:
arquivo = open("arquivo.txt", "r")
arquivo.write("Café")

#2: O que acontece se tentarmos ler (read()) de um arquivo aberto apenas para escrita ("w")?
#Resposta: Se tentarmos ler de um arquivo aberto apenas para escrita, vai da erro.
    #Prática:
arquivo = open("arquivo.txt", "w")
arquivo.read()

#3: Qual a diferença entre os modos "w" e "a" ao abrir um arquivo? Quando cada um é útil?
#Resposta: O modo w abre o arquivo para escrite, sobrescrevendo o seu conteúdo anterior (se tinha ainda) e o modo a abre o arquivo
#para escrita, mas adicionando o novo conteúdo ao final do arquivo. (w vem de write, a vem de append, faz sentido.)
    #Prática:
arquivo = open("arquivo.txt", "w")  # Modo "w" - sobrescreve o arquivo
arquivo = open("arquivo.txt", "a")  # Modo "a" - adiciona ao final do arquivo

#4: O que acontece se abrirmos um arquivo inexistente no modo "r"? E no modo "w"?
#Resposta: Se abrir um arquivo inexistente no r vai da erro, e se abrir no w vai da erro.
    #Prática:
arquivo = open("arquivo_inexistente.txt", "r") #Vai da erro
arquivo = open("arquivo_inexistente.txt", "w") #Vai da erro

#5: Por que é importante fechar um arquivo após usá-lo (arquivo.close())? O que pode acontecer se não fizermos isso?
#Resposta: Assim, é importante primeiramente pra salvar oq tu fez, e também pra evitar problemas de memória e corrupção de dados.
    #Prática:
arquivo.close() #Fecha o arquivo e salva

#6: Como substituir uma linha específica de um arquivo (ex.: alterar a 3ª linha)?
#Resposta: Se utiliza o método readlines() para ler as linhas, depois altera a linha desejada com o método write().
    #Prática:
arquivo.readlines()  # Lê todas as linhas do arquivo
arquivo.write("Nova linha 3\n")  # Escreve a nova linha no arquivo

#7: Desafio. Como contar quantas vezes uma palavra aparece em um arquivo?
    #Prática:
def contar_palavra(arquivo, palavra):
    with open(arquivo, 'r') as f:
        conteudo = f.read()
        return conteudo.count(palavra)