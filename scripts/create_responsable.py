# Script para crear un responsable de entrega desde línea de comandos
# Uso: python scripts/create_responsable.py <id_responsable> "<nombre>" <correo> <empresa_id>
from app import SessionLocal
from models import ResponsableEntrega, EmpresaExterna
import sys


def main():
    if len(sys.argv) < 5:
        print("Uso: python scripts/create_responsable.py <id_responsable> \"<nombre>\" <correo> <empresa_id>")
        return

    id_res = sys.argv[1].strip()
    nombre = sys.argv[2].strip()
    correo = sys.argv[3].strip()
    try:
        empresa_id = int(sys.argv[4])
    except ValueError:
        print("<empresa_id> debe ser un entero (id de la empresa).")
        return

    db = SessionLocal()
    try:
        # Verificar que la empresa exista
        emp = db.get(EmpresaExterna, empresa_id)
        if not emp:
            print(f"Empresa con id={empresa_id} no encontrada. Crea la empresa primero.")
            return

        # Verificar unicidad de id_responsable
        exists = db.query(ResponsableEntrega).filter(ResponsableEntrega.id_responsable == id_res).first()
        if exists:
            print(f"Ya existe un responsable con id_responsable='{id_res}' (id={exists.id}, nombre={exists.nombre_responsable}).")
            return

        r = ResponsableEntrega(
            id_responsable=id_res,
            nombre_responsable=nombre,
            correo_responsable=correo,
            empresa_id=empresa_id,
        )
        db.add(r)
        db.commit()
        print(f"Responsable creado: id={r.id}, id_responsable={r.id_responsable}, nombre={r.nombre_responsable}, empresa_id={r.empresa_id} ({emp.nombre})")
    except Exception as e:
        db.rollback()
        print("Error al crear responsable:", e)
    finally:
        db.close()


if __name__ == '__main__':
    main()
