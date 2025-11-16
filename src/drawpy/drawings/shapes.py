"""Figuras básicas basadas en líneas."""

from __future__ import annotations

from typing import Tuple

from ..traces import Stroke

Point = Tuple[int, int]


def rectangle(top_left: Point, width: int, height: int) -> Stroke:
    raise NotImplementedError("Se completará en la fase 4")
