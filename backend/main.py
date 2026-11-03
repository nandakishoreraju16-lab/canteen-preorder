from fastapi import FastAPI, HTTPException
import functions
import endpoints

app = FastAPI()


@app.get("/menu")
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
