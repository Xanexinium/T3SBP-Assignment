import threading
from typing import Dict
from ScoreStreamPy import Match


class ScoreBoard:
    def __init__(self):
        self.matches: Dict[str, Match] = {} 
        self.lock = threading.Lock()

    def start_match(self, home_team: str, away_team: str) -> Match:
        """
        Creates and adds a new Match object with status 'In progress'.
        """
        match = Match(home_team=home_team, away_team=away_team, status="In progress")
        with self.lock:
            self.matches[match.match_id] = match
        return match

    def update_match(self, match_id: str, home_score: int, away_score: int):
        """
        Updates the score of a match identified by match_id.
        """
        with self.lock:
            if match_id in self.matches:
                match = self.matches[match_id]
                # Replace the match with a new instance having updated scores
                self.matches[match_id] = match.update_score(home_score, away_score)
            else:
                raise ValueError("Match not found in the scoreboard.")

    def finish_match(self, match_id: str):
        """
        Marks a match as finished and removes it from the scoreboard.
        """
        with self.lock:
            if match_id in self.matches:
                match = self.matches.pop(match_id)
                finished_match = match.finish()
                return finished_match  # Optionally return the finished match
            else:
                raise ValueError("Match not found in the scoreboard.")

    def get_summary(self) -> list:
        """
        Returns all matches in progress, sorted by total score and then by the most recently started match.
        """
        with self.lock:
            ongoing_matches = [
                match for match in self.matches.values() if match.status == "In progress"
            ]
        return sorted(
            ongoing_matches,
            key=lambda match: (match.get_total_score(), -match.start_time),
            reverse=True
        )

    def __repr__(self):
        """
        String representation of the scoreboard.
        """
        with self.lock:
            return "\n".join(str(match) for match in self.matches.values())
