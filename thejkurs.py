import socket as s
from sys import argv, exit

portas_abertas = []


def port_scan(alvo, porta_inicial, porta_final):
    print(f'Escaneando o alvo: {alvo}')

    for porta in range(porta_inicial, porta_final + 1):
        sock = s.socket(s.AF_INET, s.SOCK_STREAM)
        sock.settimeout(1)

        resultado = sock.connect_ex((alvo, porta))

        if resultado == 0:
            portas_abertas.append(porta)

if __name__ == '__main__':
    if len(argv) != 4:
        print('Modo de uso: python3 thejkurs.py HOST PORTA INICIAL PORTA FINAL')
        print(argv)
        exit()
    
    alvo = argv[1]
    porta_inicial = int(argv[2])
    porta_final = int(argv[3])

    port_scan(alvo, porta_inicial, porta_final)
    print(f'Portas abertas: {portas_abertas}')

    