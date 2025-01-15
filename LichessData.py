import berserk
from datetime import datetime
from dateutil.relativedelta import relativedelta
from config import API_TOKEN
# berserk is a Python package designed to be used with Lichess's API

# Establishes session, creates berserk client object which makes authenticated requests on Lichess and handles API responses
def create_client():
    session = berserk.TokenSession(API_TOKEN)
    return berserk.client(session=session)
    
def get_games(
        client,
        from_rating=1300,
        to_rating=1400,
        player='daichijoseph41664',
        rated=True,
        time_control='rapid',
        num_games=50
):
    """Fetch games by player from the last month"""

    end = datetime.now()
    start = end - relativedelta(months=1)
    games = client.games.export_by_player(
        username=player,
        since=berserk.utils.to_millis(start),
        until=berserk.utils.to_millis(end),
        max=num_games,
        perf_type=time_control
    )

    filtered_games = []
    for game in games:
        white_rating = game['players']['white'].get('rating', 0)
        black_rating = game['players']['black'].get('rating', 0)
        if (from_rating <= white_rating <= to_rating and from_rating <= black_rating <= to_rating):
            filtered_games.append(game)
    return filtered_games
