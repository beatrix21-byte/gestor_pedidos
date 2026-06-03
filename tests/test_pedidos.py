"""Pruebas de la lógica de pedidos."""

import pytest

from pedidos import LineaPedido, Pedido, calcular_descuento, calcular_total_lineas


def test_calcula_subtotal_linea():
    linea = LineaPedido("Teclado", 25.0, 2)
    assert linea.subtotal() == 50.0


def test_calcula_total_lineas():
    lineas = [LineaPedido("Ratón", 10.0, 2), LineaPedido("Monitor", 150.0, 1)]
    assert calcular_total_lineas(lineas) == 170.0


def test_aplica_descuento_del_10_por_ciento():
    assert calcular_descuento(150.0) == 15.0


def test_aplica_descuento_del_15_por_ciento():
    assert calcular_descuento(300.0) == 45.0


def test_total_final_pedido_con_descuento():
    pedido = Pedido("Ana")
    pedido.agregar_linea(LineaPedido("Silla", 100.0, 2))
    assert pedido.total_con_descuento() == 170.0


def test_no_permite_cantidad_cero():
    linea = LineaPedido("Mesa", 80.0, 0)
    with pytest.raises(ValueError):
        linea.subtotal()
