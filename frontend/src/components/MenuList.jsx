import MenuItem from "./MenuItem";

function MenuList({ items }) {
  return (
    <>
      <h1>Menu</h1>
      <ul className="products">
        {items.map((item) => (
          <MenuItem key={item.id} item={item} />
        ))}
      </ul>
    </>
  );
}

export default MenuList;
