import React, { useState } from 'react';
//app.js
function App() {
  const [task, setTask] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('http://localhost:8000/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ task }),
    })
    .then((response) => {
      console.log(response); // log the response for debugging
      return response.json();
    })
    .then((data) => {
      console.log(data); // log the response data for debugging
      
    })
    .catch((error) => console.error(error));
  };

  return (
    <div>
      <h1>Task Queue</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Task:
          <input
  type="text"
  value={task}
  name="task"
  onChange={(e) => setTask(e.target.value)}
/>
        </label>
        <button type="submit">Add Task</button>
      </form>
    </div>
  );
}

export default App;
