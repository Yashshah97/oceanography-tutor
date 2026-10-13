import unittest
from oceanography_tutor import tutor

class TestTutor(unittest.TestCase):
    def test_add_card(self):
        tutor = tutor.Tutor()
        card = tutor.Card("What is the tide?", "The rise and fall of sea level due to gravitational forces.")
        tutor.add_card(card)
        self.assertEqual(len(tutor.cards), 1)

    def test_review_cards(self):
        tutor = tutor.Tutor()
        card = tutor.Card("What is the tide?", "The rise and fall of sea level due to gravitational forces.")
        card.last_reviewed = date.today() - timedelta(days=8)
        tutor.add_card(card)
        tutor.review_cards()
        self.assertEqual(card.last_reviewed, date.today())

    def test_get_next_card(self):
        tutor = tutor.Tutor()
        card1 = tutor.Card("What is the tide?", "The rise and fall of sea level due to gravitational forces.")
        card2 = tutor.Card("What is salinity?", "The concentration of dissolved salts in seawater.")
        card3 = tutor.Card("What is buoyancy?", "The upward force exerted by a fluid on an object partially or fully submerged in it.")
        card1.last_reviewed = date.today() - timedelta(days=7)
        card2.last_reviewed = date.today() - timedelta(days=8)
        card3.last_reviewed = date.today()
        tutor.add_card(card1)
        tutor.add_card(card2)
        tutor.add_card(card3)
        next_card = tutor.get_next_card()
        self.assertEqual(next_card, card2)

if __name__ == "__main__":
    unittest.main()
