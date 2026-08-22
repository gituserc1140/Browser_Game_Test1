# Asteroid Dodger (Browser Game)

This repository now uses the original template architecture as a browser-based game:

- `app.py` — Flask server for UI and game state endpoints
- `api_client.py` — core game logic (state, physics, collisions, entity updates)
- `ui/` — HTML/CSS/JavaScript front-end with a `<canvas>` render loop
- `static/` — game assets (sprites, images, sound)
- `config/` — gameplay configuration constants

## Gameplay

Dodge falling asteroids for as long as possible.

- Move with **Arrow Keys** or **WASD**
- Every missed asteroid increases score
- Collisions reduce health
- Game ends when health reaches 0

## Run locally

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Start the server

```bash
python app.py
```

3. Open your browser at:

```text
http://127.0.0.1:5000
```

## API endpoints

- `POST /api/start` — create and start a new game
- `POST /api/update` — send input + `dt`, receive updated state JSON
- `GET /api/state/<game_id>` — fetch current state JSON
