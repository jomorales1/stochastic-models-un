import random


def simulate(beta):
    b = random.uniform(-beta, beta)
    c = random.uniform(-beta, beta)
    if b**2 >= c:
        return 1
    return 0


if __name__ == '__main__':
    beta = float(input('Ingrese el valor de beta: '))
    n = int(input('Ingrese el número de simulaciones: '))
    successes = 0
    for i in range(n):
        if simulate(beta=beta) == 1:
            successes = successes + 1
    probability = successes / n
    print(f'P(A) = {probability}')
