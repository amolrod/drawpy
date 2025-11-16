"""Punto de entrada del módulo."""

from __future__ import annotations

from typing import Iterable

from .traces import Stroke, StrokeManager


def run(strokes: Iterable[Stroke], countdown: float = 3.0) -> None:
    """Ejecuta los trazos en orden."""

    manager = StrokeManager(countdown=countdown)
    manager.extend(strokes)
    manager.run()
