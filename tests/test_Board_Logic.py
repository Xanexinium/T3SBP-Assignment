import pytest
import uuid
from ScoreStreamPy import Match
from ScoreStreamPy import ScoreBoard

@pytest.fixture
def match_fixture():
    return Match("Argentina", "Brasil")


@pytest.fixture
def scoreboard_fixture():
    return ScoreBoard()

class TestScoreBoardMethods:
    def test_start_match(self, scoreboard_fixture):
        scoreboard = scoreboard_fixture
        match = scoreboard.start_match("Argentina", "Brazil")

        assert match.status == "In progress"
        assert match.home_team == "Argentina"
        assert match.away_team == "Brazil"
        assert match.match_id in scoreboard.matches
        assert scoreboard.matches[match.match_id] == match

    def test_update_match(self, scoreboard_fixture):
        scoreboard = scoreboard_fixture
        match = scoreboard.start_match("Argentina", "Brazil")

        match_id = match.match_id
        scoreboard.update_match(match_id, 3, 2)

        updated_match = scoreboard.matches[match_id]
        assert updated_match.home_score == 3
        assert updated_match.away_score == 2
        assert updated_match.get_total_score() == 5

    def test_update_match_not_found(self, scoreboard_fixture, match_fixture):
        scoreboard = scoreboard_fixture
        with pytest.raises(ValueError, match="Match not found in the scoreboard."):
            scoreboard.update_match("nonexistent-id", 1, 1)

    def test_finish_match(self, scoreboard_fixture):
        scoreboard = scoreboard_fixture
        match = scoreboard.start_match("Spain", "Italy")

        match_id = match.match_id
        finished_match = scoreboard.finish_match(match_id)

        assert match_id not in scoreboard.matches

        assert finished_match.status == "Finished"

    def test_finish_match_not_found(self, scoreboard_fixture, match_fixture):
        scoreboard = scoreboard_fixture
        with pytest.raises(ValueError, match="Match not found in the scoreboard."):
            scoreboard.finish_match("nonexistent-id")


class TestScoreBoardLogic:
    def test_get_summary(self, scoreboard_fixture):
        scoreboard = scoreboard_fixture

        match1 = scoreboard.start_match("Mexico", "Canada")
        match2 = scoreboard.start_match("Spain", "Brasil")
        match3 = scoreboard.start_match("Germany", "France")
        match4 = scoreboard.start_match("Uruguay", "Italy")
        match5 = scoreboard.start_match("Argentina", "Australia")

        scoreboard.update_match(match1.match_id, 0, 5)
        scoreboard.update_match(match2.match_id, 10, 2)
        scoreboard.update_match(match3.match_id, 2, 2)
        scoreboard.update_match(match4.match_id, 6, 6)
        scoreboard.update_match(match5.match_id, 3, 1)

        summary = scoreboard.get_summary()

        assert len(summary) == 5
        assert summary[0].get_total_score() == 12
        assert summary[1].get_total_score() == 12
        assert summary[2].get_total_score() == 5
        assert summary[3].get_total_score() == 4
        assert summary[4].get_total_score() == 4

    def test_repr(self, scoreboard_fixture):
        """Test string representation of the scoreboard."""
        scoreboard = scoreboard_fixture

        match1 = scoreboard.start_match("TeamA", "TeamB")
        match2 = scoreboard.start_match("TeamC", "TeamD")

        expected_output = "\n".join([str(match1), str(match2)])
        assert repr(scoreboard) == expected_output
