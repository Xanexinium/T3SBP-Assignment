import pytest
from ScoreStreamPy import BoardManager

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
    manager.update_match_score(shared_match.match_id, home_score=3, away_score=2)
    updated_match = manager.scoreboard.matches[shared_match.match_id]

    assert updated_match.home_score == 3
    assert updated_match.away_score == 2
    assert updated_match.status == "In progress"
    print(f"Test: Match score updated -> {updated_match}")

def test_finish_match(manager, shared_match):
    manager.finish_match(shared_match.match_id)

    assert shared_match.match_id not in manager.scoreboard.matches
    print(f"Test: Match finished -> {shared_match}")
