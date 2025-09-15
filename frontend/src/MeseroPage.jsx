// src/MeseroPage.jsx
import React, { useEffect, useState } from "react";

const MeseroPage = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/mesero_tasks/", {
      headers: { "Authorization": "Bearer " + localStorage.getItem("token") }
    })
    .then(res => res.json())
    .then(data => setTasks(data.tasks));
  }, []);

  return (
    <div>
      <h1>Mesero</h1>
      <ul>
        {tasks.map(task => <li key={task}>{task}</li>)}
      </ul>
    </div>
  );
};

export default MeseroPage;
