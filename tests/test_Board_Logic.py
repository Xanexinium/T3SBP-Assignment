import pytest
from ScoreStreamPy import Match
from ScoreStreamPy import ScoreBoard

# Fixtures needed in test


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
        print(match)
        assert match.status == "In progress"
        assert match.home_team == "Argentina"
        assert match.away_team == "Brazil"
        assert match.match_id in scoreboard.matches
        assert scoreboard.matches[match.match_id] == match

    def test_update_match(self, scoreboard_fixture):
        scoreboard = scoreboard_fixture
        match = scoreboard.start_match("Argentina", "Brazil")

        match_id = match.match_id
        scoreboard.update_match(match, 3, 2, match_id)

        updated_match = scoreboard.matches[match_id]
        assert updated_match.home_score == 3
        assert updated_match.away_score == 2
        assert updated_match.get_total_score() == 5

    def test_update_match_not_found(self, scoreboard_fixture, match_fixture):
        scoreboard = scoreboard_fixture
        with pytest.raises(ValueError, match="Match not found in the scoreboard."):
            scoreboard.update_match(match_fixture, 1, 1, 123456)

    def test_finish_match(self, scoreboard_fixture):
        scoreboard = scoreboard_fixture
        match = scoreboard.start_match("Spain", "Italy")

        match_id = match.match_id
        scoreboard.finish_match(match, match_id)

        assert match_id not in scoreboard.matches
        assert match.status == "Finished"

    def test_finish_match_not_found(self, scoreboard_fixture, match_fixture):
        scoreboard = scoreboard_fixture
        with pytest.raises(ValueError, match="Match not found in the scoreboard."):
            scoreboard.finish_match(match_fixture, 123456)


class TestScoreBoardLogic:

    def test_get_summary(self, scoreboard_fixture):
        scoreboard = scoreboard_fixture

        match1 = scoreboard.start_match("Mexico", "Canada")
        print(f"Started match: {match1}")
        match2 = scoreboard.start_match("Spain", "Brasil")
        print(f"Started match: {match2}")
        match3 = scoreboard.start_match("Germany", "France")
        print(f"Started match: {match3}")
        match4 = scoreboard.start_match("Uruguay", "Italy")
        print(f"Started match: {match4}")
        match5 = scoreboard.start_match("Argentina", "Australia")
        print(f"Started match: {match5}")

        scoreboard.update_match(match1, 0, 5, match1.match_id)
        scoreboard.update_match(match2, 10, 2, match2.match_id)
        scoreboard.update_match(match3, 2, 2, match3.match_id)
        scoreboard.update_match(match4, 6, 6, match4.match_id)
        scoreboard.update_match(match5, 3, 1, match5.match_id)
        summary = scoreboard.get_summary()
        print(summary)

        assert len(summary) == 5
        assert summary[0] == match4
        assert summary[1] == match2
        assert summary[2] == match1
        assert summary[3] == match5
        assert summary[4] == match3

    def test_repr(self, scoreboard_fixture):
        """Test string representation of the scoreboard."""
        scoreboard = scoreboard_fixture

        match1 = scoreboard.start_match("TeamA", "TeamB")
        match2 = scoreboard.start_match("TeamC", "TeamD")

        expected_output = "\n".join([str(match1), str(match2)])
        assert repr(scoreboard) == expected_output
