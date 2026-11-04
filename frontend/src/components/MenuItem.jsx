// One item from GET /menu:
// { id, name, category, price, available }
function MenuItem({ item }) {
  return (
    <li className="product">
      <h2>{item.name}</h2>
      <p>{item.category}</p>
      <p>₹{item.price}</p>
      <p>{item.available ? "Available" : "Sold out"}</p>
    </li>
  );
}

export default MenuItem;
