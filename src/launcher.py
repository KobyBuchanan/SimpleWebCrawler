import threading
import webbrowser
import uvicorn
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parent))

def run_server():
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="warning"
    )

threading.Thread(target=run_server, daemon=True).start()
webbrowser.open("http://127.0.0.1:8000")

input("Press ENTER to quit...")
