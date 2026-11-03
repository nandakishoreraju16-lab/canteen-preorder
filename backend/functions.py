from sqlalchemy import Integer, String, Column, create_engine, DateTime, ForeignKey
from sqlalchemy.orm import Session, declarative_base
from datetime import datetime

DB_PATH = "canteen-preorder.db"
engine = create_engine(f"sqlite:///{DB_PATH}")
Base = declarative_base()

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column[int](Integer, primary_key=True)
    name = Column[str](String)
    category = Column[str](String)
    price = Column[int](Integer)
    available = Column[int](Integer, default=1)


class Order(Base):
    __tablename__ = "orders"
    id = Column[int](Integer, primary_key=True)
    roll_no = Column[str](String)
    item_id = Column[int](Integer, ForeignKey("menu_items.id"))
    quantity = Column[int](Integer)
    status = Column[str](String, default="placed")
    ordered_at = Column[DateTime](DateTime, default=datetime.now)
    collected_at = Column[DateTime](DateTime, nullable=True)

Base.metadata.create_all(engine)