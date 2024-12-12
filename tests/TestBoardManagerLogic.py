import pytest
from ScoreStreamPy import BoardManager

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
    
    def test_add_new_match_to_board_raises_error(invalid_team_names):
       manager = BoardManager()
       home_team, away_team = invalid_team_names

       with pytest.raises(ValueError, match="Support not empty strings, regex [a-zA-Z0-9.-], maximum 255 characters."):
        manager.start_match(home_team, away_team)

    @pytest.mark.parametrize("updates", [
    [
        {"home_team": "Argentina", "away_team": "Brasil", "home_score": 3, "away_score": 1, "match_id": "custom1-7e76-0001-bb9e-6aea8aa2d859"},
        {"home_team": "Spain", "away_team": "Germany", "home_score": 2, "away_score": 2, "match_id": "custom2-7e76-0002-bb9e-6aea8aa2d859"},
        {"home_team": "France", "away_team": "Italy", "home_score": 4, "away_score": 5, "match_id": "custom3-7e76-0003-bb9e-6aea8aa2d859"},
    ]
])
    def test_update_score_for_matches(scoreboard_fixture, updates):
        scoreboard = scoreboard_fixture
        matches = []
    
        for update in updates:
            match = scoreboard.start_match(update["home_team"], update["away_team"])
            match.match_id = update["match_id"]
            matches.append({"match": match, "update": update})
        for entry in matches:
            match = entry["match"]
            update = entry["update"]
            scoreboard.update_match(match, update["home_score"], update["away_score"], match.match_id)
        for entry in matches:
            match = entry["match"]
            update = entry["update"]
        
        assert match.home_team == update["home_team"]
        assert match.away_team == update["away_team"]
        assert match.home_score == update["home_score"]
        assert match.away_score == update["away_score"]
        assert match.match_id in scoreboard.matches
        assert match.status == "In progress"

        print(f"Current scoreboard: {match.home_team} {match.home_score} - {match.away_score} {match.away_team}, Status: {match.status}, ID: {match.match_id}")
    
    def test_finish_match():
        manager = BoardManager()
        match = manager.start_match("Mexico", "Canada")
        manager.finish_match(match)

        assert match not in manager.scoreboard.matches

    import pytest

@pytest.mark.parametrize("updates", [
    [
        {"home_team": "Argentina", "away_team": "Brasil", "home_score": 3, "away_score": 1, "match_id": "custom1-7e76-0001-bb9e-6aea8aa2d859"},
        {"home_team": "Spain", "away_team": "Germany", "home_score": 2, "away_score": 2, "match_id": "custom2-7e76-0002-bb9e-6aea8aa2d859"},
        {"home_team": "France", "away_team": "Italy", "home_score": 4, "away_score": 5, "match_id": "custom3-7e76-0003-bb9e-6aea8aa2d859"},
    ]
])
def test_output_scoreboard_summary(scoreboard_fixture, updates):
    """
    Test updating scores for multiple matches and validating list output.
    """
    scoreboard = scoreboard_fixture
    matches = []

    for update in updates:
        match = scoreboard.start_match(update["home_team"], update["away_team"])
        match.match_id = update["match_id"]
        matches.append({"match": match, "update": update})
    for entry in matches:
        match = entry["match"]
        update = entry["update"]
        scoreboard.update_match(match, update["home_score"], update["away_score"], match.match_id)
    expected_output = [
        f"{update['home_team']} {update['home_score']} - {update['away_score']} {update['away_team']}"
        for update in updates
    ]
    result = scoreboard.display_scoreboard()
    assert result == expected_output
    print("Final Scoreboard Output:")
    for line in result:
        print(line)
