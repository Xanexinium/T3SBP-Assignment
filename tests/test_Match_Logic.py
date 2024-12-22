import unittest
import uuid
from ScoreStreamPy import Match

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.match = Match(home_team="Portugal", away_team="Spain")
    
    def test_initialization(self):
        self.assertEqual(self.match.home_team, "Portugal")
        self.assertEqual(self.match.away_team, "Spain")
        self.assertEqual(self.match.home_score, 0)
        self.assertEqual(self.match.away_score, 0)
        self.assertEqual(self.match.status, "Not started")
        self.assertTrue(isinstance(self.match.match_id, uuid.UUID))
    
    def test_update_score_creates_new_instance(self):
        new_match = self.match.update_score(1, 2)
        self.assertNotEqual(self.match, new_match)
        self.assertEqual(new_match.home_score, 1)
        self.assertEqual(new_match.away_score, 2)
        self.assertEqual(self.match.home_score, 0)
        self.assertEqual(self.match.away_score, 0)  
    
    def test_finish_creates_new_instance(self):
        finished_match = self.match.finish()
        self.assertNotEqual(self.match, finished_match)
        self.assertEqual(finished_match.status, "Finished")
        self.assertEqual(self.match.status, "Not started")  # Original match remains unchanged
    
    def test_immutability_over_multiple_operations(self):
        # Update score
        updated_match = self.match.update_score(3, 1)
        # Finish match
        finished_match = updated_match.finish()
        
        # Validate original match remains unchanged
        self.assertEqual(self.match.home_score, 0)
        self.assertEqual(self.match.away_score, 0)
        self.assertEqual(self.match.status, "Not started")
        
        # Validate updated match
        self.assertEqual(updated_match.home_score, 3)
        self.assertEqual(updated_match.away_score, 1)
        self.assertEqual(updated_match.status, "Not started")
        
        # Validate finished match
        self.assertEqual(finished_match.home_score, 3)
        self.assertEqual(finished_match.away_score, 1)
        self.assertEqual(finished_match.status, "Finished")
    
    def test_team_name_validation(self):
        with self.assertRaises(ValueError):
            Match(home_team="Invalid Team!", away_team="TeamB")
    
    def test_same_team_validation(self):
        with self.assertRaises(ValueError):
            Match(home_team="TeamA", away_team="TeamA")
    
    def test_negative_scores(self):
        with self.assertRaises(ValueError):
            self.match.update_score(-1, 2)
        with self.assertRaises(ValueError):
            self.match.update_score(1, -2)
    
    def test_total_score(self):
        updated_match = self.match.update_score(2, 3)
        self.assertEqual(updated_match.get_total_score(), 5)
    
    def test_unique_ids_for_new_instances(self):
        new_match = self.match.update_score(1, 1)
        self.assertEqual(self.match.match_id, new_match.match_id)
