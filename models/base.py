# models/base.py

from abc import ABC, abstractmethod
import uuid

class BaseEntidad(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.

    Todas las clases del sistema (Cliente, Servicio, Reserva)
    DEBEN heredar de esta clase.

    Proporciona:
    - Identificador único (encapsulado)
    - Método obligatorio para mostrar información
    """

    def __init__(self):
        self._id = str(uuid.uuid4())

    @property
    def id(self):
        """
        Retorna el ID de la entidad (solo lectura).
        """
        return self._id

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método que debe ser implementado por todas las clases hijas.
        """
        pass