# drawpy

Automatiza trazos simples del ratón con PyAutoGUI para dibujar en la herramienta de dibujo de los chats de Instagram (web o app de escritorio). El objetivo es contar con un flujo reproducible para practicar y generar formas sencillas directamente en la pantalla.

## Requisitos
- Python 3.10 o superior.
- macOS o Windows con acceso a la app / web de Instagram.
- PyAutoGUI (se instala vía `requirements.txt`).

## Instalación rápida
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Uso paso a paso
1. Abre Instagram Web o la app de escritorio, entra a un chat y activa la herramienta de dibujo.
2. Ajusta la pluma y el color dentro de Instagram (el script solo mueve el ratón).
3. Ubica las coordenadas aproximadas de tu lienzo. El ejemplo por defecto usa valores centrados en 400-600 px.
4. Ejecuta alguno de los demos disponibles:
   ```bash
   python main.py --demo line       # Línea horizontal básica
   python main.py --demo rectangle  # Rectángulo
   python main.py --demo square     # Cuadrado
   python main.py --demo zigzag     # Zigzag continuo
   python main.py --demo wave       # Curva sinusoidal
   python main.py --demo star       # Estrella de 5 puntas
   python main.py --demo spiral     # Espiral abierta
   python main.py --demo line --countdown 5  # Añade margen antes de iniciar
   ```
5. Una vez que aparezca el mensaje "Comenzando en ...", sitúa el cursor sobre el lienzo. El programa tomará control tras finalizar la cuenta regresiva.

> **Nota:** PyAutoGUI trae la función de failsafe activada. Si necesitas abortar, mueve el ratón rápidamente a la esquina superior izquierda de la pantalla.

## Estructura del proyecto
```
src/drawpy/
├── app.py             # Orquesta los trazos y los ejecuta
├── mouse.py           # Movimientos y clics seguros
├── traces.py          # Modelo Stroke y administrador de secuencias
└── drawings/
    ├── lines.py       # Generadores de líneas
    ├── shapes.py      # Figuras basadas en líneas
    └── patterns.py    # Zigzag, ondas, estrellas y espirales
```

## Ejemplo de código
```python
from src.drawpy import app
from src.drawpy.drawings import lines, patterns, shapes

# Línea en diagonal
line = lines.line((350, 400), (600, 200))

# Estrella en el centro del lienzo
star = patterns.star((500, 400), radius=140, tips=6)

# Espiral para rematar el dibujo
spiral = patterns.spiral((600, 450), turns=4, step=14)

app.run([line, star, spiral], countdown=4)
```
Los generadores devuelven instancias de `Stroke`, lo que permite componer listas con diferentes tipos de trazos.

### Parámetros útiles desde la CLI
- `--origin-x / --origin-y`: Coloca el origen del dibujo.
- `--width` / `--height`: Ajustan el tamaño de rectángulos, ondas y líneas horizontales.
- `--size`: Se usa como base para cuadrados y estrellas.
- `--segments`, `--amplitude`, `--cycles`: Controlan la forma de zigzags y ondas.
- `--turns`, `--step`: Definen la apertura de la espiral.

## FAQ
**¿Qué pasa si mis coordenadas no coinciden con el lienzo?**
Ajusta las posiciones en `main.py` o crea tus propios trazos llamando a las funciones de `drawings.lines` y `drawings.shapes`. Se recomienda capturar la posición con `pyautogui.position()` desde una consola interactiva.

**¿Puedo cambiar la velocidad del puntero?**
Sí. Modifica `MouseConfig` en `src/drawpy/mouse.py` para reducir `move_duration` o `click_pause`.

**¿Funciona fuera de Instagram?**
Sí. El script solo mueve el ratón, así que puedes dibujar en cualquier lienzo compatible.

**¿Es seguro ejecutar el script?**
PyAutoGUI usa `FAILSAFE=True` por defecto. Adicionalmente, se añade un conteo regresivo configurable antes de iniciar.

**¿Cómo consigo figuras más complejas?**
Usa el parámetro `--demo` con valores como `zigzag`, `wave`, `star` o `spiral` y ajusta los argumentos opcionales (`--segments`, `--amplitude`, `--tips`, `--turns`, etc.) para experimentar con diferentes estilos.

## Ideas futuras
- Lectura de trayectorias desde archivos SVG simples.
- Sistema de plantillas para definir letras o iconos.
- Vista previa por consola mostrando los puntos antes de ejecutar.
- Integración con atajos de teclado para lanzar diferentes trazos sin modificar el código.
