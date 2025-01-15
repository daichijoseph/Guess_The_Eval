import berserk
from config import API_TOKEN
# berserk is a Python package designed to be used with Lichess's API

# Establishes session, creates berserk client object which makes authenticated requests on Lichess and handles API responses
def create_client():
    session = berserk.TokenSession(API_TOKEN)
    return berserk.client(session=session)

