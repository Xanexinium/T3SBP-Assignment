import threading
from ScoreStreamPy import Match, ScoreBoard

class BoardManager:
    def __init__(self):
        self.scoreboard = ScoreBoard()
        self.lock = threading.Lock()

    def add_match_to_board(self, home_team: str, away_team: str, match_id: str = None) -> Match:
        """
        Adds a new match to the scoreboard and sets it to 'In progress'.
        """
        with self.lock:
            match = self.scoreboard.start_match(home_team, away_team)
            if match_id:
                match.match_id = match_id 
            return match

    def update_match_score(self, match_id: str, home_score: int, away_score: int):
        """
        Updates the score for an existing match in the scoreboard.
        """
        with self.lock: 
            if match_id not in self.scoreboard.matches:
                raise ValueError("Match not found in the scoreboard.")
            match = self.scoreboard.matches[match_id]
            match.update_score(home_score, away_score)

    def finish_match(self, match_id: str):
        """
        Finishes a match and removes it from the scoreboard.
        """
        with self.lock:  
            if match_id not in self.scoreboard.matches:
                raise ValueError("Match not found in the scoreboard.")
            match = self.scoreboard.matches[match_id]
            self.scoreboard.finish_match(match, match_id)

    def get_scoreboard_summary(self) -> list:
        """
        Retrieves a summary of all ongoing matches in a formatted numbered list.
        """
        with self.lock:  # Ensure thread safety when accessing matches
            summary = self.scoreboard.get_summary()
            return [
                f"{index + 1}. {match.home_team} {match.home_score} - {match.away_score} {match.away_team}"
                for index, match in enumerate(summary)
            ]

    def display_scoreboard(self):
        """
        Prints the formatted scoreboard summary.
        """
        summary = self.get_scoreboard_summary()
        for line in summary:
            print(line)

