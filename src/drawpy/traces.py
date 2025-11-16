"""Clases reutilizables para gestionar trazos simples."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence, Tuple

Point = Tuple[int, int]


@dataclass
class Stroke:
    points: Sequence[Point]
    hold_click: bool = False


class StrokeManager:
    """Agrupa y ejecuta trazos."""

    def __init__(self) -> None:
        self._strokes: List[Stroke] = []

    def add(self, stroke: Stroke) -> None:
        self._strokes.append(stroke)

    def clear(self) -> None:
        self._strokes.clear()

    def run(self) -> None:
        raise NotImplementedError("La lógica se implementará en fases posteriores")
