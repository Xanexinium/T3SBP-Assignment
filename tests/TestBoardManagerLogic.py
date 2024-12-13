import pytest
import re
from ScoreStreamPy import BoardManager
from ScoreStreamPy import Match

@pytest.fixture
def match_fixture_correct():
    manager = BoardManager()
    match = manager.add_match_to_board(
        "Argentina", "Brasil", 
        "333ec514-7e76-4901-bb9e-6aea8aa2d859"
    )
    return match

@pytest.fixture
def match_fixture_invalid():
    return "!@(())", "Brasil"

class TestBoardManager:
    
    def test_add_new_match_to_board_positive(self, match_fixture_correct):
        match = match_fixture_correct
        
        assert match.home_team == "Argentina"
        assert match.away_team == "Brasil"
        assert match.home_score == 0
        assert match.away_score == 0
        assert match.match_id != 0
        assert match.status == "In progress"
    
    def test_add_new_match_to_board_raises_error(self, match_fixture_invalid):
        manager = BoardManager()
        home_team, away_team = match_fixture_invalid
        expected_message = "Support not empty strings, regex [a-zA-Z0-9.-], maximum 255 characters."
        with pytest.raises(ValueError, match=re.escape(expected_message)):
            manager.add_match_to_board(home_team, away_team)

    @pytest.mark.parametrize("home_score, away_score, match_id", [
        (1, 2, "333ec514-7e76-4901-bb9e-6aea8aa2d859"),
    ])
    def test_update_score_for_matches(self, home_score, away_score, match_id):
        manager = BoardManager()
        manager.add_match_to_board("TeamA", "TeamB", match_id)
        manager.update_match_score(match_id, home_score, away_score)
    
        updated_match = manager.scoreboard.matches[match_id]
    
        assert updated_match.home_score == home_score
        assert updated_match.away_score == away_score
        assert updated_match.match_id == match_id
        
        print(f"Updated Match: {updated_match}")
