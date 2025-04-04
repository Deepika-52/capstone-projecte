// extension/content.js

// Function to send text to the prediction API
async function getPrediction(text) {
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
      });
      const data = await response.json();
      return data.prediction;
    } catch (error) {
      console.error('Error in prediction:', error);
      return null;
    }
  }
  
  // Example: Scan all paragraphs and filter harmful content
  async function filterContent() {
    const paragraphs = document.querySelectorAll('p, span, div');
  
    paragraphs.forEach(async (element) => {
      const text = element.innerText;
      if (text && text.trim().length > 20) { // Only check elements with enough text
        const prediction = await getPrediction(text);
        if (prediction && prediction.toLowerCase() === 'harmful') {
          element.style.display = 'none';  // Hide harmful content
          console.log('Hidden harmful content:', text);
        }
      }
    });
  }
  
  // Run the filter function after page load
  window.addEventListener('load', filterContent);
  