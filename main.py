from __future__ import annotations

"""CLI principal para ejecutar ejemplos de drawpy."""

from typing import List

from src.drawpy import app
from src.drawpy.drawings import lines
from src.drawpy.traces import Stroke


def main() -> None:
    """Ejemplo básico: dibuja una línea simple."""

    strokes: List[Stroke] = [
        lines.line((400, 300), (600, 300)),
    ]
    app.run(strokes)


if __name__ == "__main__":
    main()
