from flask import Blueprint, render_template, session, request, send_file, flash
import random
import string
import io
import time
from PIL import Image, ImageDraw, ImageFont, ImageFilter

captcha_bp = Blueprint("captcha", __name__)


def _random_text(n=5):
    chars = string.ascii_uppercase + string.digits
    return "".join(random.choices(chars, k=n))


@captcha_bp.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        val = (request.form.get("captcha") or "").strip()
        expected = session.get("captcha_text")
        if not expected or val.lower() != expected.lower():
            flash("Captcha incorrecto.", "danger")
        else:
            flash("Captcha válido.", "success")
    # ts for cache busting of the image
    return render_template("captcha/index.html", ts=int(time.time()))


@captcha_bp.route("/image.png")
def image():
    # Genera texto y lo guarda en session
    text = _random_text(5)
    session["captcha_text"] = text

    width, height = 160, 60
    img = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Font: intenta cargar una TTF común, si no, usa la por defecto
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except Exception:
        font = ImageFont.load_default()

    # Ruido de puntos
    for _ in range(120):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=(random.randint(150, 220), random.randint(150, 220), random.randint(150, 220)))

    # Dibujar cada carácter con pequeñas variaciones
    for i, ch in enumerate(text):
        x = 10 + i * 28 + random.randint(-3, 3)
        y = random.randint(0, 12)
        draw.text((x, y), ch, font=font, fill=(random.randint(0, 80), random.randint(0, 80), random.randint(0, 80)))

    img = img.filter(ImageFilter.SMOOTH)

    bio = io.BytesIO()
    img.save(bio, format="PNG")
    bio.seek(0)
    return send_file(bio, mimetype="image/png")
