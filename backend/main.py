from fastapi import FastAPI, HTTPException
import functions
app = FastAPI()

@app.get("/sample menu")
def menu():
    return functions.menu_items()

@app.get("/sample orders")
def menu():
    return functions.orders()

@app.get("/menu")
def menu(category:str = None, available:int = None):
    if category is not None and category not in ["breakfast", "meals", "snacks", "beverages", "desserts"]:
        raise HTTPException(status_code=422, detail="Invalid category")
    if available is not None and available not in [0, 1]:
        raise HTTPException(status_code=422, detail="Available must be 0 or 1")
    return functions.get_all_menu_items(category=category, available=available)

@app.post("/menu")
def add_menu(name: str, category: str, price: int):
    return functions.add_menu_item(name=name,category=category,price=price)

@app.patch("/menu/{id}/availability")
def update_availability(id: int, available: int):
    return functions.update_menu_availability(id, available)
    

@app.post("/orders")
def place_order(roll_no: str, item_id: int, quantity: int):
    return functions.place_order(roll_no=roll_no,item_id=item_id,quantity=quantity)

@app.get("/orders/{id}")
def get_order(id: int):
    return functions.get_order_by_id(id)
    