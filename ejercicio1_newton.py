
def newton_raphson(f, df, p0, TOL=1e-6, N0=50):
    """Devuelve (p, historia), con historia = [p0, p1, ..., p]."""
    historia = [p0]
    i = 1

    while i <= N0:
        d = df(p0)
        if d == 0:
            raise ZeroDivisionError(
                f"f'(p0) = 0 en p0 = {p0}: la tangente es horizontal"
            )

        # Paso 3: nueva aproximación.
        p = p0 - f(p0) / d
        historia.append(p)

        # Paso 4: criterio de parada.
        if abs(p - p0) < TOL:
            return p, historia

        # Pasos 5 y 6: avanzar la iteración y el punto.
        i = i + 1
        p0 = p

    raise RuntimeError(f"El método fracasó después de {N0} iteraciones")

def f(x):
    return x**3 + 4*x**2 - 10

def df(x):
    return 3*x**2 + 8*x

if __name__ == "__main__":
    p, historia = newton_raphson(f, df, 1.5, TOL=1e-6)
    print(f"Solución (6 decimales): {p:.6f}")
    print("Historia de Newton:")
    for indice, aproximacion in enumerate(historia):
        print(f"p{indice} = {aproximacion:.12f}")