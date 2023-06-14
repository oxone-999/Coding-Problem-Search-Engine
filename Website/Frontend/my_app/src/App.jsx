import React, { useState } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleInputChange = (e) => {
    setQuery(e.target.value);
  };

  const handleSearch = async () => {
    setResponse(null);
    setIsLoading(true);

    try {
      const data = await fetch(
        "https://coding-search-service.onrender.com/api/search",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ query }),
        }
      );
      try {
        const outputList = await data.json();
        setResponse(outputList);
        console.log(outputList);
        setIsLoading(false);
      } catch (err) {
        console.log(err);
      }
    } catch (err) {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <button data-text="Awesome" className="button1">
        <span className="actual-text">&nbsp;CodeSearch&nbsp;</span>
        <span className="hover-text" aria-hidden="true">
          &nbsp;CodeSearch&nbsp;
        </span>
      </button>
      <div className="container_x">
        <input
          placeholder="Enter the keywords ......."
          className="input"
          type="text"
          value={query}
          onChange={handleInputChange}
          ></input>
        <button className="button" onClick={handleSearch}>
          Search
        </button>
      </div>
      <div className="content">
        {isLoading && (
          <div className="loader">
            <div class="spinner">
              <div></div>
              <div></div>
              <div></div>
              <div></div>
              <div></div>
              <div></div>
            </div>
          </div>
        )}
        {response && response !== undefined && response !== null && (
          <ul>
            {response.results.map((value, index) => (
              <li key={index}>
                <a
                  href={value.split("*")[0]}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  {value.split("*")[1]}
                </a>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default App;
