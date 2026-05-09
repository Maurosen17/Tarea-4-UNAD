"""
exceptions/cliente_exceptions.py
Jerarquía de excepciones personalizadas para el módulo Cliente.
"""


class SoftwareFJError(Exception):
    """Raíz de todos los errores del sistema Software FJ."""
    pass


class ClienteError(SoftwareFJError):
    """Raíz de errores relacionados con Cliente."""
    pass


class NombreInvalidoError(ClienteError):
    pass


class EmailInvalidoError(ClienteError):
    pass


class TelefonoInvalidoError(ClienteError):
    pass


class IDClienteInvalidoError(ClienteError):
    pass