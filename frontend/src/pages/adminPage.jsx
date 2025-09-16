import React, { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { useNavigate } from "react-router-dom";


const AdminPage = () => {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState("");
  const navigate = useNavigate(); /* ruta de navegacion para los botones*/

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await fetch("http://127.0.0.1:8000/api/admin_tasks/", {
          headers: {
            "Content-Type": "application/json",
            Authorization: `Token ${token}`,
          },
        });

        if (!response.ok) {
          throw new Error("No autorizado o error en la petición");
        }

        const data = await response.json();
        setTasks(data.tasks);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchTasks();
  }, []);

  return (
    <div className="relative min-h-screen bg-gray-50 p-6">
      <h1 className="text-3xl font-bold mb-6">Panel Administrador</h1>

      {error && <p className="text-red-500">{error}</p>}

      {/* Lista de tareas */}
      <Card className="mb-10 max-w-lg">
        <CardContent>
          <h2 className="text-xl font-semibold mb-4">Tareas Asignadas</h2>
          <ul className="list-disc pl-5">
            {tasks.length > 0 ? (
              tasks.map((task, idx) => <li key={idx}>{task}</li>)
            ) : (
              <p>No hay tareas registradas.</p>
            )}
          </ul>
        </CardContent>
      </Card>

      {/* Panel de control en la esquina */}
      <div className="absolute top-6 right-6">
        <Card className="shadow-lg w-48">
          <CardContent className="flex flex-col gap-3">
            <h3 className="font-semibold text-lg mb-2">Panel de Control</h3>
            <Button variant="outline" onClick={() => navigate("/inventario")}>
                    Ver Inventario
            </Button>
            <Button variant="outline">Usuarios</Button>
            <Button variant="outline">Reportes</Button>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default AdminPage;


