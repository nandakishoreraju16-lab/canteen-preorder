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

def menu_items():
    session = Session(engine)
    menu = [
        MenuItem(name="Idli", category="breakfast", price=30, available=1),
        MenuItem(name="Dosa", category="breakfast", price=40, available=1),
        MenuItem(name="Puri", category="breakfast", price=35, available=1),
        MenuItem(name="Veg Meals", category="meals", price=80, available=1),
        MenuItem(name="Fried Rice", category="meals", price=90, available=1),
        MenuItem(name="Samosa", category="snacks", price=15, available=1),
        MenuItem(name="Sandwich", category="snacks", price=50, available=0),
        MenuItem(name="Burger", category="snacks", price=70, available=1),
        MenuItem(name="Tea", category="beverages", price=10, available=1),
        MenuItem(name="Coffee", category="beverages", price=20, available=0),
        MenuItem(name="Ice Cream", category="desserts", price=40, available=1),
        MenuItem(name="Gulab Jamun", category="desserts", price=30, available=1)
    ]
    session.commit()
    session.close()
    return menu



