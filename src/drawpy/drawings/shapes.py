"""Figuras básicas basadas en líneas."""

from __future__ import annotations

from typing import Tuple

from ..traces import Stroke

Point = Tuple[int, int]


def rectangle(top_left: Point, width: int, height: int, close: bool = True) -> Stroke:
    """Traza el contorno de un rectángulo."""

    x, y = top_left
    points = [
        (x, y),
        (x + width, y),
        (x + width, y + height),
        (x, y + height),
    ]
    if close:
        points.append((x, y))
    return Stroke(points=points, hold_click=True)


def square(top_left: Point, size: int, close: bool = True) -> Stroke:
    """Cuadrado auxiliar usando rectangle."""

    return rectangle(top_left, size, size, close=close)
