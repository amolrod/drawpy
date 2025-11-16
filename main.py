from __future__ import annotations

"""CLI principal para ejecutar ejemplos de drawpy."""

import argparse
from typing import List

from src.drawpy import app
from src.drawpy.drawings import lines, shapes
from src.drawpy.traces import Stroke


def build_demo(name: str) -> List[Stroke]:
    """Devuelve trazos predefinidos según el demo elegido."""

    if name == "line":
        return [lines.line((400, 300), (600, 300))]
    if name == "rectangle":
        return [shapes.rectangle((400, 300), 200, 120)]
    if name == "square":
        return [shapes.square((450, 350), 120)]
    raise ValueError(f"Demo desconocido: {name}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ejecuta demos de dibujo para Instagram.")
    parser.add_argument(
        "--demo",
        default="line",
        choices=["line", "rectangle", "square"],
        help="Tipo de trazo a ejecutar",
    )
    parser.add_argument(
        "--countdown",
        type=float,
        default=3.0,
        help="Tiempo de espera antes de comenzar.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    strokes = build_demo(args.demo)
    app.run(strokes, countdown=args.countdown)


if __name__ == "__main__":
    main()
