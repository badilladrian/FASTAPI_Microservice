from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(
    'postgresql://farmly_user:farmly_password@localhost:5432/farmly',
)
session = Session(engine)
