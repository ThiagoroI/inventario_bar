// src/App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./login";

// Páginas de ejemplo para cada rol
const AdminPage = () => <h1>Página Admin</h1>;
const MeseroPage = () => <h1>Página Mesero</h1>;
const CajeroPage = () => <h1>Página Cajero</h1>;

function App() {
  return (
    <Router>
      <Routes>
        {/* Ruta principal: Login */}
        <Route path="/" element={<Login />} />

        {/* Rutas según roles */}
        <Route path="/admin" element={<AdminPage />} />
        <Route path="/mesero" element={<MeseroPage />} />
        <Route path="/cajero" element={<CajeroPage />} />
      </Routes>
    </Router>
  );
}

export default App;
