# script para listar empresas y responsables
from app import SessionLocal
from models import ResponsableEntrega, EmpresaExterna

def main():
    db = SessionLocal()
    try:
        empresas = {e.id: e.nombre for e in db.query(EmpresaExterna).all()}
        responsables = db.query(ResponsableEntrega).order_by(ResponsableEntrega.empresa_id, ResponsableEntrega.nombre_responsable).all()

        print("Empresas registradas:")
        if not empresas:
            print("  (ninguna)")
        else:
            for eid, name in empresas.items():
                print(f"  {eid}: {name}")

        print('\nResponsables registrados:')
        if not responsables:
            print("  (ninguno)")
        else:
            for r in responsables:
                emp_name = empresas.get(r.empresa_id, '(empresa no encontrada)')
                print(f"  id={r.id} | id_responsable={r.id_responsable} | nombre={r.nombre_responsable} | empresa_id={r.empresa_id} ({emp_name})")

        # Conteo por empresa
        print('\nConteo de responsables por empresa:')
        counts = {}
        for r in responsables:
            counts[r.empresa_id] = counts.get(r.empresa_id, 0) + 1
        if not counts:
            print('  (ninguno)')
        else:
            for eid, cnt in counts.items():
                print(f"  Empresa {eid} ({empresas.get(eid,'?')}): {cnt}")

    finally:
        db.close()

if __name__ == '__main__':
    main()
