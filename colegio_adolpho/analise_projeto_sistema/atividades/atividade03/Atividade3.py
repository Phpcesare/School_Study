#exercício 1
def media(x,y,z):
    conta=x+y+z
    return conta/3
result=media(1,2,3)
print(result)

#exercício 2
def numero(t):
    if t%2==0:
        print("par")
        return "par"
    else:
        print("impar")
        return "impar"

#exercício 3
def fibo (limite):
    a, b = 0, 1
    while a <= limite:
        print(a, end='')
        a, b = b, a + b
        print()

fibo(10)

#exercício 4
from statistics import mean, median, mode
def est(numeros):
    return {
        'media': mean(numeros),
        'mediana': median(numeros),
        'moda': mode(numeros),
        'min': min(numeros),
        'max': max(numeros)
    }
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
resultado = est(numeros)
print(f"Estatisticas ae {resultado}")

#exercicio 5
def vogal (palavra):
    vogal = 'a, e, i, o, u, A, E, I, O, U'
    return sum(1 for char in palavra if char in vogal)

#exercício 6 - crie umas listas ae e bota uns bgl ae
lista_nome = []
lista_idade = []
lista_telefone = []
while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    telefone = input("Digite seu telefone: ")
    if not lista_nome or not lista_idade or not lista_telefone:
        print("Erro: Nome, idade ou telefone não podem ser nulos.")
        continue
    lista_nome.append(nome)
    lista_idade.append(idade)
    lista_telefone.append(telefone)
    print("Informações cadastradas:")
    if input("Deseja sair? (s/n)") == 's':
        break
#continuação do exercício 6 - Adicione uma verificação se o nome, idade e telefone que a pessoa digitou não é nulo