import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor

def crear_imagen(frase, fuente_path, output_path, salida="output.png", size=100, padding=50,
                 text_color="#000000", border_color="#facc15", ellipse_color="#ffffff",
                 borde=False, border_width=1, ellipse_background=False, ellipse_height_scale=1.0):
    
    fuente = ImageFont.truetype(fuente_path, size)
    lineas = frase.splitlines()

    dummy_img = Image.new("RGBA", (1, 1))
    draw_dummy = ImageDraw.Draw(dummy_img)

    ascent, descent = fuente.getmetrics()
    line_height = ascent + descent
    alto_texto_total = line_height * len(lineas)

    ancho_max = max(draw_dummy.textbbox((0, 0), linea, font=fuente)[2] for linea in lineas)

    # Ancho automático + padding
    ancho_img = ancho_max + 2 * padding
    alto_img = int((alto_texto_total * ellipse_height_scale) + 2 * padding)

    imagen = Image.new("RGBA", (ancho_img, alto_img), (0, 0, 0, 0))
    draw = ImageDraw.Draw(imagen)

    if ellipse_background:
        try:
            fill_color = ImageColor.getcolor(ellipse_color, "RGBA")
        except:
            fill_color = (255, 255, 255, 180)
        draw.ellipse([0, 0, ancho_img, alto_img], fill=fill_color)

    # Centrado vertical real
    y = (alto_img - alto_texto_total) // 2
    for linea in lineas:
        bbox = draw.textbbox((0, 0), linea, font=fuente)
        ancho_linea = bbox[2] - bbox[0]
        x = (ancho_img - ancho_linea) // 2

        if borde:
            for dx in range(-border_width, border_width + 1):
                for dy in range(-border_width, border_width + 1):
                    if dx != 0 or dy != 0:
                        draw.text((x + dx, y + dy), linea, font=fuente, fill=border_color)

        draw.text((x, y), linea, font=fuente, fill=text_color)
        y += line_height

    os.makedirs(output_path, exist_ok=True)
    ruta_salida = os.path.join(output_path, salida)
    imagen.save(ruta_salida)
    print(f"✅ Imagen guardada en: {ruta_salida}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generador de imágenes con texto estilizado.")
    parser.add_argument("-f", "--file", type=str, help="Ruta al fichero con el texto", required=False)
    parser.add_argument("-t", "--text", type=str, help="Texto directo a renderizar", required=False)
    parser.add_argument("-o", "--output", type=str, default="./output", help="Ruta de salida")
    parser.add_argument("--filename", type=str, default="output.png", help="Nombre del archivo de salida")
    parser.add_argument("-s", "--size", type=int, default=100, help="Tamaño de fuente")
    parser.add_argument("-p", "--padding", type=int, default=50, help="Padding alrededor del texto")
    parser.add_argument("--font", type=str, default=os.path.abspath("../assets/fonts/Palamecia-Titling.otf"), help="Ruta absoluta a la fuente")
    parser.add_argument("--text-color", type=str, default="#facc15", help="Color del texto")
    parser.add_argument("--border-color", type=str, default="#000000", help="Color del borde del texto")
    parser.add_argument("--border-width", type=int, default=2, help="Grosor del borde del texto")
    parser.add_argument("--ellipse-color", type=str, default="#ffffff", help="Color de fondo de la elipse")
    parser.add_argument("--ellipse-height-scale", type=float, default=1.0, help="Multiplicador de la altura de la elipse")
    parser.add_argument("--borde", action="store_true", help="Usar borde en el texto")
    parser.add_argument("--elipse", action="store_true", help="Usar fondo tipo cápsula elíptica")

    args = parser.parse_args()

    if args.borde and args.elipse:
        parser.error("❌ No puedes usar borde y fondo de elipse al mismo tiempo.")

    if args.file:
        with open(args.file, encoding="utf-8") as f:
            i=0
            for texto in f:
                i=i+1
                crear_imagen(
                    frase=texto,
                    fuente_path=os.path.abspath(args.font),
                    output_path=args.output,
                    salida=args.filename+"_"+str(i),
                    size=args.size,
                    padding=args.padding,
                    text_color=args.text_color,
                    border_color=args.border_color,
                    ellipse_color=args.ellipse_color,
                    borde=args.borde,
                    border_width=args.border_width,
                    ellipse_background=args.elipse,
                    ellipse_height_scale=args.ellipse_height_scale
                )
    elif args.text:
        texto = args.text
        
        crear_imagen(
                frase=texto,
                fuente_path=os.path.abspath(args.font),
                output_path=args.output,
                salida=args.filename,
                size=args.size,
                padding=args.padding,
                text_color=args.text_color,
                border_color=args.border_color,
                ellipse_color=args.ellipse_color,
                borde=args.borde,
                border_width=args.border_width,
                ellipse_background=args.elipse,
                ellipse_height_scale=args.ellipse_height_scale
            )
    else:
        parser.error("❌ Debes proporcionar un texto con -t o un archivo con -f")


