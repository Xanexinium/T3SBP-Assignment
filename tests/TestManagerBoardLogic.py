
import pytest
from ScoreStreamPy import ScoreManager

@pytest.fixture
def match_fixture_correct():
    manager = ScoreManager()
    match = manager.add_match_to_board(
        "Argentina", "Brasil", 
        "333ec514-7e76-4901-bb9e-6aea8aa2d859"
    )
    return match

@pytest.fixture
def match_fixture_invalid():
    return "!@(())", "Brasil"


class TestBoardManager:
    
    def test_add_new_match_to_board_positive(match_fixture_correct):
        match = match_fixture_correct  # Fixture automatically passed as an argument
    
    assert match.home_team == "Argentina"
    assert match.away_team == "Brasil"
    assert match.home_score == 0
    assert match.away_score == 0
    assert match.match_id != 0
    assert match.status == "In progress"
    
    def add_new_match_to_board_raises_error(invalid_team_names):
       manager = ScoreManager()
       home_team, away_team = invalid_team_names

       with pytest.raises(ValueError, match="Support not empty strings, regex [a-zA-Z0-9.-], maximum 255 characters."):
        manager.start_match(home_team, away_team)


    