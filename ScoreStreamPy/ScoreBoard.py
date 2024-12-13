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
                self.matches[match_id].update_score(home_score, away_score)
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

    def get_summary(self) -> list:
        """
        Returns all matches in progress, sorted by total score and ordered by the most recently started match in the
scoreboard.
        """
        with self.lock:
            ongoing_matches = [
                match for match in self.matches.values() if match.status == "In progress"]
            return sorted(
                ongoing_matches,
                key=lambda match: (match.get_total_score(), match.start_time),
                reverse=True
            )

    def __repr__(self):
        """String representation of the scoreboard."""
        return "\n".join(str(match) for match in self.matches.values())
