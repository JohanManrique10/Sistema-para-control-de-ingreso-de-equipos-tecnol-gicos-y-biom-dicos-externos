# Crear entorno y acceder
- crear el entorno
python -m venv .venv

- acceder al entorno
.venv\Scripts\Activate.ps1   

# Instalar dependencias
pip install -r requirements.txt

# Actualizar el pip install*
python.exe -m pip install --upgrade pip

# Este no es necesario si no hay nuevas dependecias 
pip freeze > requirements.txt

# Copiar las carpetas con los archivos de la estructura base del proyecto

# ---------------- Truncar las tablas
TRUNCATE TABLE user_audit, user_deletions, auth_throttle,... users RESTART IDENTITY CASCADE;


# ################################### 13 DE NOVIEMBRE #############################################

- PARTE 1: INSTALACIONES PREVIAS __________________________________________________________________
    1.) Crear entorno y acceder
    - crear el entorno
    python -m venv .venv

    - acceder al entorno
    .venv\Scripts\Activate.ps1


    2.) Instalar dependencias 
    - pip install -r requirements.txt
  
    3.) Iniciar el proyecto
    - py app.py

- PARTE 2 LOS SEED _______________________________________________________________________________

# Orden para los seed

# 1. Empresas
python seed_empresas_extern.py

# 2. Responsables
python seed_resp_ent_empresa.py

# 3. crear al usario admin y desde el FE (UI/UX) crear un usuario de rol user
3.1) python manage.py
3.2) py app.py
3.2.1) http://127.0.0.1:8095/usuarios/crear


# 4. Tener por lo menos 1 usuario con rol "usuario"
# crear Equipos
python seed_equipos.py
