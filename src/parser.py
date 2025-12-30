import json
import requests

def load_scoreboard(path: str) -> dict:
    """
    Load ESPN scoreboard JSON from a file.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to load scoreboard JSON: {e}")


def get_live_games(scoreboard: dict) -> list[dict]:
    """
    Return only live games.
    """
    games = []

    for event in scoreboard.get("events", []):
        competition = _get_competition(event)
        if not competition:
            continue

        state = competition["status"]["type"]["state"]
        if state == "in":
            games.append(_parse_game(event, competition))

    return games


def get_all_games(scoreboard: dict) -> list[dict]:
    """
    Return all games (scheduled, live, final).
    """
    games = []

    for event in scoreboard.get("events", []):
        competition = _get_competition(event)
        if competition:
            games.append(_parse_game(event, competition))

    return games

def load_scoreboard_from_url(url: str) -> dict:
    """
    Fetch scoreboard JSON from a URL (like ESPN API)
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch scoreboard from URL: {e}")


# Helper Functions

def _get_competition(event: dict) -> dict | None:
    competitions = event.get("competitions", [])
    return competitions[0] if competitions else None


def _parse_game(event: dict, competition: dict) -> dict:
    competitors = competition["competitors"]

    home = next(c for c in competitors if c["homeAway"] == "home")
    away = next(c for c in competitors if c["homeAway"] == "away")

    status = competition["status"]["type"]

    # format of JSON file
    return {
        "id": event["id"],
        "name": event["name"],
        "home_team": home["team"]["displayName"],
        "away_team": away["team"]["displayName"],
        "home_score": int(home.get("score", 0)),
        "away_score": int(away.get("score", 0)),
        "home_logo": home["team"]["logo"],
        "away_logo": away["team"]["logo"],
        "clock": competition["status"]["displayClock"],
        "period": competition["status"]["period"],
        "state": status["state"],
        "detail": status["shortDetail"]
    }
