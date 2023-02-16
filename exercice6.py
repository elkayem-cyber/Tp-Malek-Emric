def somme_fibonacci(n, m):
    # Initialisation des deux premiers termes de la suite
    fib1, fib2 = 0, 1
    # Calcul des n premiers termes de la suite
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
    # Calcul de la somme des m termes suivants
    somme = 0
    for i in range(m):
        somme += fib1
        fib1, fib2 = fib2, fib1 + fib2
    return somme
