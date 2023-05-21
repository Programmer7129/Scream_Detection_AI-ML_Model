import React, { useState } from "react";

const ActivateButton = () => {
  const [file, setFile] = useState(null);
  const [showResult, setShowResult] = useState(false);
  const [showResult1, setShowResult1] = useState(false);
  const [showResult2, setShowResult2] = useState(false);
  const [result, setResult] = useState("");
  
  function handleFileChange(event) {
    const selectedFile = event.target.files[0];
    setFile(selectedFile);
    // Resetting the showResult states when file changes
    setShowResult(false);
    setShowResult1(false);
    setShowResult2(false);
  }
  
  function activateAI() {
    if (file) {
      const formData = new FormData();
      formData.append("file", file);

      fetch("http://localhost:5000/members", {
        method: "POST",
        body: formData,
      })
        .then((response) => response.json())
        .then((responseData) => {
          console.log(responseData);
          setResult(responseData.is_scream);
          // Setting the corresponding showResult state based on responseData.number_color
          if (responseData.number_color === 0) {
            setShowResult(true);
          } else if (responseData.number_color === 1) {
            setShowResult1(true);
          } else if (responseData.number_color === 2) {
            setShowResult2(true);
          }
        });
    } else {
      console.log("No file selected");
    }
  }

  return (
    <div>
      <label htmlFor="fileInput" className="fileLabel">
        Choose File
        <input
          id="fileInput"
          className="input"
          type="file"
          accept="audio/wav"
          onChange={handleFileChange}
        />
      </label>
      <br></br>
      <button className="activateButton" onClick={activateAI}>
        Activate
      </button>
  
      <div className="container">
      {/* Rendering the result based on the corresponding showResult state */}
      {showResult && <p className="safe">You are safe</p>}
      {showResult1 && <p className="medium">Risk is Medium, calling officer in that neigborhood</p>}
      {showResult2 && <p className="emergency">Emergency Alert! Risk is high. Send immediate help.</p>}
      </div>
    </div>
  );
};

export default ActivateButton;
