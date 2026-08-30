from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class FarmModel:
    __tablename__ = 'farms'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    farm_type = Column(String(255), nullable=False)