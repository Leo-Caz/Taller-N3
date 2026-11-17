
def secante(f, p0, p1, TOL=1e-6, N0=50):
    """Devuelve (p, historia), con historia = [p0, p1, p2, ..., p]."""
    # Paso 1: dos puntos iniciales y sus evaluaciones.
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    historia = [p0, p1]

    # Paso 2: iteraciones de la secante.
    while i <= N0:
        if q1 == q0:
            raise ZeroDivisionError(
                f"La secante es horizontal: f({p0}) = f({p1}) = {q1}"
            )

        # Paso 3: fórmula de la secante y registro de p.
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        historia.append(p)

        # Paso 4: criterio de parada.
        if abs(p - p1) < TOL:
            return p, historia

        # Paso 5: incrementar el contador.
        i = i + 1

        # Paso 6: desplazar puntos. Solo una nueva evaluación de f.
        p0, q0 = p1, q1
        p1 = p
        q1 = f(p)

    # Paso 7: agotamiento de iteraciones.
    raise RuntimeError(f"El método fracasó después de {N0} iteraciones")


if __name__ == "__main__":
    llamadas = []

    def f(x):
        llamadas.append(x)
        return x**3 + 4*x**2 - 10

    llamadas.clear()
    p, historia = secante(f, 1.0, 2.0, TOL=1e-6)

    print(f"Solución (6 decimales): {p:.6f}")
    print("Historia de la secante:")
    for indice, aproximacion in enumerate(historia):
        print(f"p{indice} = {aproximacion:.12f}")
    print("Iteraciones (aproximaciones nuevas):", len(historia) - 2)
    print("Evaluaciones de f:", len(llamadas))
