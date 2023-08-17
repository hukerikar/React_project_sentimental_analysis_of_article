import React, { useState } from 'react';
import './index.css';

function Main() {
  const [enteredURL, setEnteredURL] = useState('');
  const [analysisResult, setAnalysisResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  function handleURLChange(event) {
    setEnteredURL(event.target.value);
  }

  async function analyzeData(analysisType) {
    try {
      setIsLoading(true);
      const response = await fetch('http://localhost:5000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          url: enteredURL,
          analysisType: analysisType,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const result = await response.json();
      setAnalysisResult(result);
      setIsLoading(false);
      console.log('Analysis Result:', result);
    } catch (error) {
      console.error('Error:', error);
      setIsLoading(false);
    }
  }

  return (
    <div className="container">
      <h1>Enter your Article Link</h1>
      <input
        type="text"
        className="form-control"
        id="URLInput"
        placeholder="www.example.com"
        value={enteredURL}
        onChange={handleURLChange}
      />
      <div className="input-container">
        <button className="btn btn-primary spaced-btn" onClick={() => analyzeData('sentiment')}>
          Analyze Sentiment
        </button>

        <button className="btn btn-primary spaced-btn" onClick={() => analyzeData('keywords')}>
          Extract Keywords
        </button>

        <button className="btn btn-primary spaced-btn" onClick={() => analyzeData('summary')}>
          Generate Summary
        </button>

        <button className="btn btn-primary spaced-btn" onClick={() => analyzeData('description')}>
          Description
        </button>
      </div>

      {isLoading ? (
        <div className="loading-indicator">
          <div className="spinner"></div>
        </div>
      ) : (
        analysisResult && (
          <div className="analysis-result">
            <h2>Analysis Result</h2>
            <pre>{JSON.stringify(analysisResult, null, 2)}</pre>
            {analysisResult && analysisResult.keywords && (
              <div className="keywords">
                <h4>Keywords:</h4>
                <ul className="horizontal-list">
                  {analysisResult.keywords.map((keyword, index) => (
                    <li key={index}>{keyword}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )
      )}
    </div>
  );
}

export default Main;
