
from ejercicio2_secante import secante


def saldo_final(i, monto=20000.0, cuota=450.0, meses=60):
    """Saldo luego de aplicar el interés y pagar cada cuota mensual."""
    saldo = monto
    for mes in range(meses):
        saldo = saldo * (1 + i) - cuota
    return saldo


if __name__ == "__main__":
    sin_interes = saldo_final(0)
    i, historia = secante(saldo_final, 0.005, 0.02, TOL=1e-10)
    tasa_mensual = i * 100
    tasa_efectiva_anual = ((1 + i)**12 - 1) * 100

    print(f"Saldo sin interés: {sin_interes:.2f}")
    print(f"Tasa mensual: {tasa_mensual:.4f}%")
    print(f"Tasa efectiva anual: {tasa_efectiva_anual:.2f}%")
    print(f"Saldo final con la tasa calculada: {saldo_final(i):.10f}")
    print("Iteraciones de secante:", len(historia) - 2)
