from fastapi import FastAPI, HTTPException
import functions
app = FastAPI()


@app.get("/menu")
def menu():
    return functions.menu_items()

