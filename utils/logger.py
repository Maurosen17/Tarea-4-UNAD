# utils/logger.py

import os
from datetime import datetime
from config.settings import RUTA_LOGS

class Logger:
    """
    Clase encargada del registro de eventos y errores del sistema.
    Garantiza que el sistema no falle si no existe la carpeta de logs.
    """

    def __init__(self):
        # Crear carpeta automáticamente si no existe
        os.makedirs(os.path.dirname(RUTA_LOGS), exist_ok=True)

    def registrar_error(self, mensaje, excepcion=None):
        """
        Registra errores del sistema.
        """
        try:
            with open(RUTA_LOGS, "a", encoding="utf-8") as archivo:
                fecha = datetime.now()
                archivo.write(f"[ERROR] {fecha} - {mensaje}")

                if excepcion:
                    archivo.write(f" - {str(excepcion)}")

                archivo.write("\n")

        except Exception as e:
            # Última línea de defensa: evitar que el logger rompa el sistema
            print("Error crítico al escribir en logs:", e)

    def registrar_evento(self, mensaje):
        """
        Registra eventos normales del sistema.
        """
        try:
            with open(RUTA_LOGS, "a", encoding="utf-8") as archivo:
                fecha = datetime.now()
                archivo.write(f"[INFO] {fecha} - {mensaje}\n")

        except Exception as e:
            print("Error crítico al escribir evento:", e)