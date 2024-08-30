
def inverter_string(s):
    lista_chars = list(s)
    
    inicio = 0
    fim = len(lista_chars) - 1
    
    while inicio < fim:
        lista_chars[inicio], lista_chars[fim] = lista_chars[fim], lista_chars[inicio]

        inicio += 1
        fim -= 1
    
    return ''.join(lista_chars)

entrada = input("Digite a string para ser invertida: ")

string_invertida = inverter_string(entrada)
print(f"String invertida: {string_invertida}")
