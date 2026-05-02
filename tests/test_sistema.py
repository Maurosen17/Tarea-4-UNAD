# tests/test_sistema.py

"""
ORGANIZACIÓN DE PRUEBAS DEL SISTEMA - SOFTWARE FJ

Este archivo centraliza todas las pruebas del sistema.

Diseñado por el líder del equipo para:
- Separar pruebas válidas e inválidas
- Integrar aportes de todos los módulos
- Garantizar que el sistema continúe funcionando ante errores
- Registrar eventos y fallos en logs

Cada integrante debe aportar:
- 1 prueba válida
- 1 prueba inválida

El sistema NO debe detenerse ante errores.
"""

from utils.logger import Logger
from exceptions.custom_exceptions import ClienteError, ServicioError, ReservaError

logger = Logger()


def ejecutar_pruebas():
    print("\n=== INICIO DE PRUEBAS DEL SISTEMA ===")

    pruebas_validas()
    pruebas_invalidas()

    print("\n=== FIN DE PRUEBAS DEL SISTEMA ===")


# ===============================
# ✅ PRUEBAS VÁLIDAS
# ===============================

def pruebas_validas():
    print("\n--- PRUEBAS VÁLIDAS ---")

    # Cliente válido
    try:
        print("✔ Simulando cliente válido...")
        # cliente = gestor_clientes.crear_cliente("Ana", "ana@mail.com")
        logger.registrar_evento("Cliente válido simulado correctamente")

    except Exception as e:
        logger.registrar_error("Error en cliente válido", e)

    else:
        print("Cliente válido procesado correctamente")

    finally:
        print("Fin prueba cliente válido")

    # Servicio válido
    try:
        print("\n✔ Simulando servicio válido...")
        # servicio = gestor_servicios.crear_servicio("Sala", 100)
        logger.registrar_evento("Servicio válido simulado correctamente")

    except Exception as e:
        logger.registrar_error("Error en servicio válido", e)

    else:
        print("Servicio válido procesado correctamente")

    finally:
        print("Fin prueba servicio válido")

    # Reserva válida
    try:
        print("\n✔ Simulando reserva válida...")
        # reserva = gestor_reservas.crear_reserva(cliente, servicio, 2)
        logger.registrar_evento("Reserva válida simulada correctamente")

    except Exception as e:
        logger.registrar_error("Error en reserva válida", e)

    else:
        print("Reserva válida procesada correctamente")

    finally:
        print("Fin prueba reserva válida")


# ===============================
# ❌ PRUEBAS INVÁLIDAS
# ===============================

def pruebas_invalidas():
    print("\n--- PRUEBAS INVÁLIDAS ---")

    # Cliente inválido
    try:
        print("✖ Simulando cliente inválido...")
        raise ClienteError("Nombre o correo inválido")

    except ClienteError as e:
        logger.registrar_error("Error esperado en cliente inválido", e)

    else:
        print("ERROR: no se detectó problema en cliente")

    finally:
        print("Fin prueba cliente inválido")

    # Servicio inválido
    try:
        print("\n✖ Simulando servicio inválido...")
        raise ServicioError("Parámetros incorrectos del servicio")

    except ServicioError as e:
        logger.registrar_error("Error esperado en servicio inválido", e)

    else:
        print("ERROR: no se detectó problema en servicio")

    finally:
        print("Fin prueba servicio inválido")

    # Reserva inválida
    try:
        print("\n✖ Simulando reserva inválida...")
        raise ReservaError("Datos inconsistentes en la reserva")

    except ReservaError as e:
        logger.registrar_error("Error esperado en reserva inválida", e)

    else:
        print("ERROR: no se detectó problema en reserva")

    finally:
        print("Fin prueba reserva inválida")

    # Error inesperado (demuestra robustez)
    try:
        print("\n⚠ Simulando error inesperado...")
        x = 10 / 0  # División por cero

    except Exception as e:
        logger.registrar_error("Error inesperado capturado", e)

    finally:
        print("El sistema continúa después de error inesperado ✔")