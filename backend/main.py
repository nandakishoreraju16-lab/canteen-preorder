from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import functions

import endpoints


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sample menu")
def menu():
    return functions.menu_items()



# E6 - Get Student's Orders for Today

@app.get("/orders/student/{roll_no}")
def get_student_orders(roll_no: str):

    response = endpoints.get_student_orders(roll_no)

    return response

# E7 - Move Order to Next Status

@app.patch("/orders/{order_id}/next")
def next_order_status(order_id: int):
    return endpoints.move_order_to_next_status(order_id)

# E8 - Cancel Order

@app.patch("/orders/{order_id}/cancel")
def cancel_order(order_id: int):
    return endpoints.cancel_order(order_id)


# E9 - Get Kitchen Queue

@app.get("/kitchen/queue")
def get_kitchen_queue():
    return endpoints.get_kitchen_queue()


# E10 - Get Today's Sales Summary

@app.get("/kitchen/sales")
def get_today_sales():
    return endpoints.get_today_sales()

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
    

