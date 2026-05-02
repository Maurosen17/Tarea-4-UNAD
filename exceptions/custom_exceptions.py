# exceptions/custom_exceptions.py

class SistemaError(Exception):
    """
    Excepción base del sistema.
    """
    pass


class ClienteError(SistemaError):
    """
    Errores relacionados con clientes.
    """
    pass


class ServicioError(SistemaError):
    """
    Errores relacionados con servicios.
    """
    pass


class ReservaError(SistemaError):
    """
    Errores relacionados con reservas.
    """
    pass