import pytest
import threading
import time
from ScoreStreamPy import ScoreBoard


@pytest.fixture
def scoreboard_fixture():
    return ScoreBoard()


class TestThreadScoreBoard:

    def test_start_match_thread_safety(self, scoreboard_fixture):
        """
        Test starting multiple matches concurrently to check thread safety.
        """
        scoreboard = scoreboard_fixture
        threads = []

        def start_match_in_thread(home_team, away_team):
            match = scoreboard.start_match(home_team, away_team)

        for i in range(10):
            thread = threading.Thread(
                target=start_match_in_thread,
                args=(f"Team{i}", f"Team{i+10}")
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        assert len(scoreboard.matches) == 10

    def test_update_match_thread_safety(self, scoreboard_fixture):
        """
        Test updating matches concurrently to ensure thread safety.
        """
        scoreboard = scoreboard_fixture
        match = scoreboard.start_match("TeamA", "TeamB")

        threads = []

        def update_match_in_thread(match_id):
            for _ in range(100):
                scoreboard.update_match(match, 1, 1, match_id)

        for _ in range(10):
            thread = threading.Thread(
                target=update_match_in_thread, args=(match.match_id,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        assert match.home_score == 1000
        assert match.away_score == 1000

    def test_finish_match_thread_safety(self, scoreboard_fixture):
        """
        Test finishing matches concurrently to ensure thread safety.
        """
        scoreboard = scoreboard_fixture

        # Start multiple matches
        matches = [scoreboard.start_match(
            f"Team{i}", f"Team{i+10}") for i in range(5)]
        threads = []

        def finish_match_in_thread(match_id):
            try:
                scoreboard.finish_match(
                    matches[match_id], matches[match_id].match_id)
            except ValueError as e:
                print(e)

        # Start threads to finish matches
        for i in range(5):
            thread = threading.Thread(target=finish_match_in_thread, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        assert len(scoreboard.matches) == 0

    def test_get_summary_thread_safety(self, scoreboard_fixture):
        """
        Test getting summary while updates happen concurrently.
        """
        scoreboard = scoreboard_fixture

        match1 = scoreboard.start_match("TeamA", "TeamB")
        match2 = scoreboard.start_match("TeamC", "TeamD")

        def update_match_scores():
            for _ in range(100):
                scoreboard.update_match(match1, 1, 0, match1.match_id)
                scoreboard.update_match(match2, 0, 1, match2.match_id)
        threads = []
        for _ in range(5):
            thread = threading.Thread(target=update_match_scores)
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        summary = scoreboard.get_summary()

        assert len(summary) == 2
        assert summary[0].get_total_score() >= summary[1].get_total_score()
