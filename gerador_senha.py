import random
import string

def gerar_senha(tamanho=8, usar_maiusculas=True, usar_minusculas=True, usar_digitos=True, usar_simbolos=True):
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_digitos:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado.")

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    print("Gerador de Senhas")
    tamanho = int(input("Digite o tamanho da senha: "))

    usar_maiusculas = input("Usar letras maiúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("Usar letras minúsculas? (s/n): ").lower() == 's'
    usar_digitos = input("Usar dígitos? (s/n): ").lower() == 's'
    usar_simbolos = input("Usar símbolos? (s/n): ").lower() == 's'

    senha_gerada = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_digitos, usar_simbolos)
    print(f"Senha gerada: {senha_gerada}")
    