from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def criar_imagem(texto, i):
    img = Image.new('RGB', (1080, 1080), color=(30, 0, 50))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 48)
    except:
        font = ImageFont.load_default()

    linhas = textwrap.wrap(texto, width=20)

    y = 200
    for linha in linhas:
        draw.text((100, y), linha, fill="pink", font=font)
        y += 60

    os.makedirs("posts", exist_ok=True)
    img.save(f"posts/post_{i}.png")
