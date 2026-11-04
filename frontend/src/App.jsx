import { useState } from "react";
import MenuList from "./components/MenuList";

const API_URL = "http://127.0.0.1:8001";

function App() {
  const [items, setItems] = useState([
    { id: 1, name: "Masala Dosa", category: "breakfast", price: 40, available: true },
    { id: 2, name: "Veg Meals", category: "meals", price: 80, available: true },
    { id: 3, name: "Samosa", category: "snacks", price: 15, available: false },
  ]);

  return (
    <>
      <h1>Canteen Pre-Order</h1>
      <MenuList items={items} />
    </>
  );
}

export default App;
