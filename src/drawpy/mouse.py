"""Funciones básicas de ratón basadas en PyAutoGUI."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Tuple

import pyautogui

Point = Tuple[int, int]


@dataclass
class MouseConfig:
    """Parámetros simples para mover y pulsar."""

    move_duration: float = 0.2
    click_pause: float = 0.1


config = MouseConfig()


def pause(seconds: float | None = None) -> None:
    """Pausa corta usada entre acciones."""

    time.sleep(seconds if seconds is not None else config.click_pause)


def setup() -> None:
    """Configura PyAutoGUI antes de dibujar."""

    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = config.click_pause


def move(position: Point, duration: float | None = None) -> None:
    """Mueve el ratón hasta la posición indicada."""

    x, y = position
    pyautogui.moveTo(x, y, duration=duration or config.move_duration)


def click(position: Point) -> None:
    """Hace clic izquierdo en la posición recibida."""

    move(position)
    pyautogui.click()
    pause()


def move_and_click(position: Point, duration: float | None = None) -> None:
    """Lleva el puntero a la posición dada y hace clic."""

    move(position, duration=duration)
    pyautogui.click()
    pause()
