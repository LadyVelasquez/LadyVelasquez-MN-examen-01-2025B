import matplotlib.pyplot as plt
import numpy as np

def Spline(x, x0, pars):
    a = pars["a"]
    b = pars["b"]
    c = pars["c"]
    d = pars["d"]
    return a + b * (x - x0) + c * (x - x0) ** 2 + d * (x - x0) ** 3

xs = [-1, 0, 1]
ys = [1, 5, 3]

# Coeficientes calculados para m = -3
s = [
    {"a": 1, "b": 7.5, "c": 0, "d": -3.5},
    {"a": 5, "b": -3, "c": 1.5, "d": -0.5}
]

# Gráfica
plt.figure(figsize=(8, 6))

for i, x_i in enumerate(xs[:-1]):
    x_val = np.linspace(x_i, xs[i+1], 100)
    y_val = Spline(x_val, x_i, s[i])
    plt.plot(x_val, y_val, color='red', label=f'Spline {i}' if i==0 else "")

# Puntos originales
plt.scatter(xs, ys, color='blue', zorder=5, label='Puntos dados')

# Visualización de la pendiente deseada m=-3 en x=0
m_deseada = -3
x_tang = np.linspace(-0.3, 0.3, 10)
y_tang = 5 + m_deseada * (x_tang - 0)
plt.plot(x_tang, y_tang, '--', color='green', label='Pendiente m=-3')

plt.title(f"Interpolación con Splines Cúbicos (m={m_deseada})")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()