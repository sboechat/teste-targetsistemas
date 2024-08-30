# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


def is_fibonacci(numero:int):
    fib_anterior = 0
    fib_atual = 1
    while True:
        if numero == fib_anterior:
            return True
        elif numero < fib_anterior:
            return False
        else:
            aux = fib_atual
            fib_atual += fib_anterior
            fib_anterior = aux
        
def main():
    try:
        numero = int(input("Informe um número: "))
    except:
        print("Somente são aceitos valores numéricos.")
        return 1
    
    if is_fibonacci(numero):
        print("O número informado faz parte da sequencia de Fibonacci!")
    else:
        print("O número informado NÃO faz parte da sequencia de Fibonacci!")
    return 0

if __name__ == '__main__':
    main()