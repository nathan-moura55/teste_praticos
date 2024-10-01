# função para inverter a string
def inverter_string(texto):
    invertida = ''

    for i in range(len(texto) -1, -1, -1):
          invertida += texto[i]  
    return invertida

# solicita a entrada do usuario 
entrada = input("Digite uma palavra para ser invertida: ")

# chama a funçao para inverter
resultado = inverter_string(entrada)
print(f"A string invertida é: {resultado}")