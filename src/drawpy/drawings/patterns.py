"""Patrones complejos listos para usarse como trazos."""

from __future__ import annotations

import math
from typing import List, Sequence, Tuple

from ..traces import Stroke

Point = Tuple[int, int]


def _round_points(points: Sequence[Tuple[float, float]]) -> List[Point]:
    return [(int(round(x)), int(round(y))) for x, y in points]


def zigzag(start: Point, segment_length: int, amplitude: int, segments: int) -> Stroke:
    """Genera un zigzag con la cantidad de segmentos indicada."""

    x, y = start
    points = [(x, y)]
    direction = 1
    for _ in range(segments):
        x += segment_length
        y += amplitude * direction
        points.append((x, y))
        direction *= -1
    return Stroke(points=points, hold_click=True)


def wave(start: Point, width: int, amplitude: int, cycles: int, resolution: int = 30) -> Stroke:
    """Curva sinusoidal basada en el ancho y el número de ciclos."""

    if cycles <= 0:
        raise ValueError("cycles debe ser positivo")

    total_points = cycles * resolution
    points = []
    for i in range(total_points + 1):
        progress = i / total_points
        x = start[0] + width * progress
        angle = progress * cycles * 2 * math.pi
        y = start[1] + math.sin(angle) * amplitude
        points.append((x, y))
    return Stroke(points=_round_points(points), hold_click=True)


def star(center: Point, radius: int, tips: int = 5) -> Stroke:
    """Estrella clásica alternando radios largo/corto."""

    if tips < 3:
        raise ValueError("tips debe ser al menos 3")

    cx, cy = center
    points = []
    inner_radius = radius * 0.45
    total_points = tips * 2
    for i in range(total_points):
        angle = (math.pi / tips) * i - math.pi / 2  # comienza hacia arriba
        r = radius if i % 2 == 0 else inner_radius
        x = cx + math.cos(angle) * r
        y = cy + math.sin(angle) * r
        points.append((x, y))
    points.append(points[0])
    return Stroke(points=_round_points(points), hold_click=True)


def spiral(center: Point, turns: float, step: float, samples_per_turn: int = 40) -> Stroke:
    """Traza una espiral que se expande desde el centro."""

    if turns <= 0 or step <= 0:
        raise ValueError("turns y step deben ser positivos")

    cx, cy = center
    total_samples = int(turns * samples_per_turn)
    points = []
    for i in range(total_samples + 1):
        progress = i / samples_per_turn
        angle = 2 * math.pi * progress
        radius = step * progress
        x = cx + math.cos(angle) * radius
        y = cy + math.sin(angle) * radius
        points.append((x, y))
    return Stroke(points=_round_points(points), hold_click=True)
