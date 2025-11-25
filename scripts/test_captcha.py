
from flask import Flask
import os
import sys
# Asegurar que el directorio del proyecto está en sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from captcha_app import captcha_bp

app = Flask(__name__)
app.secret_key = os.urandom(16)
app.register_blueprint(captcha_bp, url_prefix="/captcha")

if __name__ == '__main__':
    # Usar test_client para pedir la imagen y guardarla localmente
    with app.test_client() as c:
        resp = c.get('/captcha/image.png')
        if resp.status_code == 200 and resp.mimetype == 'image/png':
            out = 'captcha_test_output.png'
            with open(out, 'wb') as f:
                f.write(resp.data)
            print(f'OK - imagen guardada en {out} ({len(resp.data)} bytes)')
        else:
            print('ERROR: respuesta inesperada', resp.status_code, resp.mimetype)
