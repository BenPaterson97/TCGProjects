import React, { useState } from 'react';
import './App.css';

interface FlipResult {
  mana_produced: number;
  timestamp: string;
}

function App() {
  const [results, setResults] = useState<FlipResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleFlip = async () => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:8000/flip');
      const data = await response.json();
      setResults(prev => [...prev, {
        mana_produced: data.mana_produced,
        timestamp: new Date().toLocaleTimeString()
      }]);
    } catch (error) {
      console.error('Error flipping:', error);
    }
    setIsLoading(false);
  };

  const handleReset = async () => {
    setIsLoading(true);
    try {
      await fetch('http://localhost:8000/reset', { method: 'POST' });
      setResults([]);
    } catch (error) {
      console.error('Error resetting:', error);
    }
    setIsLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Selvala Flip Simulator</h1>
        <div className="button-container">
          <button 
            onClick={handleFlip} 
            disabled={isLoading}
            className="flip-button"
          >
            {isLoading ? 'Flipping...' : 'Flip'}
          </button>
          <button 
            onClick={handleReset} 
            disabled={isLoading}
            className="reset-button"
          >
            Reset
          </button>
        </div>
        <div className="results-container">
          <h2>Flip History</h2>
          {results.length === 0 ? (
            <p>No flips yet</p>
          ) : (
            <ul>
              {results.map((result, index) => (
                <li key={index}>
                  {result.timestamp}: {result.mana_produced} green mana
                </li>
              ))}
            </ul>
          )}
        </div>
      </header>
    </div>
  );
}

export default App; 