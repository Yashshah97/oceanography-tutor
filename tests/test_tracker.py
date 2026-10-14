import unittest
from oceanography_tutor import tracker

class TestTracker(unittest.TestCase):

    def test_add_card(self):
        tracker = tracker.Tracker()
        tracker.add_card("1", "Front side of card 1", "Back side of card 1")
        self.assertIn("1", tracker.cards)
        self.assertEqual(tracker.cards["1"]["front"], "Front side of card 1")

    def test_review_card(self):
        tracker = tracker.Tracker()
        tracker.add_card("1", "Front side of card 1", "Back side of card 1")
        tracker.review_card("1")
        self.assertEqual(tracker.get_progress("1"), 1)

    def test_get_progress(self):
        tracker = tracker.Tracker()
        tracker.add_card("1", "Front side of card 1", "Back side of card 1")
        self.assertEqual(tracker.get_progress("1"), 0)
        tracker.review_card("1")
        self.assertEqual(tracker.get_progress("1"), 1)

    def test_delete_card(self):
        tracker = tracker.Tracker()
        tracker.add_card("1", "Front side of card 1", "Back side of card 1")
        tracker.delete_card("1")
        self.assertNotIn("1", tracker.cards)
        with self.assertRaises(ValueError):
            tracker.get_progress("1")

if __name__ == "__main__":
    unittest.main()
