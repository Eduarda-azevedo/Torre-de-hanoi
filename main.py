def torre_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"*Mova o disco 1 de {origem} para {destino}")
        return
    torre_hanoi(n-1, origem, auxiliar, destino)
    print(f"-Mova o disco {n} de {origem} para {destino}")
    torre_hanoi(n-1, auxiliar, destino, origem)

n = int(input("Digite o número de discos: "))
varetas = input("Digite o nome das três varetas separadas por espaço: ").split()
torre_hanoi(n, varetas[0], varetas[1], varetas[2])