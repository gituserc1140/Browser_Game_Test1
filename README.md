# Asteroid Dodger (Browser Game)

Dodge falling asteroids for as long as possible.

## Quick start (one command)

```bash
python launch.py
```

That's it. `launch.py` will:
1. Install the required Python packages automatically.
2. Start the local game server.
3. Open your default browser at `http://127.0.0.1:5000`.

**Requirements:** Python 3.9 or later (no other installs needed beforehand).

## Manual start (if you prefer)

```bash
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Play on your phone (same Wi-Fi)

1. Start the server with LAN mode enabled:
   ```bash
   HOST=0.0.0.0 python launch.py
   ```
2. Find your computer's local IP (e.g. `192.168.1.25`).
3. On your phone, open: `http://<your-computer-ip>:5000`
4. Use the on-screen D-pad — it appears automatically on touch devices.

## Controls

| Input | Action |
|---|---|
| Arrow keys / WASD | Move the ship |
| On-screen D-pad | Move the ship (mobile / touch) |
| Start / Play Again button | Begin or restart |

Every asteroid that flies past scores a point. Collisions cost health. The game ends when health reaches 0.

## Repository layout

- `launch.py` — one-click launcher
- `app.py` — Flask server (UI + game state endpoints)
- `api_client.py` — core game logic (physics, collisions, entities)
- `ui/` — HTML / CSS / JavaScript front-end
- `static/` — game assets (sprites, images, sounds)
- `config/` — gameplay constants

## API endpoints

- `POST /api/start` — create and start a new game
- `POST /api/update` — send input + `dt`, receive updated state JSON
- `GET /api/state/<game_id>` — fetch current state JSON

