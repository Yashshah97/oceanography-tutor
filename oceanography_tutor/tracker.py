"""
Module for progress tracking and storage.

Classes:
    Tracker: Tracks the progress of a user through their flashcards.
"""

class Tracker:
    """
    Tracks the progress of a user through their flashcards.

    Attributes:
        cards (dict): A dictionary mapping card IDs to their respective data.
        last_review (dict): A dictionary mapping card IDs to their last review dates.
    """

    def __init__(self):
        self.cards = {}
        self.last_review = {}

    def add_card(self, card_id, front, back):
        """
        Adds a new flashcard to the tracker.

        Args:
            card_id (str): The ID of the flashcard.
            front (str): The front side of the flashcard.
            back (str): The back side of the flashcard.
        """
        self.cards[card_id] = {"front": front, "back": back}
        self.last_review[card_id] = 0

    def review_card(self, card_id):
        """
        Marks a flashcard as reviewed.

        Args:
            card_id (str): The ID of the flashcard to mark as reviewed.
        """
        if card_id in self.cards:
            self.last_review[card_id] += 1
        else:
            raise ValueError("Card not found")

    def get_progress(self, card_id):
        """
        Gets the progress of a flashcard.

        Args:
            card_id (str): The ID of the flashcard to get the progress for.

        Returns:
            int: The number of times the flashcard has been reviewed.
        """
        return self.last_review.get(card_id, 0)

    def delete_card(self, card_id):
        """
        Deletes a flashcard from the tracker.

        Args:
            card_id (str): The ID of the flashcard to delete.
        """
        if card_id in self.cards:
            del self.cards[card_id]
            del self.last_review[card_id]
        else:
            raise ValueError("Card not found")

def main():
    pass

if __name__ == "__main__":
    tracker = Tracker()
    tracker.add_card("1", "Front side of card 1", "Back side of card 1")
    print(tracker.get_progress("1"))  # Output: 0
    tracker.review_card("1")
    print(tracker.get_progress("1"))  # Output: 1
