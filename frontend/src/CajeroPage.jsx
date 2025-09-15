import React, { useEffect, useState } from "react";

const CajeroPage = () => {
  const [tasks, setTasks] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const token = localStorage.getItem("token"); // Suponiendo que guardaste el token al logear
        const response = await fetch("http://127.0.0.1:8000/api/cajero_tasks/", {
          headers: {
            "Content-Type": "application/json",
            "Authorization": `Token ${token}`,
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
    <div style={{ padding: "20px" }}>
      <h1>Panel Cajero</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <ul>
        {tasks.map((task, idx) => (
          <li key={idx}>{task}</li>
        ))}
      </ul>
    </div>
  );
};

export default CajeroPage;
