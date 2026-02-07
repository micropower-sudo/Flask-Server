# ================================
# Imports
# ================================
# Flask is used to serve the web interface
# psutil provides system metrics like CPU/RAM usage
# socket is used to check if servers are reachable
# random is used here to simulate power consumption
# datetime can be used for logging or timestamps
from flask import Flask, render_template_string, request
import psutil
import socket
import random
from datetime import datetime

# ================================
# Flask App Initialization
# ================================
# Main Flask application instance
# You can rename this if you integrate the app into a bigger project
app = Flask(__name__)

# ================================
# Network Configuration
# ================================
# Replace "your IP" with your real local or VPN IP if needed
# This can be used for VPNs like Tailscale or WireGuard
TAILSCALE_IP = "your IP"

# ================================
# Server Definitions
# ================================
# List of services that will be checked and displayed in the dashboard
# You can add or remove servers as needed
servers = [
    {"name": "Service A", "ip": "your IP", "port": 8000},
    {"name": "Service B", "ip": "your IP", "port": 8080},
    {"name": "Service C", "ip": "your IP", "port": 8443}
]

# ================================
# History Storage
# ================================
# Stores the last values for charts
# You can increase or decrease the history length later
history = {
    "cpu": [],
    "ram": [],
    "power": []
}

# ================================
# Helper Functions
# ================================
# Checks if a specific IP and port are reachable
# Used to detect whether a service is online
def is_online(ip, port):
    try:
        socket.create_connection((ip, port), timeout=1).close()
        return True
    except:
        return False

# ================================
# Main Dashboard Route
# ================================
# This route renders the entire dashboard
@app.route("/")
def index():

    # ============================
    # System Metrics
    # ============================
    # Collects system statistics
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    # Simulated power usage (replace with real sensor data if available)
    power = round(8 + random.uniform(-1.5, 1.5), 2)

    # ============================
    # Update History
    # ============================
    history["cpu"].append(cpu)
    history["ram"].append(ram)
    history["power"].append(power)

    # Limit history length (last 30 entries)
    for key in history:
        history[key] = history[key][-30:]

    # ============================
    # VPN / Direct Access Toggle
    # ============================
    # Allows switching between local IP and VPN IP
    use_ts = request.args.get("ts") == "1"

    # ============================
    # HTML Template Rendering
    # ============================
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="16">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Custom Web Scraper</title>

<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
body{margin:0;background:#000;color:#0f0;font-family:'Share Tech Mono'}
header{font-size:2.3em;text-align:center;padding:20px;position:relative}
#clock{position:absolute;top:22px;right:30px;font-size:0.45em}

.container{display:grid;grid-template-columns:1fr 1.4fr;gap:35px;padding:40px}
.card{background:#111;border:2px solid #0f0;border-radius:25px;padding:30px}

canvas{width:100%!important;height:360px!important}

.server-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:18px}
button{
background:#000;border:2px solid #0f0;color:#0f0;
padding:6px 14px;border-radius:8px;cursor:pointer;
font-family:'Share Tech Mono'
}
</style>
</head>

<body>

<header>
Custom Web Scraper
<div id="clock"></div>
</header>

<div class="container">

<div class="card">
<h2>System Info</h2>
CPU: {{cpu}} %<br>
RAM: {{ram}} %<br>
Disk: {{disk}} %<br>
Power: {{power}} W
</div>

<div class="card">
<h2>Performance History</h2>
<canvas id="chart"></canvas>
</div>

<div class="card">
<h2>Services</h2>
{% for s in servers %}
<div class="server-row">
<div>
{{s.name}}<br>
IP: {{s.ip}}:{{s.port}}
</div>
<div>
<button onclick="location.href='http://{{tailscale_ip if use_ts else s.ip}}:{{s.port}}'">
Open
</button>
<button onclick="location.href='/?ts={{0 if use_ts else 1}}'">
{{'VPN ON' if use_ts else 'VPN OFF'}}
</button>
</div>
</div>
{% endfor %}
</div>

</div>

<script>
new Chart(document.getElementById('chart'),{
type:'line',
data:{
labels:[...Array({{history['cpu']|length}}).keys()],
datasets:[
{label:'CPU %',data:{{history['cpu']}},borderColor:'red',tension:0.3},
{label:'RAM %',data:{{history['ram']}},borderColor:'blue',tension:0.3},
{label:'Power W',data:{{history['power']}},borderColor:'yellow',tension:0.3}
]},
options:{responsive:true,maintainAspectRatio:false}
});

setInterval(()=>{
document.getElementById("clock").innerText =
new Date().toLocaleTimeString();
},1000);
</script>

</body>
</html>
""",
cpu=cpu,
ram=ram,
disk=disk,
power=power,
servers=servers,
tailscale_ip=TAILSCALE_IP,
history=history,
use_ts=use_ts
)

# ================================
# Application Entry Point
# ================================
# Change host/port if you want to restrict network access
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
