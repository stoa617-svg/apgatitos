const API_BASE = "https://kittycheck-api.onrender.com";

document.getElementById("controlForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const data = {
    cat_name: document.getElementById("cat_name").value,
    age_months: parseInt(document.getElementById("age_months").value),
    weight_g: parseInt(document.getElementById("weight_g").value),
    sex: "N/A",
    stage: "Gatito",
    dewormer: document.getElementById("dewormer").value,
    base_dose_mg_per_kg: 5.0,
    date: document.getElementById("date").value,
    notes: "Registro desde frontend"
  };

  const res = await fetch(`${API_BASE}/api/controls`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  const result = await res.json();
  document.getElementById("result").textContent = JSON.stringify(result, null, 2);
});
