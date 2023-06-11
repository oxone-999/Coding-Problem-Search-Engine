import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState(null);

  const handleInputChange = (e) => {
    setQuery(e.target.value);
  };

  const handleSearch = async () => {
    const data = await fetch('http://localhost:5000/api/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query }),
    });
    const outputList = await data.json();
    setResponse(outputList);
    console.log(outputList);
  };

  return (
    <div className="App">
      <h1>Coding Question Search Engine</h1>
      <input type="text" placeholder="Search for a coding question..." value={query} onChange={handleInputChange} />
      <button onClick={handleSearch}>Search</button>
      <div>
        <h2>Results:</h2>
        {response && response !== undefined && response !== null && (
          <ul>
            {response.results.map((result, index) => (
              <li key={index}>{result}</li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default App;