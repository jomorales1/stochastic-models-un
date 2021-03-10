import random


def simulate(beta):
    '''
    :param beta: valor de ß
    :return: verdadero si con los valores de b y c
    la ecuación tiene raíces reales
    '''
    b = random.uniform(-beta, beta)
    c = random.uniform(-beta, beta)
    if b**2 >= c:
        return 1
    return 0


if __name__ == '__main__':
    '''
    El programa determina la probabilidad de obtener raices
    reales de la siguiente ecuación cuadrática
    x^2 + 2bx + c = 0, donde:
    b ~ U(-ß, ß)    c ~ U(-ß, ß)    ß pertenece a R+
    Para lo cual se tienen los siguientes parámetros:
    beta := representa el valor de ß sobre el cual se
    define el intervalo.
    n := representa el número de simulaciones a realizar,
    cuando n tiene valores muy grandes el resultado converge
    a lo obtenido analíticamente.
    '''
    beta = float(input('Ingrese el valor de beta: '))
    n = int(input('Ingrese el número de simulaciones: '))
    successes = 0
    for i in range(n):
        if simulate(beta=beta) == 1:
            successes = successes + 1
    probability = successes / n
    print(f'P(A) = {probability}')
