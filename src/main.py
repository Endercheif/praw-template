from os import getenv
import sqlite3
from json import loads

from typing import Dict, Any

import praw

from dotenv import load_dotenv
load_dotenv()



class SQLite3:
    def __init__(self, db: str) -> None:
        self.conn = sqlite3.connection(db)

    def __enter__(self) -> sqlite3.Cursor:
        return self.conn.cursor()

    def __exit__(self, type, value, traceback) -> None:
        self.conn.commit()
        


class RedditBot:
    """A simple class for a Reddit bot."""

    def __init__(self) -> None:

        self.reddit = praw.Reddit(
            client_id=getenv('CLIENT_ID'),
            client_secret=getenv('CLIENT_SECRET'),
            username=getenv('USERNAME'),
            password=getenv('PASSWORD'),
            user_agent='A simple Reddit Bot by /u/YOURUSERNAME',
        )

        self.subreddit = self.reddit.subreddit(getenv('SUBREDDIT'))

        self.conn = SQLite3('data.db')

    def init_db(self) -> None:
        with self.conn as curr:
            curr.execute("""CREATE TABLE IF NOT EXISTS
            tablename(arg TYPE, arg2 TYPE)""", [table])

    def get_config(self, section: str) -> Dict[str, Any]:
        return loads(self.subreddit.wiki[f'{getenv("USERNAME")}/{section}'])
        

