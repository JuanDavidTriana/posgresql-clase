from sqlalchemy import create_engine, Column, Integer,String
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = 'postgresql+psycopg2://postgres:Admin@localhost:5432/tienda_online'

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True )
    nombre = Column(String, nullable=False )

Base.metadata.create_all(engine)