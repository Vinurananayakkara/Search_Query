import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [pr_id, setPr_id] = useState('');
  const [result, setResult] = useState(null);

  const handleSearch = async () => {
    try {
      const res = await axios.get(`http://localhost:8000/search/${pr_id}`);
      setResult(res.data);
    } catch (error) {
      console.error(error);
      setResult({ message: "Error occurred" });
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Search by PR No</h2>
      <input
        type="text"
        value={pr_id}
        onChange={(e) => setPr_id(e.target.value)}
        placeholder="Enter PR ID (e.g., PRAD001)"
      />
      <button onClick={handleSearch}>Search</button>

      {result && (
        <div style={{ marginTop: 20 }}>
          {Array.isArray(result) ? (
            <table border="1">
              <thead>
                <tr>
                  {Object.keys(result[0]).map((key) => (
                    <th key={key}>{key}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {result.map((row, rowIndex) => (
                  <tr key={rowIndex}>
                    {Object.values(row).map((value, i) => (
        <td key={i}>{value}</td>
      ))}
    </tr>
  ))}
              </tbody>
            </table>
          ) : (
            <p>{result.message}</p>
          )}
        </div>
      )}
    </div>
  );
}

export default App;
