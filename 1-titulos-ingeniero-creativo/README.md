# 🖼️ Generador de Imágenes con Texto Estilizado

Este script en Python permite generar imágenes `.png` con texto personalizado utilizando una fuente específica. Esta preparado para las necesidades de Ingeniero Creativo, por lo que los casos de uso que cubre son limitados y, por tanto, no es una herramienta preparada para un uso comercial.

¿Y si te lo preguntabas...?

1) Sí, utilicé ChatGPT para hacerlo lo más rápido posible y no comerme mucho el coco, con algún ajuste manual.
2) El código no está completamente optimizado, y se puede mejorar.

## 🚀 Requisitos

- Python 3.7 o superior
- [Pillow](https://python-pillow.org/) (biblioteca de manipulación de imágenes)

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

## 🎛️ Parámetros disponibles

| Parámetro             | Descripción                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `-t`, `--text`        | Texto directo a renderizar.                                                 |
| `-f`, `--file`        | Ruta a un fichero `.txt` desde el que se procesarán multiples líneas [NO TESTEADO]                                                                                             |
| `-o`, `--output`      | Carpeta de salida donde se guardará la imagen. Por defecto: `./output`.     |
| `--filename`          | Nombre del archivo de salida. Por defecto: `output.png`.                    |
| `-s`, `--size`        | Tamaño de la fuente. Valor por defecto: `100`.                              |
| `-p`, `--padding`     | Espaciado interno alrededor del texto. Por defecto: `50`.                   |
| `--font`              | Ruta absoluta al archivo `.otf` o `.ttf` de la fuente.                      |
| `--text-color`        | Color del texto en formato hexadecimal (ej: `#000000`).                     |
| `--border-color`      | Color del borde del texto. Solo se usa si se activa `--borde`.              |
| `--ellipse-color`     | Color de fondo si se usa la opción `--elipse`.                              |
| `--ellipse-height-scale` | Multiplicador de la altura de la cápsula respecto al texto (ej: `0.6`). |
| `--borde`             | Activa el borde alrededor del texto. Incompatible con `--elipse`.           |
| `--elipse`            | Dibuja un fondo con forma de cápsula elíptica. Incompatible con `--borde`.  |

## Ejemplos de uso

Estos son los tres tipos de texto que genero para mis presentaciones.

### Título presentación

```bash
    python script.py -t "Presentación" --text-color="#000000" --borde --border-color="#facc15" --filename presentacion.png --border-width 5
```

### Título presentación multilinea

```bash
python script.py -t $'Presentación\n\nMulti\nLínea' --text-color="#000000" --borde --border-color="#facc15" --filename presentacion.png --border-width 5
```

### Título Diapositiva (elipse)

```bash
    python script.py -t "Introducción" --elipse --ellipse-color "#000" --ellipse-height-scale 0.5 --text-color "#facc15"
```
