"""Generadores de líneas simples."""

from __future__ import annotations

from typing import Tuple

from ..traces import Stroke

Point = Tuple[int, int]


def horizontal(start: Point, length: int) -> Stroke:
    """Línea horizontal desde start con la longitud dada."""

    end_x = start[0] + length
    return Stroke(points=[start, (end_x, start[1])], hold_click=True)


def vertical(start: Point, length: int) -> Stroke:
    """Línea vertical desde start con la longitud dada."""

    end_y = start[1] + length
    return Stroke(points=[start, (start[0], end_y)], hold_click=True)


def line(start: Point, end: Point) -> Stroke:
    """Línea directa entre dos puntos."""

    return Stroke(points=[start, end], hold_click=True)
