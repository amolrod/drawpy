"""Clases reutilizables para gestionar trazos simples."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple

import pyautogui

from . import mouse

Point = Tuple[int, int]


@dataclass
class Stroke:
    points: Sequence[Point]
    hold_click: bool = False


class StrokeManager:
    """Agrupa y ejecuta trazos."""

    def __init__(self, countdown: float = 3.0) -> None:
        self._strokes: List[Stroke] = []
        self.countdown = countdown

    def add(self, stroke: Stroke) -> None:
        self._strokes.append(stroke)

    def clear(self) -> None:
        self._strokes.clear()

    def extend(self, strokes: Iterable[Stroke]) -> None:
        for stroke in strokes:
            self.add(stroke)

    def run(self) -> None:
        """Ejecuta todos los trazos registrados."""

        if not self._strokes:
            print("No hay trazos para ejecutar.")
            return

        mouse.setup()
        self._countdown()

        for stroke in self._strokes:
            self._run_stroke(stroke)

    def _countdown(self) -> None:
        if self.countdown <= 0:
            return

        print(f"Comenzando en {self.countdown:.1f} segundos...")
        time.sleep(self.countdown)

    def _run_stroke(self, stroke: Stroke) -> None:
        points = list(stroke.points)
        if not points:
            return

        start = points[0]
        mouse.move(start)

        if stroke.hold_click:
            pyautogui.mouseDown()
            for point in points[1:]:
                mouse.move(point)
            pyautogui.mouseUp()
            mouse.pause()
        else:
            mouse.click(start)
            for point in points[1:]:
                mouse.move_and_click(point)
