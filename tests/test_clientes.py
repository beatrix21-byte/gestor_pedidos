"""Pruebas de validación de clientes."""

from clientes import Cliente, validar_email, validar_nombre


def test_cliente_valido():
    cliente = Cliente("Laura Pérez", "laura@example.com", "600111222")
    assert cliente.es_valido() is True


def test_cliente_con_email_invalido():
    cliente = Cliente("Laura Pérez", "correo-mal")
    assert cliente.es_valido() is False


def test_validar_nombre_rechaza_vacio():
    assert validar_nombre(" ") is False


def test_validar_email_correcto():
    assert validar_email("alumno@instituto.es") is True
