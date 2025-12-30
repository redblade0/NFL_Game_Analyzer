from parser import load_scoreboard_from_url, get_live_games, get_all_games
import cli

SCOREBOARD_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

def main():
    # Fetch live scoreboard JSON from ESPN
    scoreboard = load_scoreboard_from_url(SCOREBOARD_URL)

    live_games = get_live_games(scoreboard)

    if live_games:
        cli.show_live_games_header()
        games_to_show = live_games
    else:
        cli.show_no_games_message()
        cli.show_all_games_header()
        games_to_show = get_all_games(scoreboard)

    cli.display_games(games_to_show)

    while True:
        game = cli.prompt_user_selection(games_to_show)
        if game is None:
            print("Exiting.")
            break

        cli.show_game_details(game)


if __name__ == "__main__":
    main()
