import React, { useState } from "react";

function App() {
  const [form, setForm] = useState({});
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: Number(e.target.value)
    });
  };

  const handleSubmit = async () => {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(form)
    });

    const data = await res.json();
    setResult(data);
  };

  const getColor = (val) => (val === 1 ? "red" : "green");

  return (
  <div className="App">
    <h1>🧠 AI-Driven Digital Twin Healthcare</h1>

    <div className="input-grid">
      <input
        name="age"
        type="number"
        placeholder="Age (Years)"
        onChange={handleChange}
      />

      <input
        name="sex"
        type="number"
        placeholder="Gender (0 = Female, 1 = Male)"
        onChange={handleChange}
      />

      <input
        name="chol"
        type="number"
        placeholder="Cholesterol (mg/dL)"
        onChange={handleChange}
      />

      <input
        name="Glucose"
        type="number"
        placeholder="Glucose (mg/dL)"
        onChange={handleChange}
      />
    </div>

    <button onClick={handleSubmit}>
      🔍 Predict Health Risk
    </button>

    {result && (
      <div className="results">

        <h2>Prediction Results</h2>

        <div className={`result-card ${result.heart_risk ? "high" : "low"}`}>
          ❤️ Heart Disease Risk :
          <strong> {result.heart_risk ? "High" : "Low"}</strong>
        </div>

        <div className={`result-card ${result.diabetes_risk ? "high" : "low"}`}>
          🩸 Diabetes Risk :
          <strong> {result.diabetes_risk ? "High" : "Low"}</strong>
        </div>

        <div className={`result-card ${result.kidney_risk ? "high" : "low"}`}>
          🧬 Kidney Disease Risk :
          <strong> {result.kidney_risk ? "High" : "Low"}</strong>
        </div>

        {result.kidney_risk === 1 && (
          <div className="warning">
            ⚠️ <b>Recommendation:</b> Kidney disease risk is elevated.
            Please consult a healthcare professional for further evaluation.
          </div>
        )}

        <div className="result-card">
          <h3>🤖 Digital Twin Insight</h3>
          <p>{result.simulation}</p>
        </div>

      </div>
    )}
  </div>
);}

export default App;