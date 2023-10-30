from sqlalchemy import Column, Integer, String
from app.db.base_class import Base


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Integer, index=True)
    owner_id = Column(String)
