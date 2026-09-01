#!/usr/bin/env python3
"""Cabecalho do README de perfil do GitHub — Acacio Lima Rocha.

Regrava assets/header.png. Rode de dentro da pasta do repositorio:

    python gerar-header.py

Requer Pillow:  pip install pillow
As fontes Poppins sao procuradas no sistema; sem elas cai no DejaVu.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1280, 340
BG    = (7, 9, 13)
FG    = (240, 245, 250)
MUT   = (146, 163, 181)
BRAND = (255, 138, 76)
CYAN  = (46, 216, 195)
AQUI = os.path.dirname(os.path.abspath(__file__))
def fonte(nome, tam):
    """Procura Poppins no sistema; se nao achar, usa DejaVu."""
    for base in ("/usr/share/fonts/truetype/google-fonts/",
                 "C:/Windows/Fonts/", os.path.join(AQUI, "fontes")):
        p = os.path.join(base, nome)
        if os.path.exists(p):
            return ImageFont.truetype(p, tam)
    for base in ("/usr/share/fonts/truetype/dejavu/", "C:/Windows/Fonts/"):
        for alt in ("DejaVuSans-Bold.ttf", "arialbd.ttf", "arial.ttf"):
            p = os.path.join(base, alt)
            if os.path.exists(p):
                return ImageFont.truetype(p, tam)
    return ImageFont.load_default()
f_nome  = fonte("Poppins-Bold.ttf", 62)
f_role  = fonte("Poppins-Medium.ttf", 27)
f_sub   = fonte("Poppins-Light.ttf", 21)
f_eye   = fonte("Poppins-Medium.ttf", 15)

im = Image.new("RGB", (W, H), BG)
glow = Image.new("RGB", (W, H), BG)
g = ImageDraw.Draw(glow)
g.ellipse((-320, -300, 700, 420), fill=(78, 36, 18))
g.ellipse((900, -180, 1560, 300), fill=(9, 48, 46))
im = Image.blend(im, glow.filter(ImageFilter.GaussianBlur(140)), 0.88)

grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gg = ImageDraw.Draw(grid)
for x in range(0, W, 44): gg.line([(x, 0), (x, H)], fill=(255, 255, 255, 9))
for y in range(0, H, 44): gg.line([(0, y), (W, y)], fill=(255, 255, 255, 9))
im = Image.alpha_composite(im.convert("RGBA"), grid).convert("RGB")

d = ImageDraw.Draw(im)
X = 76
d.line([(X, 96), (X, 262)], fill=BRAND, width=4)
x = X + 30
# olho: letras espacadas
eyebrow = "S E N I O R   D A T A B A S E   A D M I N I S T R A T O R"
d.text((x, 92), eyebrow, font=f_eye, fill=BRAND)
d.text((x, 122), "Acácio Lima Rocha", font=f_nome, fill=FG)
d.text((x, 202), "Oracle · MySQL · SQL Server · PostgreSQL", font=f_role, fill=MUT)
d.text((x, 240), "12+ anos em ambientes críticos de produção", font=f_sub, fill=(110, 128, 146))

# lado direito: a credencial mais forte, com halo
ace = Image.open(os.path.join(AQUI, "assets", "badges", "ace-associate.png")).convert("RGBA")
ace.thumbnail((186, 186), Image.LANCZOS)
halo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(halo).ellipse((W-330, 62, W-102, 290), fill=(255, 138, 76, 46))
im = Image.alpha_composite(im.convert("RGBA"), halo.filter(ImageFilter.GaussianBlur(46)))
bx = W - 322 + (228 - ace.width)//2
by = 62 + (228 - ace.height)//2
im.paste(ace, (bx, by), ace)
im = im.convert("RGB")
d = ImageDraw.Draw(im)  # a propria badge ja traz o nome — sem legenda redundante

SAIDA = os.path.join(AQUI, "assets", "header.png")
im.save(SAIDA, "PNG", optimize=True)
print("gravado:", SAIDA, im.size)
