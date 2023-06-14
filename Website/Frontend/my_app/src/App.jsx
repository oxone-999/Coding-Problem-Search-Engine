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
    <>
      <div className="App">
        <button data-text="Awesome" className="button1">
          <span className="actual-text">&nbsp;CodeSearch&nbsp;</span>
          <span className="hover-text" aria-hidden="true">
            &nbsp;CodeSearch&nbsp;
          </span>
        </button>
        <div className="wow">
          <div>Search for your favourite coding problems from </div>
          <img
            className="image1"
            src="https://cdn.iconscout.com/icon/free/png-256/free-leetcode-3628885-3030025.png"
            alt="leetcode"
            border="0"
          />
          <img
            className="image2"
            src="https://codeforces.org/s/0/images/codeforces-sponsored-by-ton.png"
            alt="codeforces"
            border="0"
          />
          <img
            className="image3"
            src="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/zruiknbedz8yqafxbazb"
            alt="codechef"
            border="0"
          />
        </div>
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
            <>
              <h3>
                The Dataset is very big so it may take some time, please be
                patient...
              </h3>
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
            </>
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
    </>
  );
}

export default App;
