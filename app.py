from flask import Flask
import getpass
import subprocess
import datetime
import pytz
import os

app = Flask(__name__)

@app.route("/htop")
def htop():
    full_name = "Parmeshor Shahu Teli"
    username = getpass.getuser()

    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Top output (first 10 lines)
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], universal_newlines=True)
        top_lines = '\n'.join(top_output.splitlines()[:10])
    except Exception as e:
        top_lines = f"Error fetching top: {e}"

    html = f"""
    <html>
    <head><title>/htop</title></head>
    <body>
        <h2>Name: {full_name}</h2>
        <h2>Username: {username}</h2>
        <h2>Server Time (IST): {server_time}</h2>
        <h2>Top Output:</h2>
        <pre>{top_lines}</pre>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)