### Este código está aqui para servir como anotação para o desafio do dia 6, que fiz no Jogo da Forca. ###
# Funções, Indentação e Laços de Repetição em Python #

# Jogo da Forca em Português #

import random
import os

# Lista como fallback (todas em maiúsculas, sem acentos para evitar problemas de encoding)
WORDS = [
    "BANANA","ABACAXI","LARANJA","MORANGO","UVA","MELANCIA","MELAO","PERA","KIWI","MAÇÃ".replace("Ç","C"),
    "CACHORRO","GATO","COELHO","ELEFANTE","LEAO","TIGRE","URSO","RAPOSA","FOCA","CAVALO",
    "VACA","OVEIHA".replace("I","H"),"CABRA","GIRAFA","PANDA","COBRA","TARTARUGA","PASSARO","PAPAGAIO",
    "COMPUTADOR","TECLADO","MOUSE","MONITOR","LIVRO","CANETA","CELULAR","TELEFONE","MESA","CADEIRA",
    "JANELA","PORTA","ROUPA","SAPATO","CHAVE","MOEDA","CARRO","AVIAO","BARCO","TREM",
    "BICICLETA","MOTO","RIO","LAGO","MONTANHA","PRAIA","ILHA","FLORESTA","DESERTO","CIDADE","VILA","PAIS","MUNDO","ESPAÇO".replace("Ç","C"),"ESTRELA","PLANETA","SOL"
]

# Adicionado: arte da forca e constante de tentativas máximas
MAX_TENTATIVAS = 6

HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
        _|_
    """,
    """
     +---+
     |   |
     O   |
         |
         |
        _|_
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
        _|_
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
        _|_
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
        _|_
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
        _|_
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
        _|_
    """
]

def escolher_palavra():
    # tenta carregar de words.txt (uma palavra por linha) no mesmo diretório do script #
    path = os.path.join(os.path.dirname(__file__), "words.txt") # caminho do arquivo words.txt #
    if os.path.exists(path): # verifica se o arquivo existe #
        with open(path, "r", encoding="utf-8") as f: # abre o arquivo em modo leitura com encoding utf-8 que é mais abrangente para caracteres especiais. #
            file_words = [line.strip() for line in f if line.strip()]
        if file_words:
            return random.choice(file_words).upper()
    # fallback para a lista interna se o arquivo não existir ou estiver vazio #
    return random.choice(WORDS).upper()

def jogar_forca(): # Função principal do jogo #
    palavra_secreta = escolher_palavra() # Palavra a ser adivinhada #
    letras_adivinhadas = [] # Letras que o jogador já tentou #
    tentativas = MAX_TENTATIVAS
    print("Bem-vindo ao Jogo da Forca!\n") # Mensagem de boas-vindas #
    while tentativas > 0: # Laço principal do jogo #
        display_palavra = [letra if letra in letras_adivinhadas else "_" for letra in palavra_secreta] # Mostra a palavra com letras adivinhadas #
        print("Palavra: " + " ".join(display_palavra))
        # mostra a arte correspondente ao número de erros até agora
        erros = MAX_TENTATIVAS - tentativas
        print(HANGMAN_STAGES[erros])
        if "_" not in display_palavra: # Verifica se o jogador ganhou #
            print("Parabéns! Você ganhou!")
            break
        palpite = input("Digite uma letra:\n").upper() # Solicita um palpite ao jogador #
        if len(palpite) != 1 or not palpite.isalpha(): # Validação do palpite #
            print("Por favor, digite apenas uma letra.\n")
            continue
        if palpite in letras_adivinhadas: # Verifica se a letra já foi tentada #
            print("Você já tentou essa letra. Tente outra.\n")
            continue
        letras_adivinhadas.append(palpite)
        if palpite not in palavra_secreta: # Letra incorreta #
            tentativas -= 1
            print(f"Letra incorreta! Você tem {tentativas} tentativas restantes.\n")
    else: # Executa se o jogador perder #
        # mostra a forca completa antes de informar a perda #
        print(HANGMAN_STAGES[-1])
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

jogar_forca() # Inicia o jogo #