from dataclasses import dataclass, replace
import uuid
import re
import time

@dataclass(frozen=True)
class Match:
    home_team: str
    away_team: str
    home_score: int = 0
    away_score: int = 0
    status: str = "Not started"
    match_id: str = None
    start_time: float = None


    def __post_init__(self):
        if not self.match_id:
            object.__setattr__(self, "match_id", uuid.uuid4())
        self._validate_team_name(self.home_team)
        self._validate_team_name(self.away_team)
        if self.home_team == self.away_team:
            raise ValueError("Home team and away team cannot be the same.")
        if self.start_time is None:
            object.__setattr__(self, "start_time", time.time())

    def _validate_team_name(self, team: str):
        if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', team):
            raise ValueError("Team names must match regex [a-zA-Z0-9.-], max 255 characters.")

    def update_score(self, home_score: int, away_score: int):
        if home_score < 0 or away_score < 0:
            raise ValueError("Scores must be positive integers.")
        return replace(self, home_score=self.home_score + home_score, away_score=self.away_score + away_score)
        

    def finish(self):
        return replace(self, status="Finished")

    def get_total_score(self) -> int:
        return self.home_score + self.away_score

    def __repr__(self):
        return f"{self.home_team} {self.home_score} - {self.away_team} {self.away_score}, {self.status}, {self.match_id}"
    
