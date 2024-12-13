import pytest
import threading
from ScoreStreamPy import BoardManager


@pytest.fixture
def board_manager_fixture():
    """
    Fixture to provide a fresh instance of BoardManager.
    """
    return BoardManager()


class TestBoardManagerThreadSafety:
    def test_add_match_thread_safety(self, board_manager_fixture):
        """
        Test that multiple threads can safely add matches to the BoardManager.
        """
        manager = board_manager_fixture
        threads = []

        def add_match():
            for _ in range(100):
                manager.add_match_to_board("TeamA", "TeamB")

        # Launch multiple threads
        for _ in range(10):
            thread = threading.Thread(target=add_match)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Verify the total number of matches added
        total_matches = len(manager.scoreboard.matches)
        assert total_matches == 1000, f"Expected 1000 matches, got {total_matches}"

    def test_update_match_thread_safety(self, board_manager_fixture):
        """
        Test that multiple threads can safely update scores for the same match.
        """
        manager = board_manager_fixture
        match = manager.add_match_to_board("TeamA", "TeamB")

        threads = []

        def update_score():
            for _ in range(100):
                manager.update_match_score(match.match_id, 1, 1)

        # Launch multiple threads to update the match score
        for _ in range(10):
            thread = threading.Thread(target=update_score)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Verify the final score
        assert match.home_score == 1000, f"Expected home_score to be 1000, got {match.home_score}"
        assert match.away_score == 1000, f"Expected away_score to be 1000, got {match.away_score}"

    def test_finish_match_thread_safety(self, board_manager_fixture):
        """
        Test that multiple threads can safely finish matches.
        """
        manager = board_manager_fixture
        match = manager.add_match_to_board("TeamA", "TeamB")

        threads = []

        def finish_match():
            try:
                manager.finish_match(match.match_id)
            except ValueError:
                pass  # Allow for exceptions when trying to finish already removed matches

        # Launch multiple threads to finish the same match
        for _ in range(10):
            thread = threading.Thread(target=finish_match)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Verify the match has been removed
        assert match.match_id not in manager.scoreboard.matches, "Match should be removed from scoreboard"

    def test_combined_thread_safety(self, board_manager_fixture):
        """
        Test that add, update, and finish operations work concurrently without race conditions.
        """
        manager = board_manager_fixture
        match_ids = []

        def add_matches():
            for _ in range(100):
                match = manager.add_match_to_board("TeamA", "TeamB")
                match_ids.append(match.match_id)

        def update_matches():
            for match_id in match_ids:
                try:
                    manager.update_match_score(match_id, 1, 1)
                except ValueError:
                    pass  # Match might have been finished already

        def finish_matches():
            for match_id in match_ids:
                try:
                    manager.finish_match(match_id)
                except ValueError:
                    pass  # Match might have been already finished

        # Launch threads for add, update, and finish operations
        add_thread = threading.Thread(target=add_matches)
        update_thread = threading.Thread(target=update_matches)
        finish_thread = threading.Thread(target=finish_matches)

        add_thread.start()
        add_thread.join()  # Ensure matches are added before updating and finishing

        update_thread.start()
        finish_thread.start()

        update_thread.join()
        finish_thread.join()

        # Verify all matches are removed
        assert len(
            manager.scoreboard.matches) == 0, "All matches should be finished and removed"
