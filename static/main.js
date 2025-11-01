document.getElementById('predictBtn').addEventListener('click', async () => {
  const beta1 = document.getElementById('beta1').value;
  const beta2 = document.getElementById('beta2').value;
  const amh = document.getElementById('amh').value;
  const output = document.getElementById('output');
  output.innerHTML = '<div class="loading">Predicting...</div>';

  try {
    const resp = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ beta_hcg_i: beta1, beta_hcg_ii: beta2, amh: amh })
    });

    if (!resp.ok) {
      const err = await resp.json();
      output.innerHTML = `<div class="result error">${err.error || 'Prediction failed'}</div>`;
      return;
    }

    const data = await resp.json();
    let cls = data.prediction === 1 ? 'result pos' : 'result neg';
    let html = `<div class="${cls}"><strong>${data.label}</strong><br/>Code: ${data.prediction}`;
    if (data.probability !== undefined) {
      html += `<br/>Confidence: ${(data.probability*100).toFixed(1)}%`;
    }
    html += `</div>`;
    output.innerHTML = html;
  } catch (e) {
    output.innerHTML = `<div class="result error">Error: ${e.message}</div>`;
  }
});
