"""Flask entrypoint for the browser-based game."""

from __future__ import annotations

import os
from uuid import uuid4

from flask import Flask, jsonify, render_template, request, send_from_directory

from api_client import create_game_state, update_game_state


app = Flask(__name__, template_folder="ui", static_folder="static")
GAME_STATES = {}


@app.get("/")
def index() -> str:
    return render_template("index.html")


@app.get("/ui/<path:filename>")
def ui_assets(filename: str):
    return send_from_directory(app.template_folder, filename)


@app.post("/api/start")
def start_game():
    game_id = str(uuid4())
    state = create_game_state()
    update_game_state(state, {"start": True}, 0)
    GAME_STATES[game_id] = state
    return jsonify({"game_id": game_id, "state": state})


@app.get("/api/state/<game_id>")
def get_state(game_id: str):
    state = GAME_STATES.get(game_id)
    if not state:
        return jsonify({"error": "Game not found"}), 404
    return jsonify({"game_id": game_id, "state": state})


@app.post("/api/update")
def update_state():
    payload = request.get_json(silent=True) or {}
    game_id = payload.get("game_id")

    if not game_id or game_id not in GAME_STATES:
        return jsonify({"error": "Invalid or missing game_id"}), 404

    controls = payload.get("input") or {}
    dt = payload.get("dt", 1 / 60)

    state = update_game_state(GAME_STATES[game_id], controls=controls, dt=dt)
    return jsonify({"game_id": game_id, "state": state})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
