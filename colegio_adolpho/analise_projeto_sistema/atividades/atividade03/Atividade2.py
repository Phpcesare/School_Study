"""
2ª Prova - Exercício 02
Jogo de adivinhação
Aluno 1: Pedro Henrique Pavani Cesare
Aluno 2: Pedro Martelo
"""

from random import randint
import random

while True:
    numero_secreto = random.randint(1, 100)
    tentativas_maximas = 10
    tentativas = 0
    acertou = False
    pontuacao = 0
    numero_maximo = 100
    numero_minimo = 1
    tentativa = randint(numero_minimo, numero_maximo)
    
    print("\n=== JOGO DE ADiVINHAÇÃO ===")
    print(f"Tente adivinhar o número entre 1 e 100. Você tem {tentativas_maximas} tentativas!")

    # Implementar a lógica do jogo.


    while not acertou:
        if tentativas >= tentativas_maximas:
            print("Acabaram suas chances!")
            break
        numero = int(input("Digite um número entre 1 e 100."))
        if numero is not numero_secreto:
            print(f"Você errou, você tem mais {tentativas_maximas-tentativas} tentativas!")
            tentativas += 1
        else:
            print(f"Você acertou, sua pontuação foi de {pontuacao} pontos!")
            break

    # Calcular a pontuação conforme as tentativas usadas.

    (tentativas_maximas - tentativas) == pontuacao

    # Adicionar validação para evitar erros (ex: palpite fora do intervalo 1–100).

    if tentativa > numero_maximo:
                print(f'Número inválido! Digite um número entre 1 e {numero_maximo}')

    elif tentativa < numero_secreto:
                print('O número é maior!')

    elif tentativa > numero_secreto:
                print('O número é menor!')

    elif not numero_minimo:
                print('Digite um número válido!')

    elif not numero_maximo:
                print('Digite um número válido!')            

    elif tentativa == numero_secreto:
                print('Você acertou!')
                pontuação += 1

    if not acertou:
        print(f"\nFim de jogo! O número era {numero_secreto}.")

    jogar_novamente = input("\nQuer jogar de novo? (s/n): ").strip().lower()
    if jogar_novamente != 's':
        break
