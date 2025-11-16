"""Generadores de líneas simples."""

from __future__ import annotations

from typing import Tuple

from ..traces import Stroke

Point = Tuple[int, int]


def horizontal(start: Point, length: int) -> Stroke:
    raise NotImplementedError("Se completará en la fase 3")


def vertical(start: Point, length: int) -> Stroke:
    raise NotImplementedError("Se completará en la fase 3")
