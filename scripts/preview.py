from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os


PROJECT_ROOT = Path(__file__).resolve().parents[1]
os.chdir(PROJECT_ROOT)


if __name__ == "__main__":
    address = ("127.0.0.1", 8000)
    print(f"Preview: http://localhost:{address[1]}/?voor=tim")
    print("Stop met Ctrl+C")
    ThreadingHTTPServer(address, SimpleHTTPRequestHandler).serve_forever()
