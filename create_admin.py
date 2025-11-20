from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

load_dotenv()
database_url = os.getenv("DATABASE_URL")

engine = create_engine(
    database_url,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"} if database_url.startswith("postgresql") else {},
)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
db = Session()

try:
    # Crear usuario admin por defecto
    user = User(
        username="admin",
        email="admin@usta.edu.co",
        identificacion="123456789",
        role="admin"
    )
    user.set_password("admin123")
    db.add(user)
    db.commit()
    print("Usuario creado: admin / admin123")
finally:
    db.close()