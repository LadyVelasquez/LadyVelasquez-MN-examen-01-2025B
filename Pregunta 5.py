import numpy as np
import matplotlib.pyplot as plt

# --- FUNCIONES ---
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
    # Fórmula: log(x) ~ 2^n * alpha * r
    return (alpha * r) * (2 ** iteraciones)

# --- CÁLCULOS ---
alpha = 1 / np.log(10)

#Calcular bases con Briggs
log2 = metodo_briggs(2)
log3 = metodo_briggs(3)
log7 = metodo_briggs(7)

#Calcular derivados con propiedades logarítmicas
log4 = 2 * log2
log5 = 1 - log2
log6_suma = log2 + log3
log8 = 3 * log2
log9 = 2 * log3

#Calcular log(6) especial con 6^9
val_aux = 1.0077696
log_aprox_aux = alpha * (val_aux - 1)
log6_potencia = (log_aprox_aux + 7) / 9


datos_tabla = [
    (1, 0.0, "-"),
    (2, log2, "Briggs"),
    (3, log3, "Briggs"),
    (4, log4, "2 * log(2)"),
    (5, log5, "1 - log(2)"),
    (6, log6_suma, "log(2) + log(3)"),     # Primer 6
    (6, log6_potencia, "6^9 = ..."),         # Segundo 6 (mejorado)
    (7, log7, "Briggs"),
    (8, log8, "3 * log(2)"),
    (9, log9, "2 * log(3)"),
    (10, 1.0, "-")
]


print(f"{'x':<5} {'Logaritmo':<15} {'Pista':<20} {'Error Relativo':<15}")
print("-" * 65)

for fila in datos_tabla:
    x, val_calc, pista = fila
    
    # Calcular error relativo
    if x == 1 or x == 10:
        error = 0.0
    else:
        val_real = np.log10(x)
        error = abs(val_calc - val_real) / val_real

    # Imprimir fila con 6 decimales de precision
    print(f"{x:<5} {val_calc:<15.6f} {pista:<20} {error:<15.6f}")

# --- COMPARACIÓN LOG(6) ---
print("\n--- Comparación log(6) ---")
print(f"Método A (log2 + log3): {log6_suma:.6f}")
print(f"Método B (6^9):         {log6_potencia:.6f}")
print(f"Valor Real:             {np.log10(6):.6f}")

# --- GRÁFICA DE LA APROXIMACIÓN ---
r_vals = np.linspace(0, 0.5, 100)
y_real = np.log10(1 + r_vals)
y_aprox = alpha * r_vals

plt.figure(figsize=(8, 5))
plt.plot(r_vals, y_real, label=r"Real: $\log_{10}(1+r)$", color="blue")
plt.plot(r_vals, y_aprox, label=r"Aprox: $\alpha \cdot r$", color="red", linestyle="--")
plt.title("Aproximación Lineal de Briggs")
plt.xlabel("r")
plt.ylabel("Valor")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()