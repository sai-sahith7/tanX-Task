from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.utils.db import Base

class Alert(Base):
    __tablename__ = "alerts"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    coin = Column(String, index=True)
    target_price = Column(Float)
    price_when_created = Column(Float)
    status = Column(String, index=True)

    owner = relationship("User", back_populates="alerts")
