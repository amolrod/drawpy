"""Contendrá funciones básicas de ratón basadas en PyAutoGUI."""

from __future__ import annotations

from typing import Tuple

Point = Tuple[int, int]


def setup() -> None:
    """Configura PyAutoGUI antes de dibujar."""

    raise NotImplementedError("Se añadirá en la fase 2")


def move(position: Point) -> None:
    """Moverá el ratón hasta la posición indicada."""

    raise NotImplementedError("Se añadirá en la fase 2")


def click(position: Point) -> None:
    """Hará clic en la posición recibida."""

    raise NotImplementedError("Se añadirá en la fase 2")
