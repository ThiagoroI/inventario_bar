import { useEffect, useState } from "react";
import { getProductos } from "../../services/api";

function Inventario() {
  const [productos, setProductos] = useState([]);

  useEffect(() => {
    getProductos()
      .then(data => setProductos(data))
      .catch(err => console.error("Error cargando productos:", err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Inventario</h1>
      <table border="1" cellPadding="10" style={{ marginTop: "20px" }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Cantidad Nominal</th>
            <th>Unidad</th>
            <th>Precio</th>
            <th>stock</th>
          </tr>
        </thead>
        <tbody>
          {productos.map(p => (
            <tr key={p.id}>
              <td>{p.id}</td>
              <td>{p.nombre}</td>
              <td>{p.cantidad_nominal}</td>
              <td>{p.unidad}</td>
              <td>{p.precio}</td>
              <th>{p.stock}</th>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Inventario;
