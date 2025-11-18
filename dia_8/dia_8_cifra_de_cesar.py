### Desafio Cifra de Cesar ###
# Objetivo: Criar um programa que implemente a cifra de César, uma técnica simples de criptografia.
# Regras:
# 1. O programa deve solicitar ao usuário uma mensagem para criptografar ou descriptograf
# 2. O programa deve solicitar ao usuário um número de deslocamento (shift) para a cifra.
# 3. O programa deve aplicar a cifra de César à mensagem com base no deslocamento fornecido.
# 4. O programa deve lidar com letras maiúsculas e minúsculas, mantendo a capitalização original.
# 5. O programa deve preservar espaços e caracteres não alfabéticos sem alterações.

import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode): # Função para encriptar e desencriptar o texto
    output_text = ""
    if encode_or_decode == "decode":
        shifted_position *= -1
    
    for letter in original_text:
        
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")
    
should_continue = True

while should_continue: # Loop para permitir múltiplas operações
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
    
