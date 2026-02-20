async function Actualizar() {
    const response = await fetch("/api/sensores");
    const data = await response.json();

    document.getElementById("temp").textContent = data.temperatura;
    document.getElementById("hum").textContent = data.humedad;
}
setInterval(Actualizar, 2000);
Actualizar();