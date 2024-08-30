
def inverter_string(palavra: str):
    palavra_invertida = ""
    for _ in palavra:
        palavra_invertida+=palavra[-1]
        palavra = palavra[:-1]
    return palavra_invertida

def main():
    palavra = input("Escreva uma palavra: ")
    palavra_invertida = inverter_string(palavra)
    print(palavra_invertida)
    
if __name__ == '__main__':
    main()