"""
models/cliente.py
Clase Cliente con encapsulación, validaciones y excepciones personalizadas.
"""

import re
import logging
from abc import ABC, abstractmethod

from exceptions.cliente_exceptions import (
    ClienteError,
    NombreInvalidoError,
    EmailInvalidoError,
    TelefonoInvalidoError,
    IDClienteInvalidoError,
)

logger = logging.getLogger("software_fj")


# ── Clase abstracta base ────────────────────────────────────────────────────

class EntidadBase(ABC):
    @abstractmethod
    def describir(self) -> str:
        pass

    @abstractmethod
    def obtener_id(self) -> str:
        pass

    def __str__(self):
        return self.describir()


# ── Clase Cliente ───────────────────────────────────────────────────────────

class Cliente(EntidadBase):
    """
    Representa a un cliente de Software FJ.

    Atributos privados (acceso solo por propiedades):
        __id_cliente : identificador único (3-20 chars alfanuméricos/guiones)
        __nombre     : nombre completo (solo letras y espacios, 3-80 chars)
        __email      : correo electrónico con formato válido
        __telefono   : número de contacto (7-15 dígitos, puede iniciar con '+')
    """

    _ids_registrados: set = set()

    _RE_EMAIL    = re.compile(r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$")
    _RE_TELEFONO = re.compile(r"^\+?[0-9]{7,15}$")
    _RE_ID       = re.compile(r"^[A-Za-z0-9_\-]{3,20}$")
    _RE_NOMBRE   = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$")

    # ── Constructor ─────────────────────────────────────────────────────────

    def __init__(self, id_cliente: str, nombre: str, email: str, telefono: str):
        self.__id_cliente = self._validar_id(id_cliente)
        self.__nombre     = self._validar_nombre(nombre)
        self.__email      = self._validar_email(email)
        self.__telefono   = self._validar_telefono(telefono)

        Cliente._ids_registrados.add(self.__id_cliente)
        logger.info("Cliente registrado | ID: %s | Nombre: %s", self.__id_cliente, self.__nombre)

    # ── Validaciones privadas ───────────────────────────────────────────────

    @classmethod
    def _validar_id(cls, valor) -> str:
        if not isinstance(valor, str) or not valor.strip():
            raise IDClienteInvalidoError("El ID no puede estar vacío.")
        v = valor.strip()
        if not cls._RE_ID.match(v):
            raise IDClienteInvalidoError(
                f"ID '{v}' inválido. Use 3-20 caracteres alfanuméricos, guiones o guiones bajos."
            )
        if v in cls._ids_registrados:
            raise IDClienteInvalidoError(f"El ID '{v}' ya está registrado.")
        return v

    @classmethod
    def _validar_nombre(cls, valor) -> str:
        if not isinstance(valor, str) or not valor.strip():
            raise NombreInvalidoError("El nombre no puede estar vacío.")
        v = valor.strip()
        if len(v) < 3:
            raise NombreInvalidoError(f"Nombre '{v}' muy corto (mínimo 3 caracteres).")
        if len(v) > 80:
            raise NombreInvalidoError("El nombre excede 80 caracteres.")
        if not cls._RE_NOMBRE.match(v):
            raise NombreInvalidoError(f"Nombre '{v}' contiene caracteres inválidos. Solo letras y espacios.")
        return v

    @classmethod
    def _validar_email(cls, valor) -> str:
        if not isinstance(valor, str) or not valor.strip():
            raise EmailInvalidoError("El correo no puede estar vacío.")
        v = valor.strip().lower()
        if not cls._RE_EMAIL.match(v):
            raise EmailInvalidoError(f"Correo '{v}' no tiene formato válido.")
        return v

    @classmethod
    def _validar_telefono(cls, valor) -> str:
        if not isinstance(valor, str) or not valor.strip():
            raise TelefonoInvalidoError("El teléfono no puede estar vacío.")
        v = valor.strip()
        if not cls._RE_TELEFONO.match(v):
            raise TelefonoInvalidoError(f"Teléfono '{v}' inválido. Use 7-15 dígitos, puede iniciar con '+'.")
        return v

    # ── Propiedades (solo lectura) ──────────────────────────────────────────

    @property
    def id_cliente(self): return self.__id_cliente

    @property
    def nombre(self): return self.__nombre

    @property
    def email(self): return self.__email

    @property
    def telefono(self): return self.__telefono

    # ── Setters con validación ──────────────────────────────────────────────

    @nombre.setter
    def nombre(self, v):
        self.__nombre = self._validar_nombre(v)
        logger.info("Nombre actualizado | ID: %s", self.__id_cliente)

    @email.setter
    def email(self, v):
        self.__email = self._validar_email(v)
        logger.info("Email actualizado  | ID: %s", self.__id_cliente)

    @telefono.setter
    def telefono(self, v):
        self.__telefono = self._validar_telefono(v)
        logger.info("Teléfono actualizado | ID: %s", self.__id_cliente)

    # ── Métodos abstractos implementados ────────────────────────────────────

    def describir(self) -> str:
        return (
            f"Cliente[ID={self.__id_cliente} | "
            f"Nombre={self.__nombre} | "
            f"Email={self.__email} | "
            f"Teléfono={self.__telefono}]"
        )

    def obtener_id(self) -> str:
        return self.__id_cliente

    def __repr__(self):
        return (f"Cliente(id_cliente='{self.__id_cliente}', nombre='{self.__nombre}', "
                f"email='{self.__email}', telefono='{self.__telefono}')")

    def __eq__(self, other):
        return isinstance(other, Cliente) and self.__id_cliente == other.id_cliente

    def __hash__(self):
        return hash(self.__id_cliente)

    # ── Utilidad para pruebas ───────────────────────────────────────────────

    @classmethod
    def limpiar_registro_ids(cls):
        """Limpia el registro global de IDs. Solo para pruebas."""
        cls._ids_registrados.clear()