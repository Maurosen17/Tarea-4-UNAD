from utils.logger import Logger
from exceptions.custom_exceptions import SistemaError
from tests.test_sistema import ejecutar_pruebas

def main():
    logger = Logger()

    logger.registrar_evento("Sistema iniciado")

    print("=== SISTEMA SOFTWARE FJ ===\n")

    try:
        ejecutar_pruebas()

    except SistemaError as e:
        logger.registrar_error("Error del sistema", e)

    except Exception as e:
        logger.registrar_error("Error inesperado", e)

    else:
        print("\nSistema ejecutado correctamente.")

    finally:
        logger.registrar_evento("Sistema finalizado")
        print("\nFin de ejecución del sistema.")


if __name__ == "__main__":
    main()