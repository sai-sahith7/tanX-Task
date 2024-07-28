from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.utils.db import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    alerts = relationship("Alert", back_populates="owner")
