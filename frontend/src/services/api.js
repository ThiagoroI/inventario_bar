const API_URL = "http://127.0.0.1:8000/api"; // tu backend

export async function getProductos() {
  const response = await fetch(`${API_URL}/productos/`);
  if (!response.ok) {
    throw new Error("Error al obtener productos");
  }
  return await response.json();
}
