def verificar_letra_a(string):
    # Converte a string para minúsculas e conta as ocorrências de 'a'
    quantidade_a = string.lower().count('a')
    
    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vezes.")
    else:
        print("A letra 'a' não foi encontrada.")

# Exemplo de uso
texto = input("Digite uma string: ")
verificar_letra_a(texto)