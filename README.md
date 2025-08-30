# PwnİP

📌 PwnIP v1.1

A simple yet powerful OSINT and network tool for Termux & Linux.
With PwnIP you can quickly gather information about IPs, run reverse DNS checks, scan open ports, and even discover devices connected to your Wi-Fi network.


✨ Features

🔍 IP Lookup → Get country, city, ISP, and organization info about any IP.

🌐 Reverse DNS → Find the domain/hostname of an IP.

🚀 Port Scan (Nmap-like) → Scan a target IP for open ports.

📡 Wi-Fi Users Discovery → Detect devices connected to your Wi-Fi (LAN scan).


⚙ Installation

Clone the repo:

<code>git clone https://github.com/yourusername/pwnip.git
cd pwnip</code>

Install dependencies:

<code>pip install -r requirements.txt</code>

For Termux, make sure you have ping:

<code>pkg install iputils -y</code>

Run the tool:

<code>python3 pwnip.py</code>

📂 Requirements

requests

rich

🖥 Usage Example

Main Menu:

1. IP Lookup
2. Reverse DNS
3. Port & Network Tools
4. Exit

Port & Network Tools Menu:

1. Port Scan
2. Wi-Fi Users Discovery
3. Back

⚠ Disclaimer

This tool is created for educational and ethical purposes only.
The author takes no responsibility for misuse or illegal activities.

To exit the tool, simply choose the “Exit” option in the menu.

You can help us improve the system by sharing errors with us at codewriter@proton.me . Thank you...
