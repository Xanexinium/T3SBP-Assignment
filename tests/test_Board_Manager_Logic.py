import pytest
from ScoreStreamPy import BoardManager, ScoreBoard, Match

# Fixture: Provides a BoardManager instance (shared across the module)

@pytest.fixture(scope="module")
def manager():
    return BoardManager()


@pytest.fixture(scope="module")
def shared_match(manager):
    match = manager.add_match_to_board("Mexico", "Canada")
    yield match

    if match.match_id in manager.scoreboard.matches:
        manager.finish_match(match.match_id)
        print(f"Cleanup: Match closed -> {match}")


def test_add_and_verify_match(manager, shared_match):
    assert shared_match.home_team == "Mexico"
    assert shared_match.away_team == "Canada"
    assert shared_match.status == "In progress"
    assert shared_match.match_id in manager.scoreboard.matches
    print(f"Test: Match added -> {shared_match}")


def test_update_match_score(manager, shared_match):
    manager.update_match_score(
        shared_match.match_id, home_score=3, away_score=2)
    updated_match = manager.scoreboard.matches[shared_match.match_id]

    assert updated_match.home_score == 3
    assert updated_match.away_score == 2
    assert updated_match.status == "In progress"
    print(f"Test: Match score updated -> {updated_match}")


def test_finish_match(manager, shared_match):
    manager.finish_match(shared_match.match_id)

    assert shared_match.match_id not in manager.scoreboard.matches
    print(f"Test: Match finished -> {shared_match}")

def test_get_goals_by_team():
    """
    Test the get_goals_by_team method for accurate goal calculation.
    """
   
    scoreboard = ScoreBoard()
    scoreboard.matches = {
        "match1": Match(home_team="Team-A", away_team="Team-B", home_score=3, away_score=1),
        "match2": Match(home_team="Team-C", away_team="Team-A", home_score=2, away_score=4),
        "match3": Match(home_team="Team-A", away_team="Team-D", home_score=1, away_score=0),
    }

    total_goals_team_a = scoreboard.get_goals_by_team("Team-A")

    assert total_goals_team_a == 8, f"Expected 8 goals for Team-A, got {total_goals_team_a}"
    total_goals_team_e = scoreboard.get_goals_by_team("Team-E")
    assert total_goals_team_e == 0, f"Expected 0 goals for Team-E, got {total_goals_team_e}"

    print(f"Total goals for Team-A: {total_goals_team_a}")
    print(f"Total goals for Team-E: {total_goals_team_e}")