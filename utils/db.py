from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(
    'postgresql://root:this-is-a-very-strong-passsword@localhost:5432/test',
)
session = Session(engine, autoflush=True)
