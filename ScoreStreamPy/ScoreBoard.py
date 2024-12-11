import threading
from ScoreStreamPy import Match

class ScoreBoard:
    def __init__(self):
        self.matches = {}
        self.lock = threading.Lock()

    def start_match(self, home_team: str, away_team: str) -> Match:
        """
        Creates new Match object with status Started.
        """
        match = Match(home_team, away_team)
        with self.lock:
            self.matches[match.match_id] = match
            match.status = "In progress"
        return match

    def update_match(self, match: Match, home_score: int, away_score: int, match_id):
        """
        Updates the score of started match.
        """
        with self.lock:
            if match_id in self.matches:
                match.update_score(home_score, away_score)
            else:
                raise ValueError("Match not found in the scoreboard.")

    def finish_match(self, match: Match, match_id):
        """
        Remove a match from the scoreboard, marking it as finished.
        """
        with self.lock:
            if match_id in self.matches:
                match = self.matches.pop(match_id)
                match.finish()
            else:
                raise ValueError("Match not found in the scoreboard.")