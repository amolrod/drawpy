from __future__ import annotations

"""CLI principal para ejecutar ejemplos de drawpy."""

import argparse
from typing import List

from src.drawpy import app
from src.drawpy.drawings import lines, patterns, shapes
from src.drawpy.traces import Stroke


def build_demo(name: str, args: argparse.Namespace) -> List[Stroke]:
    """Devuelve trazos predefinidos según el demo elegido."""

    origin = (args.origin_x, args.origin_y)

    if name == "line":
        end = (origin[0] + args.width, origin[1])
        return [lines.line(origin, end)]
    if name == "rectangle":
        return [shapes.rectangle(origin, args.width, args.height)]
    if name == "square":
        return [shapes.square(origin, args.size)]
    if name == "zigzag":
        segment = max(5, args.width // max(1, args.segments))
        return [patterns.zigzag(origin, segment, args.amplitude, args.segments)]
    if name == "wave":
        return [patterns.wave(origin, args.width, args.amplitude, args.cycles)]
    if name == "star":
        center = origin
        return [patterns.star(center, args.size, tips=args.tips)]
    if name == "spiral":
        center = origin
        return [patterns.spiral(center, args.turns, step=args.step)]
    raise ValueError(f"Demo desconocido: {name}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ejecuta demos de dibujo para Instagram.")
    parser.add_argument(
        "--demo",
        default="line",
        choices=["line", "rectangle", "square", "zigzag", "wave", "star", "spiral"],
        help="Tipo de trazo a ejecutar",
    )
    parser.add_argument(
        "--countdown",
        type=float,
        default=3.0,
        help="Tiempo de espera antes de comenzar.",
    )
    parser.add_argument("--origin-x", type=int, default=400, help="Coordenada X de inicio.")
    parser.add_argument("--origin-y", type=int, default=300, help="Coordenada Y de inicio.")
    parser.add_argument("--width", type=int, default=220, help="Ancho base para rectángulos/ondas.")
    parser.add_argument("--height", type=int, default=120, help="Alto base del rectángulo.")
    parser.add_argument("--size", type=int, default=150, help="Tamaño base para cuadrados/estrellas.")
    parser.add_argument("--segments", type=int, default=8, help="Segmentos del zigzag.")
    parser.add_argument("--amplitude", type=int, default=60, help="Amplitud vertical para zigzag/onda.")
    parser.add_argument("--cycles", type=int, default=3, help="Ciclos de la onda.")
    parser.add_argument("--tips", type=int, default=5, help="Puntas de la estrella.")
    parser.add_argument("--turns", type=float, default=3.0, help="Vueltas de la espiral.")
    parser.add_argument("--step", type=float, default=12.0, help="Separación incremental de la espiral.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    strokes = build_demo(args.demo, args)
    app.run(strokes, countdown=args.countdown)


if __name__ == "__main__":
    main()
