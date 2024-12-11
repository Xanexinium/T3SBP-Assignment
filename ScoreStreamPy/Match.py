import threading
import time
import re

class Match:
    def __init__(self, home_team: str, away_team: str,
                    home_score:int = 0, away_score: int = 0):
        self._validate_team_name(home_team)
        self._validate_team_name(away_team)
        self._validate_same_team(home_team,away_team)
        self.home_team = home_team
        self.away_team = away_team
        self.start_time = time.time()
        self.match_id = int(self.start_time * 1000)
        self.home_score = home_score
        self.away_score = away_score
        self.status = "Not started"
        self.lock = threading.Lock()

    def _validate_team_name(self, team: str):
        if not isinstance(team, str) or not re.match(r'^[a-zA-Z0-9.-]{1,255}$', team):
            raise ValueError("Support not empty strings, regex [a-zA-Z0-9.-], maximum 255 characters.")
        
    def _validate_same_team(self, home_team, away_team):
        if home_team == away_team:
            raise ValueError("Home team and away team cannot be the same.")

    def _validate_if_integer(self, validate_value: int):
        if not isinstance(validate_value, int):
            raise ValueError(f"Expected positive integer value.")
        if validate_value < 0:
            raise ValueError(f"Expected positive integer value.")

    def update_score(self, home_score: int, away_score: int):
        self._validate_if_integer(home_score)
        self._validate_if_integer(away_score)
        with self.lock:
            self.home_score = home_score
            self.away_score = away_score

    def finish(self):
        self.status = "Finished"

    def __str__(self):
        return f"{self.home_team} {self.home_score} - {self.away_team} {self.away_score}"

    def get_total_score(self) -> int:
        return self.home_score + self.away_score