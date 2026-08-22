#!/usr/bin/env python3
"""One-click launcher: install deps, start the Flask server, open the browser."""

from __future__ import annotations

import os
import subprocess
import sys
import threading
import time
import webbrowser


PORT = int(os.getenv("PORT", "5000"))
URL = f"http://127.0.0.1:{PORT}"


def _install_deps() -> None:
    req = os.path.join(os.path.dirname(__file__), "requirements.txt")
    print("Installing dependencies…")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "-q", "-r", req],
    )


def _open_browser() -> None:
    time.sleep(1.5)
    webbrowser.open(URL)


def main() -> None:
    _install_deps()
    threading.Thread(target=_open_browser, daemon=True).start()
    print(f"Starting server → {URL}")
    os.environ.setdefault("HOST", "0.0.0.0")
    # Import here so Flask is available after pip install
    import app as _app  # noqa: PLC0415

    _app.app.run(
        host=os.environ["HOST"],
        port=PORT,
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true",
    )


if __name__ == "__main__":
    main()
