
def display_games(games: list[dict]):
    """
    Display all games. Live and finished for current games.
    """
    for i, game in enumerate(games, start=1):
        print(f"{i}. {game['away_team']} vs {game['home_team']} ({game['detail']})")


def prompt_user_selection(games: list[dict]):
    while True:
        choice = input("\nEnter game number to view (q to quit): ").strip()

        if choice.lower() == "q":
            return None

        if not choice.isdigit():
           print("Please enter a valid number.")
           continue

        index = int(choice) - 1
        if 0 <= index < len(games):
            return games[index]

        print("This number is invalid, choose one shown on the screen.")



def show_game_details(game: dict):
    print("\n==============================")
    print(game["name"])
    print("==============================")
    print(f"{game['away_team']}: {game['away_score']}")
    print(f"{game['home_team']}: {game['home_score']}")
    print(f"Clock: {game['clock']} | Period: {game['period']}")
    print("==============================\n")


def show_no_games_message():
    print("No live games at the moment.\n")


def show_live_games_header():
    print("Live games:\n")


def show_all_games_header():
    print("Showing scheduled games:\n")
