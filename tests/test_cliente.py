"""
tests/test_sistema.py
=====================
Pruebas del sistema Software FJ.

SECCIÓN: Clase Cliente
  - Caso 1: registro válido
  - Caso 2: registro inválido (6 sub-casos)
"""

import sys
import os
import logging

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# ── Logger ──────────────────────────────────────────────────────────────────
os.makedirs("data", exist_ok=True)

logger = logging.getLogger("software_fj")
if not logger.handlers:
    logger.setLevel(logging.DEBUG)
    fmt = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s", "%Y-%m-%d %H:%M:%S")

    fh = logging.FileHandler("data/software_fj.log", encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)

    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)
    ch.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(ch)

# ── Imports del proyecto ────────────────────────────────────────────────────
from models.cliente import Cliente
from exceptions.cliente_exceptions import (
    ClienteError,
    NombreInvalidoError,
    EmailInvalidoError,
    TelefonoInvalidoError,
    IDClienteInvalidoError,
)


# ============================================================================
# CASO 1 — REGISTRO VÁLIDO
# ============================================================================

def test_cliente_valido():
    """
    Crea un cliente con datos correctos y verifica getters y setters.
    Bloque: try / except / else / finally
    """
    logger.info("─" * 55)
    logger.info("CASO 1 — Registro válido de cliente")
    logger.info("─" * 55)
    print("\n─── CASO 1 — Registro válido de cliente ───")

    cliente = None
    try:
        cliente = Cliente(
            id_cliente="CLI001",
            nombre="Fernanda Jiménez López",
            email="fernanda@softwarefj.com",
            telefono="+573001234567",
        )

    except ClienteError as e:
        logger.error("CASO 1 — Error inesperado: %s", e)
        print(f"  [ERROR] {e}")

    else:
        # Solo se ejecuta si no hubo excepción
        assert cliente.id_cliente == "CLI001"
        assert cliente.nombre     == "Fernanda Jiménez López"
        assert cliente.email      == "fernanda@softwarefj.com"
        assert cliente.telefono   == "+573001234567"

        # Actualización controlada por setters
        cliente.email    = "fernanda.nueva@softwarefj.com"
        cliente.telefono = "3109876543"
        assert cliente.email    == "fernanda.nueva@softwarefj.com"
        assert cliente.telefono == "3109876543"

        logger.info("CASO 1 EXITOSO — %s", cliente)
        print(f"  [OK] {cliente}")

    finally:
        logger.info("CASO 1 — Finalizado.")
        print("  [INFO] Caso 1 finalizado.\n")


# ============================================================================
# CASO 2 — REGISTROS INVÁLIDOS
# ============================================================================

def test_cliente_invalido():
    """
    Intenta crear clientes con datos incorrectos.
    El sistema captura cada error, lo registra y continúa operando.
    Bloque: try / except / finally  +  encadenamiento de excepciones
    """
    logger.info("─" * 55)
    logger.info("CASO 2 — Intentos inválidos de registro")
    logger.info("─" * 55)
    print("─── CASO 2 — Intentos inválidos de registro ───")

    sub_casos = [
        {
            "desc": "2a — Nombre con números",
            "datos": dict(id_cliente="CLI002", nombre="Juan123 Pérez",
                          email="juan@softwarefj.com", telefono="3001112233"),
            "excepcion": NombreInvalidoError,
        },
        {
            "desc": "2b — Email sin '@'",
            "datos": dict(id_cliente="CLI003", nombre="Ana Torres",
                          email="ana.torres.softwarefj.com", telefono="3002223344"),
            "excepcion": EmailInvalidoError,
        },
        {
            "desc": "2c — Teléfono con letras",
            "datos": dict(id_cliente="CLI004", nombre="Carlos Ruiz",
                          email="carlos@softwarefj.com", telefono="ABCD1234"),
            "excepcion": TelefonoInvalidoError,
        },
        {
            "desc": "2d — ID duplicado (CLI001 ya existe)",
            "datos": dict(id_cliente="CLI001", nombre="Laura Gómez",
                          email="laura@softwarefj.com", telefono="3003334455"),
            "excepcion": IDClienteInvalidoError,
        },
        {
            "desc": "2e — Nombre demasiado corto",
            "datos": dict(id_cliente="CLI005", nombre="X",
                          email="x@softwarefj.com", telefono="3004445566"),
            "excepcion": NombreInvalidoError,
        },
        {
            "desc": "2f — Campos vacíos",
            "datos": dict(id_cliente="", nombre="", email="", telefono=""),
            "excepcion": ClienteError,
        },
    ]

    for sub in sub_casos:
        try:
            Cliente(**sub["datos"])
            # Si llega aquí, la validación no funcionó
            logger.error("CASO %s — Debió rechazarse pero el objeto se creó.", sub["desc"])
            print(f"  [FALLO LÓGICO] {sub['desc']}: debió rechazarse.")

        except sub["excepcion"] as e:
            # Error esperado: se registra y el sistema sigue
            logger.warning("CASO %s — %s: %s", sub["desc"], type(e).__name__, e)
            print(f"  [OK - Rechazado] {sub['desc']}: {type(e).__name__}")

        except Exception as e:
            # Error inesperado: se encadena y registra
            try:
                raise ClienteError(f"Error inesperado en {sub['desc']}") from e
            except ClienteError as ce:
                logger.error("CASO %s — %s | Causa: %s", sub["desc"], ce, e)
                print(f"  [ERROR INESPERADO] {sub['desc']}: {ce}")

        finally:
            logger.debug("CASO %s — sub-caso procesado.", sub["desc"])

    print("\n  [INFO] Caso 2 finalizado. El sistema sigue operando.\n")


# ============================================================================
# EJECUCIÓN
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("  SOFTWARE FJ — PRUEBAS CLASE CLIENTE")
    print("=" * 55)

    Cliente.limpiar_registro_ids()

    test_cliente_valido()
    test_cliente_invalido()

    print("=" * 55)
    print("  Pruebas finalizadas. Log → data/software_fj.log")
    print("=" * 55 + "\n")