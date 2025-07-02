from sqlalchemy.ext.declarative import declarative_base

# Define la base declarativa para tus modelos de SQLAlchemy
Base = declarative_base()

# Aquí es donde más adelante definirás tus modelos de base de datos, por ejemplo:
# from sqlalchemy import Column, Integer, String
#
# class CryptoData(Base):
#    __tablename__ = "crypto_data"
#    id = Column(Integer, primary_key=True, index=True)
#    symbol = Column(String, index=True)
#    price = Column(Float)
#    timestamp = Column(DateTime)