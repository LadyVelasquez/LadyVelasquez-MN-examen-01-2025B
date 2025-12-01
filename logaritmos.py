import numpy as np
import matplotlib.pyplot as plt

def redondear_sig(numero, cifras=6):
    if numero == 0:
        return 0
    escala = int(np.floor(np.log10(abs(numero))))
    return round(numero, cifras - escala - 1)

def metodo_briggs(x, iteraciones=5):
    valor = x
    for _ in range(iteraciones):
        valor = np.sqrt(valor)
        valor = redondear_sig(valor, 6)
    
    r = valor - 1
    alpha = 1 / np.log(10)
    return (alpha * r) * (2 ** iteraciones)

# se calcula aqui
alpha = 1 / np.log(10)

log2 = metodo_briggs(2)
log3 = metodo_briggs(3)
log7 = metodo_briggs(7)

log4 = 2 * log2
log5 = 1 - log2
log6_suma = log2 + log3
log8 = 3 * log2
log9 = 2 * log3

val_aux = 1.0077696
log_aprox_aux = alpha * (val_aux - 1)
log6_potencia = (log_aprox_aux + 7) / 9

datos_tabla = [
    (1, 0.0, "-"),
    (2, log2, "B"),
    (3, log3, "B"),
    (4, log4, "2"),
    (5, log5, ),
    (6, log6_suma, ""),     
    (6, log6_potencia, ""),        
    (7, log7, "Briggs"),
    (8, log8, ""),
    (9, log9, ""),
    (10, 1.0, "-")
]


for fila in datos_tabla:
    x, val_calc, pista = fila
    
    if x == 1 or x == 10:
        error = 0.0
    else:
        val_real = np.log10(x)
        error = abs(val_calc - val_real) / val_real

    print(f"{x:<5} {val_calc:<15.6f} {pista:<20} {error:<15.6f}")