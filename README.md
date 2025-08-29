# PwnİP

1️⃣ Update your Termux packages

Before installing anything, make sure your Termux environment is up-to-date:

<code>pkg update && pkg upgrade -y</code>

2️⃣ Install Python and Git

PwnIP requires Python 3 and Git. Install them with:

<code>pkg install python git -y</code>

3️⃣ Clone the PwnIP repository

Get the latest version from GitHub:

<code>git clone https://github.com/yourusername/pwnip.git</code>

4️⃣ Navigate to the tool directory

Change into the cloned folder:

<code>cd pwnip</code>

5️⃣ Install Python dependencies

PwnIP uses some Python packages. Install them via pip:

<code>pip install -r requirements.txt</code>

> Dependencies include:

requests – for API calls

whois – for domain info

rich – for colorful terminal interface

6️⃣ Run PwnIP

Start the tool with Python 3:

<code>python pwnip.py</code>

You should now see the colorful PwnIP menu. Select options to perform IP Lookup, WHOIS Lookup, or Reverse DNS.

7️⃣ Notes

Works best on Termux and Linux terminals.

Requires internet connection to fetch IP and domain info.

Make sure Python 3 is installed and updated.

To exit the tool, simply choose the “Exit” option in the menu.
