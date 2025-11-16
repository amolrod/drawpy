"""Punto de entrada del módulo."""

from __future__ import annotations

from typing import Iterable

from .traces import Stroke, StrokeManager


def run(strokes: Iterable[Stroke]) -> None:
    """Ejecuta los trazos en orden."""

    manager = StrokeManager()
    for stroke in strokes:
        manager.add(stroke)
    manager.run()
