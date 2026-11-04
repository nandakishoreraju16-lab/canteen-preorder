import { useState, useEffect } from "react";
import MenuList from "./components/MenuList";
import MyOrders from "./components/MyOrders";

const API_URL = "http://127.0.0.1:8001";

function App() {
  const [items, setItems] = useState([]);
  const [rollNo, setRollNo] = useState("");
  const [quantity, setQuantity] = useState(1);
  const [orders, setOrders] = useState([]);
  const [myRollNo, setMyRollNo] = useState("");
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    // GET /menu
    fetch(API_URL + "/menu")
      .then((response) => response.json())
      .then((data) => setItems(data));
  }, []);

  // POST /orders   (SEND a new order to our API)
  function placeOrder(itemId) {
    if (rollNo.trim() === "") return;          // no roll number, so don't send
    if (quantity < 1 || quantity > 5) return;  // quantity must be 1 to 5

    fetch(API_URL + "/orders?roll_no=" + rollNo + "&item_id=" + itemId + "&quantity=" + quantity, {
      method: "POST",
    })
      .then((response) => response.json())
      .then(() => loadOrders(rollNo));   // show the new order in My orders
  }

  // GET /orders/student/{roll_no}   (one student's orders for today)
  function loadOrders(roll) {
    setMyRollNo(roll);
    setSelected(null);
    fetch(API_URL + "/orders/student/" + roll)
      .then((response) => response.json())
      .then((data) => setOrders(data));
  }

  // PATCH /orders/{id}/cancel
  function cancelOrder(id) {
    fetch(API_URL + "/orders/" + id + "/cancel", {
      method: "PATCH",
    })
      .then((response) => response.json())
      .then(() => loadOrders(myRollNo));   // load the list again
  }

  // GET /orders/{id}   (one order's details)
  function showDetails(id) {
    fetch(API_URL + "/orders/" + id)
      .then((response) => response.json())
      .then((data) => setSelected(data));
  }

  return (
    <>
      <h1>Canteen Pre-Orders</h1>

      <input
        type="text"
        placeholder="Roll number"
        value={rollNo}
        onChange={(e) => setRollNo(e.target.value)}
      />
      <input
        type="number"
        min="1"
        max="5"
        value={quantity}
        onChange={(e) => setQuantity(Number(e.target.value))}
      />

      <MenuList items={items} onOrder={placeOrder} />

      <MyOrders
        orders={orders}
        selected={selected}
        onShow={loadOrders}
        onCancel={cancelOrder}
        onSelect={showDetails}
      />
    </>
  );
}

export default App;
