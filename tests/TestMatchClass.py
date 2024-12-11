import pytest
import re
from ScoreStreamPy.Match import Match

import pytest
import re
from ScoreStreamPy.Match import Match


class TestMatchTeamValidate:

    @pytest.mark.parametrize("home_team, away_team, expected_message", [
    ("A" * 256, "Croatia", "Support not empty strings, regex [a-zA-Z0-9.-], maximum 255 characters."),
    ("Slovenia", "B" * 256, "Support not empty strings, regex [a-zA-Z0-9.-], maximum 255 characters."),
    ("@&?///", "Croatia", "Support not empty strings, regex [a-zA-Z0-9.-], maximum 255 characters."),
    ("Slovenia", "", "Support not empty strings, regex [a-zA-Z0-9.-], maximum 255 characters."),
    (" ","Slovenia", "Support not empty strings, regex [a-zA-Z0-9.-], maximum 255 characters."),
    ])
    def test_validation_team_name_error_dispatched(self, home_team, 
                                                   away_team, expected_message):
        escaped_message = re.escape(expected_message)
        with pytest.raises(ValueError, match=escaped_message):
            Match(home_team, away_team)
    
    @pytest.mark.parametrize("home_team, away_team, expected_message", [
    ("Slovenia", "Slovenia", "Home team and away team cannot be the same."),
    ])
    def test_validation_same_team(self, home_team,
                                    away_team, expected_message):
        with pytest.raises(ValueError, match=expected_message):
            Match(home_team, away_team)

class TestMatchScoreValidate:
  
    @pytest.mark.parametrize("home_score, away_score, expected_message", [
    ("Abc", -2, "Expected positive integer value."),
    (-1, "Xyz", "Expected positive integer value."),
    (1, "Xyz", "Expected positive integer value."),
    ("Adb", "1", "Expected positive integer value."),
    ("1","Adb", "Expected positive integer value."),
    ("Home", "Away", "Expected positive integer value."),
    ])
    def test_validation_message_update_score_dispatched(self, home_score, away_score, expected_message):
        match = Match("TeamA", "TeamB")
        with pytest.raises(ValueError, match=expected_message):
            match.update_score(home_score, away_score)

class TestMatchClassMethods:
    
    @pytest.mark.parametrize("home_team, away_team, home_score, away_score", [
    ("Argentina", "Jamaica", 0, 0),
    ])
    def test_start_new_match(self, home_team, away_team,
                              home_score, away_score):
        match = Match(home_team, away_team)
        print(match)
        assert match.home_team == "Argentina"
        assert match.away_team == "Jamaica"
        assert match.home_score == 0
        assert match.away_score == 0
    
    @pytest.mark.parametrize("home_team, away_team, home_score, away_score", [
    ("Argentina", "Jamaica", 5, 0),
    ])
    def test_update_score(self, home_team, away_team, home_score, away_score):
        match = Match(home_team, away_team, home_score, away_score)
        match.update_score(5, 0)
        print(match)
        assert match.home_score == 5
        assert match.away_score == 0
    
    @pytest.mark.parametrize("home_team, away_team, home_score, away_score", [
    ("Argentina", "Jamaica", 5, 3),
    ])
    def test_total_score(self, home_team, away_team, home_score, away_score):
        match = Match(home_team, away_team, home_score, away_score)
        total_score = match.get_total_score()
        print("Total score is", total_score)
        assert total_score == (home_score + away_score)