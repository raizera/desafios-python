import numpy as np

numeros = np.random.rand(5) # Gera 5 números aleatórios entre 0 e 1

maiores_que_0_3 = list(
    map(
        lambda x:round(x, 2), 
        filter(
            lambda x:x > 0.3, numeros
            )
        )
    )

print(maiores_que_0_3)