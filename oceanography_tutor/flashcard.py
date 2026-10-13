"""
Flashcard model and operations.

This module defines the `Flashcard` class, which represents a flashcard with
question and answer data. It also provides methods for creating new flashcards,
saving them to memory, and retrieving existing ones.
"""

class Flashcard:
    """
    A flashcard with question and answer data.

    Attributes:
        question (str): The question on the flashcard.
        answer (str): The answer to the question on the flashcard.
    """

    def __init__(self, question: str, answer: str):
        """
        Initialize a new flashcard.

        Args:
            question (str): The question on the flashcard.
            answer (str): The answer to the question on the flashcard.
        """
        self.question = question
        self.answer = answer

    def __repr__(self) -> str:
        return f"Flashcard(question='{self.question}', answer='{self.answer}')"

class FlashcardDeck:
    """
    A collection of flashcards.

    Attributes:
        cards (list): The list of flashcards in the deck.
    """

    def __init__(self):
        self.cards = []

    def add_card(self, card: Flashcard) -> None:
        """
        Add a new flashcard to the deck.

        Args:
            card (Flashcard): The flashcard to add.
        """
        self.cards.append(card)

    def get_cards(self) -> list:
        """
        Get all flashcards in the deck.

        Returns:
            list: A list of `Flashcard` objects.
        """
        return self.cards
