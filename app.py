import uuid
from flask import Flask,request
from flask_smorest import abort
from db import items,stores

app = Flask(__name__)
stores = {
    
        
    }

items = {
    1:{
        "name":"chair",

    }
}

@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, "Bad request. Ensure that the store name is in the JSON payload.")
    for store in stores.values():
        if store_data["name"]== store["name"]:
            abort(400, "Store alerady esists.")
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id" : store_id}
    stores[store_id] = new_store
    return new_store, 201

@app.post("/item")
def create_item(name):
    item_data = request.get_json
    if (
        "price" not in item_data
        or "store_id" not in item_data
        or "name" not in item_data
    ):
        abort(404, message="Bad request. Ensure 'price' 'store_id' and 'name' are included in JSON payload.")
    for item in item.values():
        if (
            item_data["name"] == item["name"]
            and item_data["store_id"] == item["store_id"]
        ):
            abort(400, message=f"Iteam already exists.")
        if item_data["store_id"] not in stores:
            abort(404, message="Store not found.")
    item_id = uuid.uuid4().hex
    item = {**item_data, "id":item_id}
    items[item_id]=item

@app.get("/item")
def get_all_items():
    return {"items":list(items.values())}



@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message= "Store not found.")


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return(items[item_id])
    except KeyError:
        abort(404, message="Item not found.")

