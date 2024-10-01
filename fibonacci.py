# geração a sequência de Fibonacci com limite
def fibonacci_seq(limite):
    seq = [0, 1]
    while seq[-1] < limite:
        seq.append(seq[-1] + seq[-2])
    return seq

# verificação
def pertence_a_fibonacci(numero):
    seq = fibonacci_seq(numero)
    return numero in seq

# Solicitando o input do usuário
entrada = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# output
if pertence_a_fibonacci(entrada):
    print(f"{entrada} pertence à sequência de Fibonacci.")
else:
    print(f"{entrada} NÃO pertence à sequência de Fibonacci.")