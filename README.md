```text


 /$$$$$$$                            /$$                              
| $$__  $$                          | $$                              
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$       /$$$$$$/$$$$   /$$$$$$ 
| $$$$$$$/ /$$__  $$ |____  $$ /$$__  $$      | $$_  $$_  $$ /$$__  $$
| $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$      | $$ \ $$ \ $$| $$$$$$$$
| $$  \ $$| $$_____/ /$$__  $$| $$  | $$      | $$ | $$ | $$| $$_____/
| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$      | $$ | $$ | $$|  $$$$$$$
|__/  |__/ \_______/ \_______/ \_______/      |__/ |__/ |__/ \_______/
                                                                      
                                                                      
                                                                      
# Flask Server

This project features a full overview for your local server and helps you to fetch data like current RAM usage, CPU usage, Power usage and more...

Installation Guide (Linux)

This guide explains how to run the Custom Web Scraper dashboard locally on a Linux system.

1️⃣ Requirements

Make sure you have the following installed:

Python 3.9+

pip (Python package manager)

A Linux system (Ubuntu, Debian, Arch, etc.)

Check your Python version:

```
python3 --version
```

If Python is missing:

sudo apt install python3 python3-pip -y

2️⃣ Clone the Repository

Clone the project from GitHub and move into the project directory:

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

3️⃣ (Optional but Recommended) Create a Virtual Environment

This keeps dependencies clean and avoids conflicts.

python3 -m venv venv
source venv/bin/activate


You should now see (venv) in your terminal.

4️⃣ Install Dependencies

Install the required Python packages:

pip install flask psutil


(If you later add more dependencies, you can put them into a requirements.txt.)

5️⃣ Configure the Project

Open the main Python file (for example app.py) and edit the following values:

TAILSCALE_IP = "your IP"

servers = [
    {"name": "Service A", "ip": "your IP", "port": 8000},
    {"name": "Service B", "ip": "your IP", "port": 8080},
]


🔧 Replace "your IP" with:

your local machine IP

or your Tailscale IP if you use a VPN

You can add or remove services as needed.

6️⃣ Run the Application

Start the Flask server:

python3 app.py


If everything works, you should see output like:

Running on http://0.0.0.0:5000/

7️⃣ Open the Dashboard

Open your browser and go to:

http://localhost:5000


If you are accessing it from another device on the network, use:

http://YOUR_LOCAL_IP:5000

8️⃣ Using the Tailscale Toggle

The VPN toggle switches links between local IPs and your Tailscale IP

This allows quick testing between local network and VPN access 😄🌐

No page reload logic is needed beyond the built-in refresh

🛑 Stopping the Server

To stop the application, press:

CTRL + C

Have fun! 😊



 ______              _______ _________ _______  _______  _______         _______  _______           _______  _______ 
(  ___ \ |\     /|  (       )\__   __/(  ____ \(  ____ )(  ___  )       (  ____ )(  ___  )|\     /|(  ____ \(  ____ )
| (   ) )( \   / )  | () () |   ) (   | (    \/| (    )|| (   ) |       | (    )|| (   ) || )   ( || (    \/| (    )|
| (__/ /  \ (_) /   | || || |   | |   | |      | (____)|| |   | | _____ | (____)|| |   | || | _ | || (__    | (____)|
|  __ (    \   /    | |(_)| |   | |   | |      |     __)| |   | |(_____)|  _____)| |   | || |( )| ||  __)   |     __)
| (  \ \    ) (     | |   | |   | |   | |      | (\ (   | |   | |       | (      | |   | || || || || (      | (\ (   
| )___) )   | |     | )   ( |___) (___| (____/\| ) \ \__| (___) |       | )      | (___) || () () || (____/\| ) \ \__
|/ \___/    \_/     |/     \|\_______/(_______/|/   \__/(_______)       |/       (_______)(_______)(_______/|/   \__/
                                                                                                                     









