"""
2ª Prova - Exercício 02
Jogo de adivinhação
Aluno 1: Pedro Henrique Pavani Cesare
Aluno 2: Pedro Martelo
"""

import random

while True:
    numero_secreto = random.randint(1, 100)
    tentativas_maximas = 10
    tentativas = 0
    acertou = False
    numero_maximo = 100
    numero_minimo = 1

    print("\n=== JOGO DE ADiVINHAÇÃO ===")
    print(f"Tente adivinhar o número entre {numero_minimo} e {numero_maximo}. Você tem {tentativas_maximas} tentativas!")

    # Implementar a lógica do jogo.
    while tentativas < tentativas_maximas:
        palpite = int(input(f"Tentativa {tentativas + 1}: "))
        tentativas += 1
        if palpite == numero_secreto:
            acertou = True
            print(f"Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            break
        elif palpite < numero_minimo and palpite > numero_maximo:
            print('o numero deve estar entre 1 e 100')    
        elif palpite < numero_secreto:
            print("O seu palpite é menor que o número, tente novamente com um número maior.")
        else:
            print("O número é menor, tente com um palpite menor.")
    pontuacao = (tentativas_maximas - tentativas)
    if not acertou:
        print(f"\nFim de jogo! O número era {numero_secreto}.")

    jogar_novamente = input("\nQuer jogar de novo? (s/n): ").strip().lower()
    if jogar_novamente != 's':
        break
