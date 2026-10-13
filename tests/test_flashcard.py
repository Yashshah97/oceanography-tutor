import unittest
from oceanography_tutor import flashcard

class TestFlashcard(unittest.TestCase):

    def test_flashcard_init(self):
        card = flashcard.Flashcard('question', 'answer')
        self.assertEqual(card.question, 'question')
        self.assertEqual(card.answer, 'answer')

    def test_flashcard_repr(self):
        card = flashcard.Flashcard('question', 'answer')
        self.assertEqual(repr(card), "Flashcard(question='question', answer='answer')")

    def test_flashcard_deck_init(self):
        deck = flashcard.FlashcardDeck()
        self.assertEqual(deck.cards, [])

    def test_flashcard_deck_add_card(self):
        deck = flashcard.FlashcardDeck()
        card = flashcard.Flashcard('question', 'answer')
        deck.add_card(card)
        self.assertEqual(len(deck.get_cards()), 1)

if __name__ == '__main__':
    unittest.main()
