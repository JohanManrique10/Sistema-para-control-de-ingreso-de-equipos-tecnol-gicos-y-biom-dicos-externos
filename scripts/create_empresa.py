# Script para crear una empresa externa desde línea de comandos
# Uso: python scripts/create_empresa.py <identificacion> "<nombre>"
from app import SessionLocal
from models import EmpresaExterna
import sys

def main():
    if len(sys.argv) < 3:
        print("Uso: python scripts/create_empresa.py <identificacion> \"<nombre>\"")
        return

    ident = sys.argv[1].strip()
    nombre = sys.argv[2].strip()

    db = SessionLocal()
    try:
        # Verificar unicidad
        exists = db.query(EmpresaExterna).filter(EmpresaExterna.identificacion == ident).first()
        if exists:
            print(f"Ya existe una empresa con identificación '{ident}' (id={exists.id}, nombre={exists.nombre}).")
            return

        emp = EmpresaExterna(identificacion=ident, nombre=nombre)
        db.add(emp)
        db.commit()
        print(f"Empresa creada: id={emp.id}, identificacion={emp.identificacion}, nombre={emp.nombre}")
    except Exception as e:
        db.rollback()
        print("Error al crear la empresa:", e)
    finally:
        db.close()

if __name__ == '__main__':
    main()
